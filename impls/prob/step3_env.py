import sys
import traceback

import Reader
import Printer
import Mal
import Env

# repl_env = {'+': lambda a,b: a + b,
#             '-': lambda a,b: a - b,
#             '*': lambda a,b: a * b,
#             '/': lambda a,b: int(a/b)}

repl_env = Env.Env()
repl_env.set('+', lambda a,b: a + b)
repl_env.set('-', lambda a,b: a - b)
repl_env.set('*', lambda a,b: a * b)
repl_env.set('/', lambda a,b: int(a/b))

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
        first_symbol = ast.data[0].data
        if first_symbol == 'def!':
            key = ast.data[1].data
            value = EVAL(ast.data[2], env)
            env.set(key, value)
            return value
        elif first_symbol == 'let*':
            let_env = Env.Env(env)
            e1 = ast.data[1].data
            e2 = ast.data[2]
            for i in range(0, len(e1), 2):
                let_env.set(e1[i].data , EVAL(e1[i+1], let_env))
            return EVAL(e2, let_env)

        else:
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
            return env.get(ast.data)
        except:
            raise Exception(f"{ast.data} not found")
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