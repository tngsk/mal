from enum import Enum

class MalType(Enum):
    NIL = 0
    TRUE = 1
    FALSE = 2
    STRING = 3
    NUMBER = 4
    SYMBOL = 5
    KEYWORD = 6
    FUNCTION = 7
    LIST = 8
    VECTOR = 9
    HASH_MAP = 10
    ATOM = 11

class MalData(type, data):
    def __init__(self, type, data):
        self.type = type
        self.data = data

