import Mal

def pr_str(obj, print_readably=True):
    
    if type(obj) is str:
        return obj
    
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

    elif type(obj) is Mal.Vector:
        lst = []
        for n in obj:
            lst.append(pr_str(n))
        s = ' '.join(lst)
        s = f'[{s}]'
        return s  

    elif type(obj) is Mal.HashMap:
        lst = []
        for n in obj:
            lst.append(pr_str(n))
        s = ' '.join(lst)
        s = '{' + s + '}'
        return s

    elif type(obj) is Mal.Func:
        return '#<function>'

    elif type(obj) is Mal.Nil:
        return 'nil'

    elif type(obj) is Mal.Tru:
        return 'true'

    elif type(obj) is Mal.Fal:
        return 'false'

    else:
        return obj
