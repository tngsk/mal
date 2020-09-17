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

def read_atom(reader):
    token = reader.next()
    int_type = re.compile(r"-?[0-9]+$")
    str_type = re.compile(r'"(?:[\\].|[^\\"])*"')
    if re.match(int_type, token):
        return Mal.Type.NUMBER, token
    elif re.match(str_type, token):
        #token = token[1:-1]#.replace(r"/\\(.)/g", lambda x:x)
        return Mal.Type.STR, token
    elif token[0] == '"':
        raise Exception('EOF')
    elif token[0] == ':':
        # token = "\u029e" + token[1:]
        # token = token[1:]
        return Mal.Type.KEYWORD, token
    elif token == 'nil':
        return Mal.Type.NIL, 'nil'
    elif token == 'true':
        return Mal.Type.TRUE, 'true'
    elif token == 'false':
        return Mal.Type.FALSE, 'false'
    else:
        return Mal.Type.STR, token

def read_form(reader):
    token = reader.peek()
    if token == '\'':
        reader.next()
        symbol = Mal.Data(Mal.Type.SYMBOL,'quote')
        return Mal.Data(Mal.Type.LIST, list([symbol, read_form(reader)]))
    elif token == '`':
        reader.next()
        symbol = Mal.Data(Mal.Type.SYMBOL,'quasiquote')
        return Mal.Data(Mal.Type.LIST, list([symbol, read_form(reader)]))
    elif token == '~':
        reader.next()
        symbol = Mal.Data(Mal.Type.SYMBOL,'unquote')
        return Mal.Data(Mal.Type.LIST, list([symbol, read_form(reader)]))
    elif token == '~@':
        reader.next()
        symbol = Mal.Data(Mal.Type.SYMBOL,'splice-unquote')
        return Mal.Data(Mal.Type.LIST, list([symbol, read_form(reader)]))
    elif token == '^':
        reader.next()
        symbol = Mal.Data(Mal.Type.SYMBOL,'with-meta')
        return Mal.Data(Mal.Type.LIST, list([symbol, read_form(reader)]))
    elif token == '@':
        reader.next()
        symbol = Mal.Data(Mal.Type.SYMBOL,'deref')
        return Mal.Data(Mal.Type.LIST, list([symbol, read_form(reader)]))

    # list
    elif token == ')': raise Exception('unexpected ")"')
    elif token == '(':
        return Mal.Data(Mal.Type.LIST, read_list(reader))

    # vector
    elif token == ']': raise Exception('unexpected "]"')
    elif token == '[':
        return Mal.Data(Mal.Type.LIST, read_list(reader))

    # hash-map
    elif token == '{': raise Exception('unexpected "}"')
    elif token == '}':
        return Mal.Data(Mal.Type.LIST, read_list(reader))

    # atom
    else:
        type, data = read_atom(reader)
        return Mal.Data(type, data)


def read_str(str):
    tokens = tokenize(str)
    return read_form(Reader(tokens))
