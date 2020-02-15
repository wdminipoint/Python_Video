'''
1. 列表    [,]      切片操作
'''


# l = ['zhang', '1', 2, 3, 4, 5]
#
# print(l[3:])

'''
tumple  (1,2,3) 切片  不能改变值
'''

# t = (1,2,3,'H')
#
# print(t)

'''
{}  集合是无序的， 元素是去重的
'''

# s = {1, 'a', 'b', 'B', 'D', 'A','A'}
#
# print(s)
#
# for item in s:
#     print(item)

'''
{} 一个键 和 值   
'''

d = {'数学': 90, "语文": 80, '英语': 50}

# print(d['数学'])

# for k in d.keys():
#     print(k)
#
# for v in d.values():
#     print(v)

for item in d.items():
    print(item)

