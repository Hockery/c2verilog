import json


c_file = open('x265.cpp.test', 'r')
c_line = c_file.readlines()
c_file.close()


cw_file = open('x265.cpp.test.w', 'w')

is_sline_comment = False
is_mline_comment = False


############################################################
# @Function:
#      get_comment  -- hocker(20190426)
# @Parameter：
#      line: 当前行状态
#      s_mc: is multipy comment continue. 是否是多行注释
#
# @Return:
#       ([[cs1, ce1], [cs2, ce2], ...], is_ms)
############################################################


def get_comment(line, is_mc):
    mcomment = []
    l_index = 0
    is_tm_comment = True
    while is_tm_comment:
        # 寻找 /* 多行注释开始符号
        comment_ms = line.find('/*', l_index)
        if comment_ms >= 0:
            l_index = comment_ms + 2
            comment_ms = l_index - 2

        # 寻找 */ 多行注释结束符号
        comment_me = line.find('*/', l_index)
        if comment_me >= 0:
            l_index = comment_me + 2
            comment_me = l_index - 2

        d_quot = line.find('"', l_index)

        if comment_ms < d_quot:
            pass

        if comment_ms >= 0:
            is_mc = True

        # 如果该行没有多行注释开始符号并且多行注释也没有没有在本行，就退出
        if comment_ms < 0 and not is_mc:
            break

        mcomment_ = []
        if comment_ms < 0 and comment_me < 0 and l_index == 0:
            mcomment_ = [0, len(line)]
        elif comment_ms < 0 and comment_me >= 0:
            mcomment_ = [0, comment_me+2]
        elif comment_ms >= 0 and comment_me < 0:
            mcomment_ = [comment_ms, len(line)]
        elif comment_ms >= 0 and comment_me >= 0:
            mcomment_ = [comment_ms, comment_me+2]
        if mcomment_ != []:
            mcomment.append(mcomment_)
        if comment_me >= 0 and is_mc:
            is_mc = False

        # 如果查阅长度大于了字符长度，退出
        if l_index >= len(line):
            break
        # 如果改行没有多行注释符号了，说明该行已经分析完成， 就退出
        if comment_ms < 0 and comment_me < 0:
            break
    return (mcomment, is_mc)


single_line = ['else', '{', '}']
parentheses_line = ['if', 'while', 'switch', 'for']

# 将字符串做分析


def find_str(line, str_start):
    strs = []
    str_end = True
    # 寻找转译符号 \

    return (strs, str_end)


def is_line_end(line, is_start):
    return is_start


def get_word(line):
    # 字符串不分割，作为一个串返回

    # 变量的值都进行分割为单元进行返回
    pass


c_lines = ''
is_mc = False
for line in c_line:
    line = line.strip()
    mcomments, is_mc = get_comment(line, is_mc)

    # 去掉 '/**/' 样式的多行注释
    l_remaind = ''
    if len(mcomments) > 0:
        l_remaind += line[0:mcomments[0][0]]
        for c_i in range(len(mcomments) - 1):
            l_remaind += line[mcomments[c_i][1]: mcomments[c_i + 1][0]]
        l_remaind += line[mcomments[len(mcomments) - 1][1]:]
    else:
        l_remaind = line

    # 去掉 '//' 样式的单行注释
    comment_s = l_remaind.find('//')
    if comment_s > 0:
        l_index = comment_s + 2
    else:
        comment_s = len(l_remaind)
    l_remaind = l_remaind[:comment_s]
    if len(l_remaind) == 0:
        continue

    cw_file.write(l_remaind + '\n')
    if is_line_end(l_remaind):
        c_lines += ' ' + l_remaind
        get_word(c_lines)
    else:
        c_lines += ' ' + l_remaind

    # 将多行代码转换为单行代码

    # l_remaind 是纯代码， 下面对代码进行解析
    print(l_remaind.split())


cw_file.close()
