class TesterAgent:
    def generate_contract_test(self, plan_json: dict):
        # Simulación de Pact: Verifica que las llaves esenciales existan
        required_keys = [
            "legacy_id",
            "suggested_architecture",
            "steps",
            "estimated_roi_multiplier",
        ]
        for key in required_keys:
            if key not in plan_json:
                raise ValueError(f"🚨 Contrato roto: Falta la llave {key}")
        print("✅ Test de Contrato (Pact-style) aprobado.")
