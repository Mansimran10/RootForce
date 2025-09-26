from pydantic import BaseModel
from typing import List, Optional

class CodeSystemConcept(BaseModel):
    code: str
    display: str
    definition: Optional[str] = None

class CodeSystem(BaseModel):
    resourceType: str = "CodeSystem"
    id: str
    name: str
    concept: List[CodeSystemConcept]

class ConceptMapMapping(BaseModel):
    source_code: str
    target_code: str
    relationship: str

class ConceptMap(BaseModel):
    resourceType: str = "ConceptMap"
    id: str
    name: str
    mappings: List[ConceptMapMapping]
