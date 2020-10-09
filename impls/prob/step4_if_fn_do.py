import sys
import reader
import printer
from mal import *
from env import Env
import core

repl_env = Env()
for key,value in core.ns.items():
    repl_env.set(key, value)

def READ(arg):
    return reader.read_str(arg)

def PRINT(arg):
    return printer.pr_str(arg)

def EVAL(ast, env):
    if not type(ast) is list:
        return eval_ast(ast, env)

    if len(ast) == 0:
        return ast

    if type(ast) is list:
        first = ast[0]

        if first == 'def!':
            value = EVAL(ast[2], env)
            env.set(ast[1], value)
            return value

        elif first == 'let*':
            let_env = Env(env)
            for i in range(0, len(ast[1]), 2):
                let_env.set(ast[1][i] , EVAL(ast[1][i+1], let_env))
            return EVAL(ast[2], let_env)
        
        elif first == 'do':
            elem = eval_ast(ast[1:], env)
            return elem[len(elem) - 1]
        
        elif first == 'if':
            cond = type(EVAL(ast[1], env))
            if (cond is Nil) or (cond is Fal):
                if len(ast) > 3:
                    return EVAL(ast[3], env)
                else:
                    return Nil()
            else:
                return EVAL(ast[2], env)
            
        elif first == 'fn*':
            def fn(*args):
                fn_env = Env(env, ast[1], args)
                return EVAL(ast[2], fn_env)
            return Fn(fn)

        else:
            fn = eval_ast(ast, env)
            return eval_function(fn)

    else:
        raise Exception("EVAL: Type Error")
 
def eval_function(el):
    fn = el[0]
    args = []
    for arg in el[1:]:
        if type(arg) is Number:
            args.append(int(arg))
        else:
            args.append(arg)
    return fn(*args)

def eval_ast(ast, env):
    
    if type(ast) is Symbol:
        try:
            return env.get(ast)
        except:
            raise Exception(f" {ast} not found")

    elif type(ast) is list:
        lst = list(map(lambda x: EVAL(x, env), ast))
        return lst

    elif type(ast) is Vector:
        lst = list(map(lambda x: EVAL(x, env), ast))
        return Vector(lst)

    elif type(ast) is HashMap:
        lst = []
        for i in range(0, len(ast), 2):
            lst.append(ast[i])
            lst.append(EVAL(ast[i+1], env))
        return HashMap(lst)
    else:
        return ast

def rep(arg):
    r = READ(arg)
    e = EVAL(r, repl_env)
    p = PRINT(e)
    print(p)


rep('(def! not (fn* (a) (if a false true)))')

def LOOP():
    while True:
        try:
            # print('user> ', end='')
            line = input('user> ')
            if line:
                rep(line)
            else:
                sys.exit(0)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    LOOP()