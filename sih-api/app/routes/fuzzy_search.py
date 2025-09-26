from fastapi import APIRouter, Query
import pandas as pd
from fuzzywuzzy import process

router = APIRouter()
namaste_df = pd.read_csv("app/data/namaste_mock_data.csv")
icd_df = pd.read_csv("app/data/icd_mock_data.csv")

@router.get("/search")
def search_disease(name: str = Query(..., min_length=1), limit: int = 5, threshold: int = 70):
    search_keys = list(namaste_df['display']) + list(namaste_df['code']) + \
                  list(icd_df['display']) + list(icd_df['code'])
    
    matches = process.extract(name, search_keys, limit=limit)
    results = []

    for match_text, score in matches:
        if score < threshold:
            continue
        row_n = namaste_df[(namaste_df['display'] == match_text) | (namaste_df['code'] == match_text)]
        row_i = icd_df[(icd_df['display'] == match_text) | (icd_df['code'] == match_text)]
        if not row_n.empty:
            r = row_n.iloc[0]
            results.append({"source": "NAMASTE", "code": r['code'], "display": r['display'], "definition": r['definition']})
        if not row_i.empty:
            r = row_i.iloc[0]
            results.append({"source": "ICD", "system": r['system'], "code": r['code'], "display": r['display'], "definition": r['definition']})

    if results:
        return {"results": results}
    return {"message": "No match found"}
