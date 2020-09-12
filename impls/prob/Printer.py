
def pr_str(obj):
    if type(obj) == str:
        return str(obj)
    elif type(obj) == int:
        return int(obj)
    elif type(obj) == list:
        lst = []
        for n in obj:
            if type(n) == list:
                n = pr_str(n)
            else:
                n = str(n)
            lst.append(n)
        s = ' '.join(lst)
        s = f'({s})'
        return str(s)
