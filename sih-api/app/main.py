from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import namaste, icd, mapping, fuzzy_search

app = FastAPI(title="NAMASTE ↔ ICD11 FHIR API")

# Serve frontend static files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Include routers
app.include_router(namaste.router)
app.include_router(icd.router)
app.include_router(mapping.router)
app.include_router(fuzzy_search.router)

@app.get("/")
def read_root():
    return {"message": "Go to /static/index.html to use the GUI"}
