from abc import ABC, abstractmethod

class PetListerInterface(ABC):
 
    @abstractmethod
    def list(self) -> dict:
        pass