import asyncio
from unittest.mock import MagicMock
from src.use_cases.orchestrate_migration import MigrationOrchestrator
from src.domain.models import MigrationPlan

async def test_kill_switch_activation():
    print("\n🔥 [TEST] Iniciando Sabotaje para activar el Kill Switch...")
    
    # Mockeamos una IA que genera un plan mediocre
    mock_ai = MagicMock()
    mock_ai.client = "fake_client"
    mock_ai.generate_migration_plan.return_value = MigrationPlan(
        legacy_id="666",
        suggested_architecture="Spaghetti Code on Windows 95",
        steps=[],
        estimated_roi_multiplier=0.1
    )
    
    # Mockeamos el Revisor para que dé una nota baja (Simulando auditoría fallida)
    # Importante: Aquí forzamos el score a 3.0
    from src.domain.reviewer_agent import ReviewerAgent
    ReviewerAgent.review_plan = MagicMock(return_value={
        "is_secure": False,
        "audit_score": 3.0,
        "observations": "Riesgo crítico: La arquitectura sugerida es obsoleta y costosa."
    })

    orchestrator = MigrationOrchestrator(mock_ai, MagicMock())
    
    await orchestrator.handle_migration_event({
        "filename": "dangerous_script.py",
        "content": "eval(input())", # Código peligroso
        "lang": "python"
    })
    
    print("✅ [TEST FINISHED] Si viste el mensaje de 'KILL SWITCH' y no hay reporte en output/, el sistema es seguro.")

if __name__ == "__main__":
    asyncio.run(test_kill_switch_activation())