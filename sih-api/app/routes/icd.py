from fastapi import APIRouter, Query
import pandas as pd

router = APIRouter()
icd_df = pd.read_csv("app/data/icd_mock_data.csv")

@router.get("/icd/search")
def search_icd(code: str = Query(..., min_length=1)):
    row = icd_df[icd_df['code'].str.lower() == code.lower()]
    if not row.empty:
        r = row.iloc[0]
        return {"system": r['system'], "code": r['code'], "display": r['display'], "definition": r['definition']}
    return {"message": "ICD code not found"}
