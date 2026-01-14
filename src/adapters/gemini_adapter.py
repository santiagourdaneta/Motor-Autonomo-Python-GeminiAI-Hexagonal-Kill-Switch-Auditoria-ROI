import json

from google import genai
from src.domain.models import MigrationPlan


class GeminiAdapter:
    def __init__(self, api_key):
        # Forzamos la v1 para evitar el 404 de la beta
        self.client = genai.Client(api_key=api_key, http_options={"api_version": "v1"})
        self.model_id = "gemini-1.5-flash"

    def generate_migration_plan(self, legacy_code) -> MigrationPlan:
        # Prompt ultra-detallado para que la IA no invente campos
        prompt = (
            f"Analiza este código: {legacy_code.content}. "
            "Genera un plan de migración en JSON con esta estructura exacta: "
            "{"
            '  "architecture": "string", '
            '  "steps": [{"step_number": 1, "action": "string", "reasoning": "string"}], '
            '  "roi": 0.0'
            "}"
        )

        try:
            response = self.client.models.generate_content(
                model=self.model_id, contents=prompt
            )

            clean_text = response.text.replace("```json", "").replace("```", "").strip()
            raw_json = json.loads(clean_text)

            return MigrationPlan(
                legacy_id=legacy_code.id,
                suggested_architecture=raw_json.get("architecture", "N/A"),
                steps=raw_json.get("steps", []),
                estimated_roi_multiplier=float(raw_json.get("roi", 0)),
            )
        except Exception as e:
            print(f"⚠️ [AI_FALLBACK] Activado por error: {e}")
            # FALLBACK: Cumpliendo estrictamente con los campos: step_number, action, reasoning
            return MigrationPlan(
                legacy_id=legacy_code.id,
                suggested_architecture="Revisión Manual por Fallo de API",
                steps=[
                    {
                        "step_number": 1,
                        "action": "Verificar conectividad con Google Cloud v1",
                        "reasoning": "La API devolvió un error 404 o 400 durante la generación.",
                    }
                ],
                estimated_roi_multiplier=0.0,
            )
