from mal import *
import printer

def prn(*arg):
    print(printer.pr_str(arg[0], True))
    return Nil()

def _str(*arg):
    return "".join(list(map(lambda x: printer.pr_str(x,False), arg)))

def pr_str(*arg):
    return " ".join(list(map(lambda x: printer.pr_str(x,True), arg)))

def _println(*arg):
    return " ".join(list(map(lambda x: printer.pr_str(x,False), arg)))

def makelist(*arg):
    return list(arg)

def isList(*arg):
    if (type(arg[0]) is list) or (type(arg[0]) is tuple):
        return Tru()
    else:
        return Fal()

def isEmpty(*arg):
    if len(list(arg[0])) == 0:
        return Tru()
    else:
        return Fal()

def count(*arg):
    if type(arg[0]) is Nil:
        return 0
    else:
        r = len(list(arg[0]))
        return r

def eq(*arg):
    s1 = str(arg[0])
    s2 = str(arg[1])
    if s1 is s2:
        return Tru()
    else:
        return Fal()

ns = {

    '+': lambda a,b: a + b,
    '-': lambda a,b: a - b,
    '*': lambda a,b: a * b,
    '/': lambda a,b: int(a/b),
    '<': lambda a,b: Tru() if a < b else Fal(),
    '<=': lambda a,b: Tru() if a <= b else Fal(),
    '>': lambda a,b: Tru() if a > b else Fal(),
    '>=': lambda a,b: Tru() if a >= b else Fal(),
    '=': lambda a,b: Tru() if a == b else Fal(),

    'prn': prn,
    'list': makelist,
    'list?': isList,
    'empty?': isEmpty,
    'count': count,
    'pr-str': pr_str,
    'str': _str,
    'println': _println,

}
