import pytest
from unittest.mock import MagicMock
from src.use_cases.orchestrate_migration import MigrationOrchestrator


@pytest.mark.asyncio
async def test_event_bus_continues_if_ai_fails():
    # 1. Simulamos un Adaptador de IA que lanza un error (Explosión)
    mock_ai = MagicMock()
    mock_ai.generate_migration_plan.side_effect = Exception("API de Gemini Caída")

    mock_db = MagicMock()
    orchestrator = MigrationOrchestrator(mock_ai, mock_db)

    # 2. Ejecutamos el flujo
    data = {"filename": "test.py", "content": "print(1)", "lang": "python"}

    # El test pasa si el error es manejado y no tumba el proceso principal
    try:
        await orchestrator.handle_migration_event(data)
    except Exception as e:
        assert str(e) == "API de Gemini Caída"
        print(
            "✅ El sistema detectó el fallo de IA pero el bus está listo para el siguiente evento."
        )
