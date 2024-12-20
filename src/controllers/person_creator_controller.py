from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
import re
from .interfaces.person_creator_controller import PersonCreatorControllerInterface

class PersonCreatorController(PersonCreatorControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

        def create(self, person_info: dict) -> dict:
            first_name = person_info.get('first_name')
            last_name = person_info.get('last_name')
            age = person_info.get('age')
            pet_id = person_info.get('pet_id')

            self.__validate_first_and_last_name(first_name, last_name)
            self.__insert_person_in_db(first_name, last_name, age, pet_id)
            formatted_response = self.__format_response(person_info)
            return formatted_response

            
        def __validate_first_and_last_name(self,first_name: str, last_name: str) -> None:
            """_summary_

            Args:
                first_name (str): _description_
                last_name (str): _description_

            Raises:
                Exception: _description_
            """
            non_valid_caracters = re.compile(r'[^a-zA-Z]')
            if non_valid_caracters.search(first_name) or non_valid_caracters.search(last_name):
                raise Exception('Invalid first or last name')
            
        def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
            """_summary_

            Args:
                first_name (str): _description_
                last_name (str): _description_
                age (int): _description_
                pet_id (int): _description_
            """
            self.__people_repository.insert_person(first_name, last_name, age, pet_id)

        def __format_response(self, person_info: dict) -> dict:
            return {
                "data": {
                    "type": "Person",
                    "count": 1,
                    "attributes": person_info
                }
            }
        
if __name__ == '__main__':
    person = PersonCreatorController()
    person.create({'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'pet_id': 1})