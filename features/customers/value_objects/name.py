from typing import Optional
class Name:
    def __init__(self, first_name: str, last_name: Optional[str] = ""):
        if len(first_name) == 0:
            raise ValueError("First name can't be empty")
        self.__first_name = first_name.capitalize()
        self.__last_name = last_name.capitalize() 
    
    def __str__(self):
        return self.__first_name + " "+ self.__last_name
    def __eq__(self, name):
        return name.first_name == self.first_name and name.last_name == self.last_name