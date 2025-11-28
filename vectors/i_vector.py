from abc import ABC, abstractmethod

class IVector(ABC):

    @abstractmethod
    def abs(self) -> float:
        pass

    @abstractmethod
    def cdot(self, v: 'IVector') -> float:
        pass

    @abstractmethod
    def get_components(self) -> tuple[float, float]:
        pass