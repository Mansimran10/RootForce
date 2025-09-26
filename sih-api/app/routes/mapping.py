from fastapi import APIRouter, Query
import pandas as pd

router = APIRouter()
mapping_df = pd.read_csv("app/data/mapping_mock.csv")

@router.get("/translate")
def translate_code(code: str = Query(..., min_length=1)):
    row = mapping_df[(mapping_df['namaste_code'].str.lower() == code.lower()) |
                     (mapping_df['icd_code'].str.lower() == code.lower())]
    if not row.empty:
        r = row.iloc[0]
        return {"namaste_code": r['namaste_code'], "icd_code": r['icd_code']}
    return {"message": "Code not found"}
