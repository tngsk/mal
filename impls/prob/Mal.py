class Symbol(str): pass
class Keyword(str): pass 
class Atom(str): pass
class Vector(list): pass
class HashMap(list): pass

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
