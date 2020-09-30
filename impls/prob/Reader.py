import re
import Mal

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
        if not token:
            raise Exception('EOF')
        lst.append(read_form(reader))
        token = reader.peek()
    reader.next()
    return lst

def read_list(reader):
    return read_sequence(reader, ')')

def read_vector(reader):
    return read_sequence(reader, ']')

def read_hash_map(reader):
    return read_sequence(reader, '}')

def read_atom(reader):
    token = reader.next()
    int_regex = re.compile(r"-?[0-9]+$")
    str_regex = re.compile(r'"(?:[\\].|[^\\"])*"')
    if re.match(int_regex, token):
        return Mal.Number(token)
    elif re.match(str_regex, token):
        return str(token)
    elif token[0] == '"':
        raise Exception('EOF')
    elif token[0] == ':':
        # token = "\u029e" + token[1:]
        # token = token[1:]
        return Mal.Keyword(token)
    elif token == 'nil':
        return Mal.Nil()
    elif token == 'true':
        return Mal.Tru()

    elif token == 'false':
        return Mal.Fal()
    else:
        return Mal.Symbol(token)
    
def read_form(reader):
    token = reader.peek()
    if token == '\'':
        reader.next()
        symbol = Mal.Symbol('quote')
        return list([symbol, read_form(reader)])

    elif token == '`':
        reader.next()
        symbol = Mal.Symbol('quasiquote')
        return list([symbol, read_form(reader)])

    elif token == '~':
        reader.next()
        symbol = Mal.Symbol('unquote')
        return list([symbol, read_form(reader)])

    elif token == '~@':
        reader.next()
        symbol = Mal.Symbol('splice-unquote')
        return list([symbol, read_form(reader)])

    elif token == '^':
        reader.next()
        meta = read_form(reader)
        symbol = Mal.Symbol('with-meta')
        return list([symbol, read_form(reader), meta])

    elif token == '@':
        reader.next()
        symbol = Mal.Symbol('deref')
        return list([symbol, read_form(reader)])

    # list
    elif token == ')': raise Exception('unexpected ")"')
    elif token == '(':
        return read_list(reader)

    # vector
    elif token == ']': raise Exception('unexpected "]"')
    elif token == '[':
        vector = read_vector(reader)
        return Mal.Vector(vector)

    # hash-map
    elif token == '}': raise Exception('unexpected "}"')
    elif token == '{':
        hashmap = read_hash_map(reader)
        return Mal.HashMap(hashmap)

    # atom
    else:
        return read_atom(reader)


def read_str(str):
    tokens = tokenize(str)
    return read_form(Reader(tokens))
