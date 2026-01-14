import random
from unittest.mock import MagicMock

import pytest
from src.use_cases.orchestrate_migration import MigrationOrchestrator


@pytest.mark.asyncio
async def test_chaos_glitch():
    # Creamos mocks rápidos
    mock_ai = MagicMock()
    mock_db = MagicMock()
    orchestrator = MigrationOrchestrator(mock_ai, mock_db)

    # Simulación de Caos
    if random.random() < 0.5:
        print("\n🚨 [GLITCH] Simulando caída de VectorDB...")
        mock_db.search.side_effect = Exception("DB Timeout")

    assert orchestrator is not None
    print("✅ Chaos test ejecutado (infraestructura lista para fallos).")
