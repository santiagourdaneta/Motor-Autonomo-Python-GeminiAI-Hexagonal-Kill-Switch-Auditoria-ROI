class ReviewerAgent:
    def __init__(self, client):
        self.client = client

    def review_plan(self, plan_data: str) -> dict:
        # Prompt enfocado en seguridad y realismo
        prompt = f"Actúa como un Auditor de Seguridad Cloud. Revisa este plan de migración y detecta riesgos: {plan_data}"
        
        # Aquí llamarías a la IA (usando la nueva google-genai)
        # Por ahora, simulamos la lógica de validación
        return {
            "is_secure": True,
            "audit_score": 9.5,
            "observations": "Arquitectura serverless validada. Riesgo de latencia bajo."
        }