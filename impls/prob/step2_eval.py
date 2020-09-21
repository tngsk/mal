import sys
import traceback

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
    if not ast.type == Mal.Type.LIST:
        return eval_ast(ast, env)
    elif len(ast.data) == 0:
        return ast
    elif ast.type == Mal.Type.LIST:
        el = eval_ast(ast, env)
        evaluted = eval_function(el)
        return Mal.Data(Mal.Type.STR, evaluted)

    else:
        raise Exception("EVAL: Type Error")
 
def eval_function(el):
    func = el.data[0]
    args = []
    for arg in el.data[1:]:
        if arg.type == Mal.Type.NUMBER:
            args.append(int(arg.data))
        else:
            args.append(arg.data)
    return func(*args)

def eval_ast(ast, env):
    if ast.type == Mal.Type.SYMBOL:
        try:
            return env[ast.data]
        except:
            raise Exception("no value is found")
    elif ast.type == Mal.Type.LIST:
        newlist = list(map(lambda x: EVAL(x, env), ast.data))
        return Mal.Data(Mal.Type.LIST, newlist)
    elif ast.type == Mal.Type.VECTOR:
        newlist = list(map(lambda x: EVAL(x, env), ast.data))
        return Mal.Data(Mal.Type.VECTOR, newlist)
    elif ast.type == Mal.Type.HASH_MAP:
        newmap = []
        for i in range(0, len(ast.data), 2):
            newmap.append(ast.data[i])
            newmap.append(EVAL(ast.data[i+1], env))
        return Mal.Data(Mal.Type.HASH_MAP, newmap)
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