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
    
    def setNil(self):
        self.type = Type.NIL
        self.data = None
    
    def setTrue(self):
        self.type = Type.TRUE
        self.data = True
    
    def setFalse(self):
        self.type = Type.FALSE
        self.data = False

    def String(self, data):
        self.type = Type.STR
        self.data = data

    def Number(self, data):
        self.type = Type.NUMBER
        self.data = data

    def Symbol(self, data):
        self.type = Type.SYMBOL
        self.data = data

    def Keyword(self, data):
        self.type = Type.KEYWORD
        self.data = data

    def Function(self, data):
        self.type = Type.FUNCTION
        self.data = data

    def List(self, data):
        self.type = Type.LIST
        self.data = data

    def Vector(self, data):
        self.type = Type.VECTOR
        self.data = data
    
    def HashMap(self, data):
        self.type = Type.HASH_MAP
        self.data = data

    def Atom(self, data):
        self.type = Type.ATOM
        self.data = data




