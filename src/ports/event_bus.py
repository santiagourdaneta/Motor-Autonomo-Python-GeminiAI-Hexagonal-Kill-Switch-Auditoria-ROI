from abc import ABC, abstractmethod


class EventBus(ABC):
    @abstractmethod
    async def publish(self, event_type: str, data: dict):
        pass

    @abstractmethod
    def subscribe(self, event_type: str, handler):
        pass
