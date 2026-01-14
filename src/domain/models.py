from pydantic import BaseModel
from datetime import datetime
from typing import List


class LegacyCode(BaseModel):
    id: str
    filename: str
    content: str
    language: str


class MigrationStep(BaseModel):
    step_number: int
    action: str  # Ej: "Refactorizar a Función Lambda"
    reasoning: str


class MigrationPlan(BaseModel):
    legacy_id: str
    suggested_architecture: str
    steps: List[MigrationStep]
    estimated_roi_multiplier: float  # Impacto de negocio
    created_at: datetime = datetime.now()
