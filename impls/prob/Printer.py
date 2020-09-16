
def pr_str(obj, print_readably=True):
    if type(obj) == str:

        # keyword
        if obj[0] == "\u029e":
            obj = ":" + obj[1:]

        return str(obj)
    elif type(obj) == int:
        return str(obj)
    elif type(obj) == list:
        lst = []
        for n in obj:
            lst.append(pr_str(n))
        s = ' '.join(lst)
        s = f'({s})'
        return str(s)
    else:
        return str(obj)

