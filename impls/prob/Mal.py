from enum import Enum

class Type(Enum):
    NIL = 0
    TRUE = 1
    FALSE = 2
    STR = 3
    NUMBER = 4
    SYMBOL = 5
    KEYWORD = 6
    FUNCTION = 7
    LIST = 8
    VECTOR = 9
    HASH_MAP = 10
    ATOM = 11

class Data():
    def __init__(self, type, data):
        self.type = type
        self.data = data


# ===== New Classes =====

class Symbol(str): pass
class Keyword(str): pass 
class Atom(str): pass
class Vector(list):
        def __init__(self,*args) -> None:
            super().__init__(args)

class HashMap(dict): pass
class Nil(int):
    def __bool__():
        return False
    def __str__(self) -> str:
        return 'nil'

class Tru(int):
    def __bool__():
        return True
    def __str__(self) -> str:
        return 'true'

class Fal(int):
    def __bool__():
        return False
    def __str__(self) -> str:
        return 'false'

class Func(object):
    def __init__(self, fn) -> None:
        self.fn = fn
    def call(self):
        return self.fn()
