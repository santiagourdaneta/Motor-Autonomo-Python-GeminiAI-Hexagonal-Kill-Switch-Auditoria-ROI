import asyncio
import os

from dotenv import load_dotenv
from src.adapters.gemini_adapter import GeminiAdapter
from src.adapters.memory_event_bus import MemoryEventBus
from src.adapters.vector_db_adapter import VectorDBAdapter
from src.use_cases.orchestrate_migration import MigrationOrchestrator

load_dotenv()


async def main():
    # Inicializar componentes
    bus = MemoryEventBus()
    db = VectorDBAdapter()
    ai = GeminiAdapter(api_key=os.getenv("GEMINI_API_KEY"))

    orchestrator = MigrationOrchestrator(ai, db)

    # Suscribir orquestador al bus
    bus.subscribe("FILE_UPLOADED", orchestrator.handle_migration_event)

    print("🤖 Sistema Activo. Simulando evento de entrada...")
    await bus.publish(
        "FILE_UPLOADED",
        {
            "filename": "old_script.py",
            "content": "def connect_db(): pass",
            "lang": "python",
        },
    )


if __name__ == "__main__":
    asyncio.run(main())
