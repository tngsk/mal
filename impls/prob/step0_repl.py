import sys

def READ(arg):
    return arg

def PRINT(arg):
    return arg

def EVAL(arg):
    return arg

def rep(arg):
    r = READ(arg)
    e = EVAL(r)
    p = PRINT(e)
    print(p)
    
def LOOP():
    while True:
        print('user> ', end='')
        line = input()
        if line:
            rep(line)
        else:
            sys.exit(0)

if __name__ == "__main__":
    LOOP()