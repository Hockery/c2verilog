import json
from copy import deepcopy

mcomment = False

include_file = ''

code_parse = []

cur_node = []
stat = {
    'mcomment': False,
    'scomment': False,
    'str': False,
    'predef': False,
    'sline': [],  # 0:初始状态, 1:有独立式的状态， 2:有组合1， 3：有组合2 （用于各种组合状态记录）
    'code_status': 0
}


def un_sline():
    global cur_node
    global stat

    if len(stat['sline']) > 0:
        stat['sline'] = stat['sline'][:-1]
    else:
        stat['sline'] = []

    if len(stat['sline']) > 0:
        cur_node = stat['sline'][-1]
    else:
        cur_node = []

# 解析符号


def symbol_code(n):
    global cur_node
    global include_file
    is_option = True
    if (stat['scomment']) and (stat['str']) and (stat['mconment']):
        is_option = False
        pass

    if len(cur_node) > 0 and cur_node[0] == 'include' and cur_node[1]['status'] == 1 \
            and ((cur_node[1]['symbol'] == 1 and n[0] != '"') or (cur_node[1]['symbol'] == 2 and n[0] != '>')):
        cur_node[1]['node'][1] += n
        # print('include_file:', include_file)
        return ''

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
            if len(cur_node) > 0 and cur_node[0] == 'include':
                if cur_node[1]['status'] == 0:
                    cur_node[1]['symbol'] = 2  # 1 代表 ""; 2 代表 <>
                    cur_node[1]['status'] = 1
            return n[1:]
        if n[:1] == '>':
            # print(cur_node)
            if len(cur_node) > 0 and cur_node[0] == 'include':
                # print('cur_node[1][status]:', cur_node[1]['status'])
                if cur_node[1]['status'] == 1 and cur_node[1]['symbol'] == 2:
                    # cur_node[1]['node'].append(include_file)
                    # include_file = ''
                    un_sline()
            return n[1:]
        if n[:1] == '~':
            return n[1:]
        if n[:1] == '!':
            return n[1:]
        if n[:1] == '@':
            return n[1:]
        if n[:1] == '#':
            stat['predef'] = True
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
            # print(cur_node)
            if len(cur_node) > 0 and cur_node[0] == 'include':
                # print('cur_node[1][status]:', cur_node[1]['status'])
                if cur_node[1]['status'] == 0:
                    cur_node[1]['symbol'] = 1  # 1 代表 ""; 2 代表 <>
                    cur_node[1]['status'] = 1
                elif cur_node[1]['status'] == 1 and cur_node[1]['symbol'] == 1:
                    print('include:', include_file)
                    # print('cur_node[1]:', cur_node)
                    # print('cur_node[1]:', cur_node[1])
                    # cur_node[1]['node'].append(include_file)
                    # include_file = ''
                    un_sline()
                    # cur_node[1]['status'] = 2
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

# 解析符号串


def deal_symbol(symbols):
    s = deepcopy(symbols)
    # stat_ = deepcopy(stat)
    while len(s) != 0:
        s = symbol_code(s)
        # if stat_['mcomment'] != stat['mcomment']:
        #     print('mcomment:', stat['mcomment'], symbols)
        #     stat_['mcomment'] = stat['mcomment']
        # if stat_['scomment'] != stat['scomment']:
        #     print('scomment:', stat['scomment'], symbols)
        #     stat_['scomment'] = stat['scomment']
        # if stat_['str'] != stat['str']:
        #     print('str:', stat['str'], symbols)
        #     stat_['str'] = stat['str']
        # print(len(s))


