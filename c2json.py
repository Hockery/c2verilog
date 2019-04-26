import json


c_file = open('x265.cpp.test', 'r')
c_line = c_file.readlines()
c_file.close()


cw_file = open('x265.cpp.test.w', 'w')

is_sline_comment = False
is_mline_comment = False


# line: 当前行状态
# is_mc: is multipy comment continue. 是否是多行注释

def get_comment(line, is_mc):
    # mcomment = [[cs1, ce1], [cs2, ce2], ...]
    mcomment = []
    l_index = 0
    is_tm_comment = True
    while is_tm_comment:
        # 寻找 /* 多行注释开始符号
        comment_ms = line.find('/*', l_index)
        if comment_ms >= 0:
            # print('comment_ms:', comment_ms)
            l_index += comment_ms + 2
            comment_ms = l_index - 2

        # 寻找 */ 多行注释结束符号
        comment_me = line.find('*/', l_index)
        if comment_me >= 0:
            # print('comment_me:', comment_me)
            l_index += comment_me + 2
            comment_me = l_index - 2

        if comment_ms >= 0:
            is_mc = True

        # print(comment_me, comment_ms, is_mc, end=' ')
        # print(l_index, len(line))

        # 如果查阅长度大于了字符长度，退出
        if l_index >= len(line):
            is_tm_comment = False
            is_mc = False
            # break

        # 如果该行没有多行注释开始符号并且多行注释也没有没有在本行，就退出
        if (comment_ms < 0 and not is_mc):
            break

        # if comment_ms < 0 and comment_me < 0:
        #     mcomment_ = [0, len(line)]
        #     print('abc1')
        #     # cw_file.write(line)
        # el
        mcomment_ = []
        if comment_ms < 0 and comment_me >= 0:
            mcomment_ = [0, comment_me+2]
            # print('abc2:', mcomment_)
            # cw_file.write(line[:comment_me+2])
        elif comment_ms >= 0 and comment_me < 0:
            mcomment_ = [comment_ms, len(line)]
            # print('abc3:', mcomment_)
            # cw_file.write(line[comment_ms:])
        elif comment_ms >= 0 and comment_me >= 0:
            mcomment_ = [comment_ms, comment_me+2]
            # print('abc4:', mcomment_)
            # cw_file.write(line[comment_ms:comment_me+2])
        # cw_file.write('\n')
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
