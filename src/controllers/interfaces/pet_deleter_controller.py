from abc import ABC,abstractmethod

class PetDeleterInterface(ABC):

    @abstractmethod
    def delete(self, name: str) -> None:
        pass
        