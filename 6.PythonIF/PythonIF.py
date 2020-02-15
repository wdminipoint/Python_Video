'''
通过两个例子讲解一下 IF 判断 while for 循环
'''

score = input()  # 取到外面输入的一个值

# if int(score) < 60:
#     print('不及格')
# elif int(score) <=80:
#     print('良')
# else:
#     print('优')


# if txt == '张立国':
#     print('恭喜你答对了')
# else:
#     print('不好意思，你答错了')

i = int(score)

while i < 10:

    print(i)

    if i==8:

        # break
        print('continue:'+str(i))

        continue

        i = i + 1

    i = i + 1

print('退出了')
