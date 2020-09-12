import re

class Reader():
    def __init__(self, tokens, position=0):
        self.position = position
        self.tokens = tokens

    def next(self):
        if self.position < len(self.tokens):
            token = self.tokens[self.position]
            self.position = self.position + 1
            return token
        else:
            return None

    def peek(self):
        if self.position < len(self.tokens):
            token = self.tokens[self.position]
            return token
        else:
            return None

def tokenize(str):
    regex = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:[\\].|[^\\"])*"?|;.*|[^\s\[\]{}()'"`@,;]+)""")
    tokenized = [t for t in re.findall(regex, str) if t[0] != ";"]
    return tokenized

def read_sequence(reader, stop):
    lst = list()
    token = reader.next()
    token = reader.peek()
    while token != stop:
        lst.append(read_form(reader))
        token = reader.peek()
    reader.next()
    return lst

def read_list(reader):
    return read_sequence(reader, ')')

def read_atom(reader):
    token = reader.next()
    if token:
        int_type = re.compile(r"-?[0-9]+$")
        if re.match(int_type, token):
            return int(token)
        else:
            return str(token)

def read_form(reader):
    token = reader.peek()
    special = {'\'', '`', '~', '~@', '^', '@'}
    right_paren = {')',']','}'}
    left_paren = {'(','[','{'}
    if token in special:
        reader.next()
        return read_form(reader)
    elif token in right_paren:
        raise Exception('unexpected')
    elif token in left_paren:
        return read_list(reader) 
    else:
        return read_atom(reader)

def read_str(str):
    tokens = tokenize(str)
    return read_form(Reader(tokens))
