from abc import ABC, abstractmethod

class PersonCreatorInterface(ABC):
        
        @abstractmethod
        def create(self, person_info: dict) -> dict:
           pass
