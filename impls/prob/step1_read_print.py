import sys
import traceback

import Reader
import Printer

def prob_read(arg):
    return Reader.read_str(arg)

def prob_print(arg):
    return Printer.pr_str(arg)

def prob_eval(arg):
    return arg

def rep(arg):
    p_read = prob_read(arg)
    p_eval = prob_eval(p_read)
    p_print = prob_print(p_eval)
    print(p_print)
    
def main():
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
    main()