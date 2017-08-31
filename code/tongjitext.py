# --encodeing:utf-8 --
# author:denny chen
# date:2017.08.29
# remark:
# 共出现了多少个不同的汉字；
# 每个汉字出现了多少次；
# 出现得最频繁的汉字有哪些。

import sys


fr = open(r'C:\python\demo\MLSZ\data\tongjitext.txt', 'r',encoding='UTF-8')

characters = []
stat = {}

for line in fr.read():
	#print('line:',line)
	# 去掉每一行两边的空白
	line = line.strip()
	# 如果为空行则跳过该轮循环
	if len(line) == 0:
		continue
	# 将文本转为unicode，便于处理汉字
	#line = unicode(line)
	# 遍历该行的每一个字
	for x in range(0, len(line)):
		#print('x:',line[x])
		# 去掉标点符号和空白符
		if line[x] in [' ', '\t', '\n', '。', '，', '(', ')', '（', '）', '：', '□', '？', '！', '《', '》', '、', '；', '“', '”', '……']:
			continue
		# 尚未记录在characters中
		if not line[x] in characters:
			characters.append(line[x])
		# 尚未记录在stat中
		if line[x] not in stat:
			stat[line[x]] = 0
		# 汉字出现次数加1
		stat[line[x]] += 1
		#print('char:',characters)
		#print('stat:',stat)
# print('char:',characters)
# print('*'*20)
# print('stat:',stat)

# lambda生成一个临时函数,dict sort,get list
# d表示字典的每一对键值对，d[0]为key，d[1]为value
# reverse为True表示降序排序
print('items:',stat.items())
stat = sorted(stat.items(), key=lambda d:d[1], reverse=True)
print('items:',stat)
#list sort,get list
# student_tuples = [
 #         ('john', 'A', 15),
 #         ('jane', 'B', 12),
 #         ('dave', 'B', 10),
 # ]
#sorted(listex,key=lambda listex:listex[2])
#str sort,get list
#sorted('this is a test string sort'.split,key=str.lower())

fw = open(r'C:\python\demo\MLSZ\data\tongjitext_result.txt', 'w',encoding='UTF-8')
for item in stat:
	# 进行字符串拼接之前，需要将int转为str
	fw.write(item[0] + ',' + str(item[1]) + '\n')
	#print(item[0],item[1])

fr.close()
fw.close()

