from fastapi import FastAPI
from app.routes import namaste, icd, mapping

app = FastAPI(title="NAMASTE ↔ ICD11 FHIR API")

@app.get("/")
def read_root():
    return {"message": "Welcome to the NAMASTE ↔ ICD11 FHIR API"}


app.include_router(namaste.router)
app.include_router(icd.router)
app.include_router(mapping.router)