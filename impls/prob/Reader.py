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
        return int(token)
    elif re.match(str_type, token):
        return str(token)
    elif token[0] == '"':
        raise Exception('EOF')
    elif token[0] == ':':
        pass
    elif token == 'nil':
        return None
    elif token == 'true':
        return True
    elif token == 'false':
        return False
    else:
        return str(token)

def read_form(reader):
    token = reader.peek()
    if token:
        special = {'`', '~', '~@', '^', '@'}
        right_paren = {')',']','}'}
        left_paren = {'(','[','{'}

        if token == '\'':
            reader.next()
            return list(['quote', read_form(reader)])
        elif token == '`':
            reader.next()
            return list(['quasiquote', read_form(reader)])
        elif token == '~':
            reader.next()
            return list(['unquote', read_form(reader)])
        elif token == '~@':
            reader.next()
            return list(['splice-unquote', read_form(reader)])
        elif token == '^':
            reader.next()
            return list(['with-meta', read_form(reader)])
        elif token == '@':
            reader.next()
            return list(['deref', read_form(reader)])

        # list
        elif token == ')': raise Exception('unexpected ")"')
        elif token == '(':
            return read_list(reader)

        # vector
        elif token == ']': raise Exception('unexpected "]"')
        elif token == '[':
            return read_list(reader)

        # hash-map
        elif token == '{': raise Exception('unexpected "}"')
        elif token == '}':
            return read_list(reader)

        # atom
        else:
            return read_atom(reader)
    else:
        raise Exception('EOF')

def read_str(str):
    tokens = tokenize(str)
    return read_form(Reader(tokens))
