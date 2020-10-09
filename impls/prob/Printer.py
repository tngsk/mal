import re
from mal import *

def pr_str(obj, print_readably=True):
    
    if type(obj) is str:
        if print_readably:
            obj = re.sub('"','\"',obj)
            #obj = f'"{obj}"'
        
        return obj
    
    elif type(obj) is Number:
        return str(obj)

    elif type(obj) is int:
        return str(obj)

    elif type(obj) is float:
        return str(obj)

    elif type(obj) is list:
        lst = []
        for n in obj:
            lst.append(pr_str(n))
        s = ' '.join(lst)
        s = f'({s})'
        return str(s)

    elif type(obj) is Vector:
        lst = []
        for n in obj:
            lst.append(pr_str(n))
        s = ' '.join(lst)
        s = f'[{s}]'
        return s  

    elif type(obj) is HashMap:
        lst = []
        for n in obj:
            lst.append(pr_str(n))
        s = ' '.join(lst)
        s = '{' + s + '}'
        return s

    elif type(obj) is Fn:
        return '#<function>'

    elif type(obj) is Nil:
        return 'nil'

    elif type(obj) is Tru:
        return 'true'

    elif type(obj) is Fal:
        return 'false'

    else:
        return obj
