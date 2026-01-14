import pytest
from src.adapters.memory_event_bus import MemoryEventBus


@pytest.mark.asyncio
async def test_smoke_pipeline():
    bus = MemoryEventBus()
    received = []

    async def handler(data):
        received.append(data)

    bus.subscribe("SMOKE_TEST", handler)
    await bus.publish("SMOKE_TEST", {"status": "ok"})

    assert len(received) == 1
    assert received[0]["status"] == "ok"
