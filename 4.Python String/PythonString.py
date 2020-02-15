'''
本节课 我们讲解 string
'''

# + 首先定义连个变量 a ='A' b='B'

a = 'A'
b = 'B'

# out_1 = a + '_' + b
#
# print(out_1)

# '%s %s'  %  (a,b)

# out_2 = '这里我们输出两个字母%s 和 %s' % (a,b)
#
# print(out_2)

'''
3.format()
'''

# out_3 = '这里我们输出两个字母{}和{}'.format(a,b)
#out_3 = '这里我们输出两个字母{0}和{1}'.format(a,b)
# out_3 = '这里我们输出两个字母{str0}和{str1}'.format(str0=a,str1=b)

# print(out_3)

'''
4. f string
'''
# c='CCC'
# d="DDD"
#
# out_4 = f'这里我们输出两个字母{c} 和 {d}'  # python 3.6
#
# print(out_4)

'''
5.join
'''
lb=['中','国','加','油']

out_5 ='_'.join(lb)

print(out_5)

