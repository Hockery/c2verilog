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
            print("l_index[%d][%d]: [%s] -comment start!" %
                  (l_index, comment_ms, line[l_index:]))
            l_index = comment_ms + 2
            comment_ms = l_index - 2

        # 寻找 */ 多行注释结束符号
        comment_me = line.find('*/', l_index)
        if comment_me >= 0:
            l_index = comment_me + 2
            comment_me = l_index - 2

        if comment_ms >= 0:
            is_mc = True

        # 如果查阅长度大于了字符长度，退出
        if l_index >= len(line):
            is_tm_comment = False
            is_mc = False
            # break

        # 如果该行没有多行注释开始符号并且多行注释也没有没有在本行，就退出
        if (comment_ms < 0 and not is_mc):
            break

        mcomment_ = []
        if comment_ms < 0 and comment_me >= 0:
            mcomment_ = [0, comment_me+2]
        elif comment_ms >= 0 and comment_me < 0:
            mcomment_ = [comment_ms, len(line)]
        elif comment_ms >= 0 and comment_me >= 0:
            mcomment_ = [comment_ms, comment_me+2]
        if mcomment_ != []:
            mcomment.append(mcomment_)
        if comment_me >= 0 and is_mc:
            is_mc = False

        # 如果改行没有多行注释符号了，说明该行已经分析完成， 就退出
        if comment_ms < 0 and comment_me < 0:
            break
    return (mcomment, is_mc)


for line in c_line:
    line = line.strip()
    is_mc = False
    mcomments, is_mc = get_comment(line, is_mc)
    # if len(mcomments) > 0:
    #     print(mcomments)

    for c_i in mcomments:
        print('\t' + line[c_i[0]: c_i[1]], end='')
    if len(mcomments) > 0:
        print(mcomments)

    # comment_s = line.find('//', l_index)
    # if comment_s > 0:
    #     l_index += comment_s + 2
    #     cw_file.write(line[comment_s:])

    # elif is_mline_comment:
    #     cw_file.write(line)

    if is_sline_comment or is_mline_comment:
        cw_file.write('\n')
    # cw_file.write(line+'\n')


cw_file.close()
