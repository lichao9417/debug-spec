import collections
import sys
import os
import re
#读入文件路径，去除特殊字符，用空格分开，返回strr字符串
def openfile(file_path):
	s = '.txt'
	if s not in file_path:
		file_path = file_path + s
	with open(file_path,'r',encoding="utf-8") as file:
		strr = file.read().lower()
	words = re.findall(r'[a-z0-9^-]+',strr)
	count(words)

def count(words):
	collect = collections.Counter(words)
	num = 0
	for i in collect:
		num += 1
	if sys.argv[1] == '-s':
		print('total ', num)
	else:
	    print('total  {} words'.format(num))
	result = collect.most_common(10)
	for j in result:
		print('%-8s%5d' % (j[0], j[1]))

def folderCount(path):
	files = os.listdir(path)
	for file in files:
		filename = os.path.splitext(file)[0]
		print(filename)
		openfile(path + '\\' +file)
		print('----')

if __name__ == '__main__':
    if sys.argv[1] == '-s':
        openfile(sys.argv[2])
    elif len(sys.argv) == 2 and os.path.isfile(sys.argv[1] + '.txt'):
    	openfile(sys.argv[1] + '.txt')
    elif len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
        os.path.isdir(sys.argv[1])
        folderCount(sys.argv[1])
    else:
        openfile(sys.argv[1])