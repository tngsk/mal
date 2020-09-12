import sys

def prob_read(arg):
    return arg

def prob_print(arg):
    return arg

def prob_eval(arg):
    return arg

def rep(arg):
    p_read = prob_read(arg)
    p_eval = prob_eval(p_read)
    p_print = prob_print(p_eval)
    print(p_print)
    
def main():
    while True:
        print('user> ', end='')
        line = input()
        if line:
            rep(line)
        else:
            sys.exit(0)
if __name__ == "__main__":
    main()