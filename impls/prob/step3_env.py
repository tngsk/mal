import sys
import Reader
import Printer
import Mal
import Env

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
    if not type(ast) is list:
        return eval_ast(ast, env)

    elif len(ast) == 0:
        return ast

    elif type(ast) is list:
        first_symbol = ast[0]

        if first_symbol == 'def!':
            key = ast[1]
            value = EVAL(ast[2], env)
            env.set(key, value)
            return value

        elif first_symbol == 'let*':
            let_env = Env.Env(env)
            e1 = ast[1]
            e2 = ast[2]
            for i in range(0, len(e1), 2):
                let_env.set(e1[i] , EVAL(e1[i+1], let_env))
            return EVAL(e2, let_env)

        else:
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
            return env.get(ast)
        except:
            raise Exception(f"{ast} not found")

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