from src.ports.event_bus import EventBus


class MemoryEventBus(EventBus):
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type: str, handler):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(handler)

    async def publish(self, event_type: str, data: dict):
        print(f"📢 Evento publicado: {event_type}")
        if event_type in self.subscribers:
            for handler in self.subscribers[event_type]:
                # Usamos asyncio para que sea no-bloqueante (Escalabilidad)
                await handler(data)
