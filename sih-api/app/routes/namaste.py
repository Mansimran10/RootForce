from fastapi import APIRouter, Query
import pandas as pd

router = APIRouter()
namaste_df = pd.read_csv("app/data/namaste_mock_data.csv")

@router.get("/namaste/search")
def search_namaste(code: str = Query(..., min_length=1)):
    # Exact match check
    row = namaste_df[namaste_df['code'] == code]
    if not row.empty:
        r = row.iloc[0]
        return {
            "resourceType": "CodeSystem",
            "concepts": [
                {
                    "code": r['code'],
                    "display": r['display'],
                    "definition": r.get('definition', None)
                }
            ]
        }
    
    # Agar code galat ho
    return {"message": "No match found. Please try another Namaste code."}
