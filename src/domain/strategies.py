from abc import ABC, abstractmethod


class MigrationStrategy(ABC):
    @abstractmethod
    def get_prompt_extension(self) -> str:
        pass


class PythonStrategy(MigrationStrategy):
    def get_prompt_extension(self) -> str:
        return "Enfócate en PEP8 y usa FastAPI para la nueva versión."


class JavascriptStrategy(MigrationStrategy):
    def get_prompt_extension(self) -> str:
        return "Convierte a TypeScript y usa Clean Architecture en el backend."
