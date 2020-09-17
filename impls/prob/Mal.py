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

