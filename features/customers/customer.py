from .value_objects import Nif, Name
import uuid
class Customer:
    def __init__(self, name: Name, nif: Nif , id:uuid.UUID=None):
        self.__id = id
        self.__nif = nif
        self.__name = name

    def get_name(self):
        return self.__name

    def set_nif(self, nif:Nif):
        self.__nif = nif
    def get_nif(self):
        return self.__nif
    def get_id(self):
        return str(self.__id)
    def set_name(self, name:str):
        if len(name) > 0:
            self.__name = name