
class Number(int): pass
class Symbol(str): pass
class Keyword(str): pass 
class Atom(str): pass
class Vector(list): pass
class HashMap(list): pass

class Nil(int):
    def __bool__(self):
        return False
    def __str__(self) -> str:
        return 'nil'

class Tru(int):
    def __bool__(self):
        return True
    def __str__(self) -> str:
        return 'true'

class Fal(int):
    def __bool__(self):
        return False
    def __str__(self) -> str:
        return 'false'

class Fn(object):
    def __init__(self,fn) -> None:
        self.fn = fn
    def __call__(self, *args, **kwds) -> None:
        return self.fn(*args)
