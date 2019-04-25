import json


c_file = open('x265.cpp.test', 'r')
c_line = c_file.readlines()
c_file.close()


cw_file = open('x265.cpp.test.w', 'w')

is_sline_comment = False
is_mline_comment = False

for line in c_line:
    line = line.strip()
    l_index = 0
    is_tm_comment = True
    while is_tm_comment:
        comment_ms = line.find('/*', l_index)
        if comment_ms >= 0:
            print('comment_ms:', comment_ms)
            l_index += comment_ms + 2
            comment_ms = l_index - 2
        comment_me = line.find('*/', l_index)
        if comment_me >= 0:
            print('comment_me:', comment_me)
            l_index += comment_me + 2
            comment_me = l_index - 2
        if comment_ms > 0:
            is_mline_comment = True

        if is_mline_comment and comment_me < 0:
            cw_file.write(line[comment_ms:] + '\n')
        elif is_mline_comment and comment_me >= 0:
            cw_file.write(line[comment_ms:comment_me] + '\n')

        if comment_me > 0 and is_mline_comment:
            is_mline_comment = False

        # 如果改行没有多行注释命令了，就退出
        if comment_ms < 0 and comment_me < 0:
            is_tm_comment = False

        print(l_index, len(line), is_tm_comment)
        if l_index >= len(line):
            break

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
