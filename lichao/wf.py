import re  # 导入正则模块
import sys  # 用于获取命令行参数
import os
import os.path  # 用于判断是文件还是文件夹
from collections import Counter

# 全局变量
filename = ''


def get_word_freq(str):
    words = get_file_content(str)
    word_list = Counter(words)  # [('a', 5), ('b', 2), ('r', 2)]
    total = len(word_list)  # 记录单词个数
    print("total    ", total)

    common_word_list = word_list.most_common(10)
    for common_word in common_word_list:
        print("%20s  %5d" % (common_word[0], common_word[1]))



def get_file_content(path_or_content_str):
    contents = ''
    if(os.path.isfile(path_or_content_str)):
        filename = path_or_content_str
        with open(filename, decoding='utf-8') as f_obj:
            contents = f_obj.read()  # findall(p,txt) 在txt字符串总查找所有匹配的内容，如果找到，返回字符串列表，否则None
    else: contents = path_or_content_str
    words = re.findall(r'[\w^-]+', contents)  # ['My', 'English', 'is', 'very', 'very', 'pool']
    return words


# 功能3循环调用 word_fre function
def multiple_call_word_fre(dir_str):
    file_list = os.listdir(dir_str)
    # print(file_list)
    for file in file_list:
        filename = dir_str + '/' + file
        print(file.replace(".txt", ""))
        get_word_freq(filename)


# 通过判断命令行参数来确定实现哪个功能--------------------------------INTERFACE------------------------------------------------------

if len(sys.argv) == 3 and sys.argv[1] == "-s":  # 功能1接口
    filename = sys.argv[2]
    get_word_freq(filename)
elif len(sys.argv) == 2 and os.path.isfile(sys.argv[1] + '.txt'):  # 功能2
    get_word_freq(filename)
# 是否为功能3接口
elif len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
    multiple_call_word_fre(sys.argv[1])
# 功能4
elif len(sys.argv) == 2:  # 功能4情况1     command < file 	将输入重定向到 file。
    file_str = input().replace('\n',' ')

    get_word_freq(file_str)
elif len(sys.argv) == 1:   #功能4情况2
    data = ""
    for line in sys.stdin:
        if line != "\n":#停止条件
            data += line
        else:
            break
    get_word_freq(data)
#elif len(sys.argv)==4:   #功能5  规定命令行参数格式：wf test.txt m n     其中m为几个字母 n为top多少
# file_str = input().
# print(file_str)
# get_word_freq(file_str)