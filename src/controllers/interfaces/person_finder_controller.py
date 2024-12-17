from abc import ABC, abstractmethod

class PersonFinderInterface(ABC):
        
        @abstractmethod
        def find(self, person_id: int) -> dict:
                pass

       