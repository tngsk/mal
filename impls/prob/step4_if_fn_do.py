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

    if len(ast) == 0:
        return ast

    if type(ast) is list:

        a0, a1, a2, a3, _ = ast

        if a0 == 'def!':
            value = EVAL(a2, env)
            env.set(a1, value)
            return value

        elif a0 == 'let*':
            let_env = Env.Env(env)
            for i in range(0, len(a1), 2):
                let_env.set(a1[i] , EVAL(a1[i+1], let_env))
            return EVAL(a2, let_env)
        
        elif a0 == 'do':
            return eval_ast(ast[1:], env)
        
        elif a0 == 'if':
            if1 = EVAL(a1, env)
            if not (type(if1) is Mal.Nil or type(if1) is Mal.Fal):
                return EVAL(a2, env)
            else:
                if3 = EVAL(a3, env)
                return if3 if if3 else Mal.Nil()
        
        elif a0 == 'fn*':
            def fn(*args):
                fn_env = Env.Env(env, a1, args)
                return EVAL(a2, fn_env)
            return Mal.Fn(fn)

        else:
            fn = eval_ast(ast, env)
            return eval_function(fn)

    else:
        raise Exception("EVAL: Type Error")
 
def eval_function(el):
    fn = el[0]
    args = []
    for arg in el[1:]:
        if type(arg) is Mal.Number:
            args.append(int(arg))
        else:
            args.append(arg)
    return fn(*args)

def eval_ast(ast, env):
    
    if type(ast) is Mal.Symbol:
        try:
            return env.get(ast)
        except:
            raise Exception(f" {ast} not found")

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