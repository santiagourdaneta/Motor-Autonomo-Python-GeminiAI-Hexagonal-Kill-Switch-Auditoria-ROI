from abc import ABC, abstractmethod
from src.domain.models import LegacyCode, MigrationPlan


class AIModelPort(ABC):
    @abstractmethod
    def generate_migration_plan(self, code: LegacyCode) -> MigrationPlan:
        """Este método define QUÉ queremos, no CÓMO se hace."""
        pass
