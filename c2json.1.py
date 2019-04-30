import json
from copy import deepcopy

mcomment = False

stat = {
    'mcomment': False,
    'scomment': False,
    'str': False,
    'sline': [],  # 0:初始状态, 1:有独立式的状态， 2:有组合1， 3：有组合2 （用于各种组合状态记录）
    'code_status': 0
}

# 解析符号


def symbol_code(n):
    if len(n) == 0:
        return ''

    if len(n) >= 2:
        if stat['scomment'] != True and stat['str'] != True:
            if n[:2] == '/*':
                stat['mcomment'] = True
            if n[:2] == '*/':
                stat['mcomment'] = False

    if len(n) >= 3:
        if n[:3] == '>>=':
            return n[3:]
        if n[:3] == '<<=':
            return n[3:]
    if len(n) >= 2:
        if n[:2] == '+=':
            return n[2:]
        if n[:2] == '-=':
            return n[2:]
        if n[:2] == '*=':
            return n[2:]
        if n[:2] == '/=':
            return n[2:]
        if n[:2] == '%=':
            return n[2:]

        if n[:2] == '>=':
            return n[2:]
        if n[:2] == '<=':
            return n[2:]
        if n[:2] == '==':
            return n[2:]

        if n[:2] == '->':
            return n[2:]
        if n[:2] == '++':
            return n[2:]
        if n[:2] == '--':
            return n[2:]
        if n[:1] == '//':
            stat['scomment'] = True
            return n[1:]

        if n[:2] == '&&':
            return n[2:]
        if n[:2] == '||':
            return n[2:]
        if n[:2] == '::':
            return n[2:]
        if n[:2] == '->':
            return n[2:]

    if len(n) >= 1:
        if n[:1] == '=':
            return n[1:]
        if n[:1] == '<':
            return n[1:]
        if n[:1] == '>':
            return n[1:]
        if n[:1] == '~':
            return n[1:]
        if n[:1] == '!':
            return n[1:]
        if n[:1] == '@':
            return n[1:]
        if n[:1] == '#':
            return n[1:]
        if n[:1] == '$':
            return n[1:]
        if n[:1] == '%':
            return n[1:]
        if n[:1] == '^':
            return n[1:]
        if n[:1] == '&':
            return n[1:]
        if n[:1] == '*':
            return n[1:]
        if n[:1] == '(':
            return n[1:]
        if n[:1] == ')':
            return n[1:]
        if n[:1] == '{':
            return n[1:]
        if n[:1] == '}':
            return n[1:]
        if n[:1] == '_':
            return n[1:]
        if n[:1] == '+':
            return n[1:]
        if n[:1] == '-':
            return n[1:]
        if n[:1] == '*':
            return n[1:]
        if n[:1] == '/':
            return n[1:]
        if n[:1] == ',':
            return n[1:]
        if n[:1] == '.':
            return n[1:]
        if n[:1] == '?':
            return n[1:]
        if n[:1] == ';':
            return n[1:]
        if n[:1] == ':':
            return n[1:]
        if n[:1] == '"':
            if stat['scomment'] != True and stat['mcomment'] != True:
                stat['str'] = not stat['str']
            return n[1:]
        if n[:1] == '\'':
            return n[1:]
        if n[:1] == '|':
            return n[1:]
        if n[:1] == '\\':
            return n[1:]
        if n[:1] == '[':
            return n[1:]
        if n[:1] == ']':
            return n[1:]
    print(n)

# 解决符号串


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


def parse_code(code):
    if code == 'asm':
        print('key words:', code)
        pass
    if code == 'auto':
        print('key words:', code)
        pass
    if code == 'bool':
        print('key words:', code)
        pass
    if code == 'break':
        print('key words:', code)
        pass
    if code == 'case':
        print('key words:', code)
        pass
    if code == 'catch':
        print('key words:', code)
        pass
    if code == 'char':
        print('key words:', code)
        pass
    if code == 'class':
        print('key words:', code)
        pass
    if code == 'const':
        print('key words:', code)
        pass
    if code == 'continue':
        print('key words:', code)
        pass
    if code == 'default':
        print('key words:', code)
        pass
    if code == 'delete':
        print('key words:', code)
        pass
    if code == 'do':
        print('key words:', code)
        pass
    if code == 'double':
        print('key words:', code)
        pass
    if code == 'dynamic_cast':
        print('key words:', code)
        pass
    if code == 'else':
        print('key words:', code)
        pass
    if code == 'enum':
        print('key words:', code)
        pass
    if code == 'explicit':
        print('key words:', code)
        pass
    if code == 'export':
        print('key words:', code)
        pass
    if code == 'extern':
        print('key words:', code)
        pass
    if code == 'false':
        print('key words:', code)
        pass
    if code == 'float':
        print('key words:', code)
        pass
    if code == 'for':
        print('key words:', code)
        pass
    if code == 'friend':
        print('key words:', code)
        pass
    if code == 'goto':
        print('key words:', code)
        pass
    if code == 'if':
        print('key words:', code)
        pass
    if code == 'inline':
        print('key words:', code)
        pass
    if code == 'int':
        print('key words:', code)
        pass
    if code == 'long':
        print('key words:', code)
        pass
    if code == 'mutable':
        print('key words:', code)
        pass
    if code == 'namespace':
        print('key words:', code)
        pass
    if code == 'new':
        print('key words:', code)
        pass
    if code == 'operator':
        print('key words:', code)
        pass
    if code == 'private':
        print('key words:', code)
        pass
    if code == 'protected':
        print('key words:', code)
        pass
    if code == 'public':
        print('key words:', code)
        pass
    if code == 'register':
        print('key words:', code)
        pass
    if code == 'reinterpret_cast':
        print('key words:', code)
        pass
    if code == 'return':
        print('key words:', code)
        pass
    if code == 'short':
        print('key words:', code)
        pass
    if code == 'signed':
        print('key words:', code)
        pass
    if code == 'sizeof':
        print('key words:', code)
        pass
    if code == 'static':
        print('key words:', code)
        pass
    if code == 'static_cast':
        print('key words:', code)
        pass
    if code == 'struct':
        print('key words:', code)
        pass
    if code == 'switch':
        print('key words:', code)
        pass
    if code == 'template':
        print('key words:', code)
        pass
    if code == 'this':
        print('key words:', code)
        pass
    if code == 'throw':
        print('key words:', code)
        pass
    if code == 'true':
        print('key words:', code)
        pass
    if code == 'try':
        print('key words:', code)
        pass
    if code == 'typedef':
        print('key words:', code)
        pass
    if code == 'typeid':
        print('key words:', code)
        pass
    if code == 'typename':
        print('key words:', code)
        pass
    if code == 'union':
        print('key words:', code)
        pass
    if code == 'unsigned':
        print('key words:', code)
        pass
    if code == 'using':
        print('key words:', code)
        pass
    if code == 'virtual':
        print('key words:', code)
        pass
    if code == 'void':
        print('key words:', code)
        pass
    if code == 'volatile':
        print('key words:', code)
        pass
    if code == 'wchar_t':
        print('key words:', code)
        pass
    print('other:', code)


def deal_code(codes):
    parse_code(codes)


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
                deal_code(word)
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


if __name__ == "__main__":

    c_file = open('x265.cpp.test', 'r')
    c_line = c_file.read()
    c_file.close()

    splite_code(c_line)
