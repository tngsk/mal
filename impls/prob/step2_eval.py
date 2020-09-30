import sys
import Reader
import Printer
import Mal

repl_env = {'+': lambda a,b: a + b,
            '-': lambda a,b: a - b,
            '*': lambda a,b: a * b,
            '/': lambda a,b: int(a/b)}

def READ(arg):
    return Reader.read_str(arg)

def PRINT(arg):
    return Printer.pr_str(arg)

def EVAL(ast, env):
    if not type(ast) is list:
        return eval_ast(ast, env)
    elif len(ast) == 0:
        return ast
    elif type(ast) is list:
        fn = eval_ast(ast, env)
        return Mal.Number(eval_function(fn))

    else:
        raise Exception("EVAL: Type Error")
 
def eval_function(el):
    func = el[0]
    args = []
    for arg in el[1:]:
        if type(arg) is Mal.Number:
            args.append(int(arg))
        else:
            args.append(arg)
    return func(*args)

def eval_ast(ast, env):
    
    if type(ast) is Mal.Symbol:
        try:
            return env[ast]
        except:
            raise Exception("no value is found")

    elif type(ast) is list:
        lst = list(map(lambda x: EVAL(x, env), ast))
        return lst

    elif type(ast) is Mal.Vector:
        lst = list(map(lambda x: EVAL(x, env), ast))
        return Mal.Vector(lst)

    elif type(ast) is Mal.HashMap:
        lst = []
        for i in range(0, len(ast), 2):
            lst.append(ast[i])
            lst.append(EVAL(ast[i+1], env))
        return Mal.HashMap(lst)
    else:
        return ast

def rep(arg):
    r = READ(arg)
    e = EVAL(r, repl_env)
    p = PRINT(e)
    print(p)
    
def LOOP():
    while True:
        try:
            print('user> ', end='')
            line = input()
            if line:
                rep(line)
            else:
                sys.exit(0)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    LOOP()