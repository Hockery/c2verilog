import json
from copy import deepcopy

mcomment = False

stat = {
    'mcomment': False,
    'scomment': False,
    'str': False
}
# 解析符号


def symbol_code(n):
    if len(n) == 0:
        return ''

    if len(n) >= 2:
        # print('n[:2] == \'/*\'', n)
        if stat['scomment'] != True and stat['str'] != True:
            if n[:2] == '/*':
                stat['mcomment'] = True
            if n[:2] == '*/':
                stat['mcomment'] = False
        # return n[2:]

    if len(n) >= 3:
        if n[:3] == '>>=':
            pass
            return n[3:]
        if n[:3] == '<<=':
            pass
            return n[3:]
    if len(n) >= 2:
        if n[:2] == '+=':
            pass
            return n[2:]
        if n[:2] == '-=':
            pass
            return n[2:]
        if n[:2] == '*=':
            pass
            return n[2:]
        if n[:2] == '/=':
            pass
            return n[2:]
        if n[:2] == '%=':
            pass
            return n[2:]

        if n[:2] == '>=':
            pass
            return n[2:]
        if n[:2] == '<=':
            pass
            return n[2:]
        if n[:2] == '==':
            pass
            return n[2:]

        if n[:2] == '->':
            pass
            return n[2:]
        if n[:2] == '++':
            pass
            return n[2:]
        if n[:2] == '--':
            pass
            return n[2:]
        if n[:1] == '//':
            stat['scomment'] = True
            return n[1:]

        if n[:2] == '&&':
            pass
            return n[2:]
        if n[:2] == '||':
            pass
            return n[2:]

    if len(n) >= 1:
        if n[:1] == '=':
            pass
            return n[1:]
        if n[:1] == '<':
            pass
            return n[1:]
        if n[:1] == '>':
            pass
            return n[1:]
        if n[:1] == '~':
            pass
            return n[1:]
        if n[:1] == '!':
            pass
            return n[1:]
        if n[:1] == '@':
            pass
            return n[1:]
        if n[:1] == '#':
            pass
            return n[1:]
        if n[:1] == '$':
            pass
            return n[1:]
        if n[:1] == '%':
            pass
            return n[1:]
        if n[:1] == '6':
            pass
            return n[1:]
        if n[:1] == '&':
            pass
            return n[1:]
        if n[:1] == '*':
            pass
            return n[1:]
        if n[:1] == '(':
            pass
            return n[1:]
        if n[:1] == ')':
            pass
            return n[1:]
        if n[:1] == '{':
            pass
            return n[1:]
        if n[:1] == '}':
            pass
            return n[1:]
        if n[:1] == '_':
            pass
            return n[1:]
        if n[:1] == '+':
            pass
            return n[1:]
        if n[:1] == '-':
            pass
            return n[1:]
        if n[:1] == '*':
            pass
            return n[1:]
        if n[:1] == '/':
            pass
            return n[1:]
        if n[:1] == ',':
            pass
            return n[1:]
        if n[:1] == '.':
            pass
            return n[1:]
        if n[:1] == '?':
            pass
            return n[1:]
        if n[:1] == ';':
            pass
            return n[1:]
        if n[:1] == ':':
            pass
            return n[1:]
        if n[:1] == '"':
            if stat['scomment'] != True and stat['mcomment'] != True:
                stat['str'] = not stat['str']
            pass
            return n[1:]
        if n[:1] == '\'':
            pass
            return n[1:]
        if n[:1] == '|':
            pass
            return n[1:]
        if n[:1] == '\\':
            pass
            return n[1:]
        if n[:1] == '[':
            pass
            return n[1:]
        if n[:1] == ']':
            pass
            return n[1:]
    print(n)


def deal_symbol(symbols):
    s = deepcopy(symbols)
    stat_ = deepcopy(stat)
    while len(s) != 0:
        s = symbol_code(s)
        if stat_['mcomment'] != stat['mcomment']:
            print('mcomment:', stat['mcomment'], symbols)
            stat_['mcomment'] = stat['mcomment']
        if stat_['scomment'] != stat['scomment']:
            print('scomment:', stat['scomment'], symbols)
            stat_['scomment'] = stat['scomment']
        if stat_['str'] != stat['str']:
            print('str:', stat['str'], symbols)
            stat_['str'] = stat['str']
        # print(len(s))


def is_word_connect(char_):
    c = ord(char_)
    if (c >= 48 and c <= 57) or (c >= 65 and c <= 90) or (c >= 97 and c <= 122) or (c == 95):
        return True
    else:
        return False


def splite_code(code):
    word = ''
    symbol = ''
    for i in code:
        if is_word_connect(i):
            word += i
            if len(symbol) != 0:
                # print(symbol)
                deal_symbol(symbol)
            symbol = ''
        else:
            if len(word) > 0:
                # print(word)
                pass
            word = ''
            if i == ' ' or i == '\n' or i == '\t':
                if i == '\n':
                    stat['scomment'] = False
                if len(symbol) != 0:
                    # print(symbol)
                    deal_symbol(symbol)
                symbol = ''
            else:
                symbol += i
    pass


if __name__ == "__main__":

    c_file = open('x265.cpp.test', 'r')
    c_line = c_file.read()
    c_file.close()

    splite_code(c_line)

#   Lh@2019!Cloud@0409
