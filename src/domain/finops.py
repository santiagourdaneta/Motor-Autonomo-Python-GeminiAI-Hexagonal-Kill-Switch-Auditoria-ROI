class FinOpsGuard:
    @staticmethod
    def validate_query_cost(estimated_tokens: int):
        # Si la consulta va a costar más de $2 (ejemplo exagerado para BigQuery)
        if estimated_tokens > 1000000:
            print("⚠️ BLOQUEO FINOPS: Esta consulta es demasiado cara. Optimiza antes.")
            return False
        return True
