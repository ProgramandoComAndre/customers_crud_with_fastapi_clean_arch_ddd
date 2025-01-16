
class Nif:
    def __validate_digit(self, digit:str):
        if not digit.isdigit(): raise ValueError
        soma = sum([int(digito) * (9 - pos) for pos, digito in enumerate(digit)])
        resto = soma % 11
        if resto == 0: return '0'
        if resto == 1: return '0'
        return str(11 - resto)
    def __validate_nif(self, value:str):
        EXPECTED_DIGITS = 9
        if not value.isdigit() or len(value) != EXPECTED_DIGITS: 
            return False
        return value[-1] == self.__validate_digit(value[0:8])
    def __init__(self, value):
        if self.__validate_nif(value):
            self.__value = value
            return
        raise ValueError("Not a NIF")
    def __str__(self):
        return self.__value
    def __eq__(self, value):
        return self.__value == str(value)
