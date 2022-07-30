# imports
from arrows import *
# errors


class error:
    def __init__(self, pos_start, pos_end, err, dis):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.err = err
        self.dis = dis

    def form(self):
        res = f'{self.err}:{self.dis}\n'
        res += f'File {self.pos_start.fn},line:{self.pos_start.ln+1}'
        return res


class wrongchar(error):
    def __init__(self, pos_start, pos_end, dis):
        super().__init__(pos_start, pos_end, "wrong char", dis)


class invalidsyntax(error):
    def __init__(self, pos_start, pos_end, dis):
        super().__init__(pos_start, pos_end, "invalid syntax", dis)
# positions


class position:
    def __init__(self, ind, ln, col, fn, ftxt):
        self.ind = ind
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char=None):
        self.ind += 1
        self.col += 1
        if current_char == '\n':
            self.ln += 1
            self.col = 0
        return self

    def copy(self):
        return position(self.ind, self.ln, self.col, self.fn, self.ftxt)
# tokens


class tokens:
    def __init__(self, type, val=None):
        self.type = type
        self.val = val

    def __repr__(self):
        if self.val:
            return f'{self.type}:{self.val}'
        return f'{self.type}'
# lexer


class lexer:
    def __init__(self, fn, text):
        self.text = text
        self.fn = fn
        self.pos = position(-1, 0, -1, fn, text)
        self.current_char = None
        self.inc()

    def inc(self):
        self.pos.advance(self.current_char)
        if self.pos.ind < len(self.text):
            self.current_char = self.text[self.pos.ind]
        else:
            self.current_char = None

    def tokensization(self):
        token = []
        while self.current_char != None:
            if self.current_char in ' \t':
                self.inc()
            elif self.current_char in "0123456789":
                token.append(self.createnum())
            elif self.current_char == '+':
                token.append(tokens("PLUS"))
                self.inc()
            elif self.current_char == '-':
                token.append(tokens("MINUS"))
                self.inc()
            elif self.current_char == '*':
                token.append(tokens("MULTI"))
                self.inc()
            elif self.current_char == '/':
                token.append(tokens("DIVI"))
                self.inc()
            elif self.current_char == ')':
                token.append(tokens("RPAR"))
                self.inc()
            elif self.current_char == '(':
                token.append(tokens("LPAR"))
                self.inc()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.inc()
                return [], wrongchar(pos_start, self.pos, char)
        return token, None

    def createnum(self):
        num = ""
        dotcount = 0
        while((self.current_char != None) and (self.current_char in "0123456789.")):
            if(self.current_char == '.'):
                if(dotcount == 1):
                    break
                dotcount += 1
                num += '.'
            else:
                num += self.current_char
            self.inc()
        if(dotcount == 0):
            return tokens('INT', int(num))
        else:
            return tokens('FLOAT', float(num))

# nodes


class numnode:
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f'{self.tok}'


class binopnode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node},{self.op_tok},{self.right_node})'
# parser


class parser:
    def __init__(self, token):
        self.token = token
        self.ind = -1
        self.inc()

    def inc(self):
        self.ind += 1
        if(self.ind < len(self.token)):
            self.current_tok = self.token[self.ind]
        return self.current_tok

    def parse(self):
        return self.exp()

    def fact(self):
        tok = self.current_tok
        if tok.type in ('INT', 'FLOAT'):
            self.inc()
            return numnode(tok)

    def term(self):
        return self.bin_op(self.fact, ('MULTI', 'DIVI'))

    def exp(self):
        return self.bin_op(self.term, ('PLUS', 'MINUS'))

    def bin_op(self, func, ops):
        left = func()
        while self.current_tok.type in ops:
            op_tok = self.current_tok
            self.inc()
            right = func()
            left = binopnode(left, op_tok, right)
        return left

# runner


def play(fn, text):
    l = lexer(fn, text)
    token, error = l.tokensization()
    if error:
        None, error
    p = parser(token)
    ast = p.parse()
    return ast, None