def parse_code(code):
    global cur_node
    global include_file
    global code_parse
    if len(cur_node) > 0 and cur_node[0] == 'include' and cur_node[1]['status'] == 1:
        cur_node[1]['node'][1] += code
        # include_file += code
        # print('include_file:', include_file)
        return
    if stat['predef'] == True:
        if code == 'define':
            #print('predef words: ', code)
            pass
        elif code == 'ifdef':
            #print('predef words: ', code)
            pass
        elif code == 'ifndef':
            #print('predef words: ', code)
            pass
        elif code == 'if':
            #print('predef words: ', code)
            pass
        elif code == 'else':
            #print('predef words: ', code)
            pass
        elif code == 'endif':
            #print('predef words: ', code)
            pass
        elif code == 'undef':
            #print('predef words: ', code)
            pass
        elif code == 'include':
            # stat['sline'].append(['include', {'status': 0}])
            code_parse.append(['include', ''])
            stat['sline'].append(
                ['include', {'status': 0, 'node': code_parse[-1]}])
            print('stat[sline]', stat['sline'])
            cur_node = stat['sline'][-1]
            # print('cur_node:', cur_node)
            print('predef words: ', code)
        elif code == 'pragma':
            #print('predef words: ', code)
            pass
        elif code == 'include':
            #print('predef words: ', code)
            pass
        else:
            print('predef unknow: ', code)
        stat['predef'] = False
        return

    if code == 'asm':
        # print('key words: ', code)
        return
    if code == 'auto':
        # print('key words: ', code)
        return
    if code == 'bool':
        # print('key words: ', code)
        return
    if code == 'break':
        # print('key words: ', code)
        return
    if code == 'case':
        # print('key words: ', code)
        return
    if code == 'catch':
        # print('key words: ', code)
        return
    if code == 'char':
        # print('key words: ', code)
        return
    if code == 'class':
        # print('key words: ', code)
        return
    if code == 'const':
        # print('key words: ', code)
        return
    if code == 'continue':
        # print('key words: ', code)
        return
    if code == 'default':
        # print('key words: ', code)
        return
    if code == 'delete':
        # print('key words: ', code)
        return
    if code == 'do':
        # print('key words: ', code)
        return
    if code == 'double':
        # print('key words: ', code)
        return
    if code == 'dynamic_cast':
        # print('key words: ', code)
        return
    if code == 'else':
        # print('key words: ', code)
        return
    if code == 'enum':
        # print('key words: ', code)
        return
    if code == 'explicit':
        # print('key words: ', code)
        return
    if code == 'export':
        # print('key words: ', code)
        return
    if code == 'extern':
        # print('key words: ', code)
        return
    if code == 'false':
        # print('key words: ', code)
        return
    if code == 'float':
        # print('key words: ', code)
        return
    if code == 'for':
        # print('key words: ', code)
        return
    if code == 'friend':
        # print('key words: ', code)
        return
    if code == 'goto':
        # print('key words: ', code)
        return
    if code == 'if':
        # print('key words: ', code)
        return
    if code == 'inline':
        # print('key words: ', code)
        return
    if code == 'int':
        # print('key words: ', code)
        return
    if code == 'long':
        # print('key words: ', code)
        return
    if code == 'mutable':
        # print('key words: ', code)
        return
    if code == 'namespace':
        # print('key words: ', code)
        return
    if code == 'new':
        # print('key words: ', code)
        return
    if code == 'operator':
        # print('key words: ', code)
        return
    if code == 'private':
        # print('key words: ', code)
        return
    if code == 'protected':
        # print('key words: ', code)
        return
    if code == 'public':
        # print('key words: ', code)
        return
    if code == 'register':
        # print('key words: ', code)
        return
    if code == 'reinterpret_cast':
        # print('key words: ', code)
        return
    if code == 'return':
        # print('key words: ', code)
        return
    if code == 'short':
        # print('key words: ', code)
        return
    if code == 'signed':
        # print('key words: ', code)
        return
    if code == 'sizeof':
        # print('key words: ', code)
        return
    if code == 'static':
        # print('key words: ', code)
        return
    if code == 'static_cast':
        # print('key words: ', code)
        return
    if code == 'struct':
        # print('key words: ', code)
        return
    if code == 'switch':
        # print('key words: ', code)
        return
    if code == 'template':
        # print('key words: ', code)
        return
    if code == 'this':
        # print('key words: ', code)
        return
    if code == 'throw':
        # print('key words: ', code)
        return
    if code == 'true':
        # print('key words: ', code)
        return
    if code == 'try':
        # print('key words: ', code)
        return
    if code == 'typedef':
        # print('key words: ', code)
        return
    if code == 'typeid':
        # print('key words: ', code)
        return
    if code == 'typename':
        # print('key words: ', code)
        return
    if code == 'union':
        # print('key words: ', code)
        return
    if code == 'unsigned':
        # print('key words: ', code)
        return
    if code == 'using':
        # print('key words: ', code)
        return
    if code == 'virtual':
        # print('key words: ', code)
        return
    if code == 'void':
        # print('key words: ', code)
        return
    if code == 'volatile':
        # print('key words: ', code)
        return
    if code == 'wchar_t':
        # print('key words: ', code)
        return
    # print('other:', code)


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

    print(code_parse)


if __name__ == "__main__":

    c_file = open('x265.cpp.test', 'r')
    c_line = c_file.read()
    c_file.close()

    splite_code(c_line)
