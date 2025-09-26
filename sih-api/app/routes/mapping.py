from fastapi import APIRouter, Query
import pandas as pd
from app.models import ConceptMap, ConceptMapMapping

router = APIRouter()

map_df = pd.read_csv("app/data/combined_namaste_icd_snomed_loinc.csv")

@router.get("/translate")
def translate_code(
    system: str = Query(..., description="Source system (NAM or TM2)"),
    code: str = Query(..., description="Code to translate")
):
    """Bidirectional translational system for NAMASTE, ICD11_TM2, SNOMED CT, and LOINC"""

    system = system.upper()
    code = code.strip()

    if system == "NAM":
        matches = map_df[map_df["source_code"] == code]
        mappings = [
            ConceptMapMapping(
                source_code=row["source_code"],
                target_code=row["target_code"],
                relationship=row["relationship"],
                snomed_ct_code=str(row["snomed_ct_code"]),
                loinc_code=str(row["loinc_code"]),
            )
            for _, row in matches.iterrows()
        ]
    elif system == "TM2":
        matches = map_df[map_df["target_code"] == code]
        mappings = [
            ConceptMapMapping(
                source_code=row["target_code"],
                target_code=row["source_code"],
                relationship=row["relationship"],
                snomed_ct_code=str(row["snomed_ct_code"]),
                loinc_code=str(row["loinc_code"]),
            )
            for _, row in matches.iterrows()
        ]
    else:
        return {"error": "Unsupported system. Use NAMASTE(NAM) or ICD11(TM2)."}

    return ConceptMap(id="ConceptMap", name="NAMASTE-ICD11-SNOMED-LOINC Map", mappings=mappings)
