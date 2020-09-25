import Mal

def pr_str(obj, print_readably=True):
    
    if obj.type == Mal.Type.STR:

        # # keyword
        # if obj.type == Mal.Type.KEYWORD:
        #     obj.data = ":" + obj.data[1:]

        return str(obj.data)
    
    elif obj.type == Mal.Type.NUMBER:
        return str(obj.data)

    elif obj.type == Mal.Type.LIST:
        lst = []
        for n in obj.data:
            lst.append(pr_str(n))
        s = ' '.join(lst)
        s = f'({s})'
        return str(s)

    elif obj.type == Mal.Type.VECTOR:
        lst = []
        for n in obj.data:
            lst.append(pr_str(n))
        s = ' '.join(lst)
        s = f'[{s}]'
        return str(s)  

    elif obj.type == Mal.Type.HASH_MAP:
        lst = []
        for n in obj.data:
            lst.append(pr_str(n))
        s = ' '.join(lst)
        s = '{' + s + '}'
        return str(s)

    elif obj.type ==  Mal.Type.FUNCTION:
        return str('#<function>')

    else:
        return str(obj.data)
