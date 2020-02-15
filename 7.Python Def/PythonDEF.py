'''
函数的应用
成绩的例子：
60-70 是及格
71-80 是良
81-100 优
59 以下的是 要努力了
'''

# score = float(input('请您输入数值'))

def score_Class(score):

    if score >= 60 and score < 70:
        print(f'{score}分->及格')
    elif score >= 70 and score < 80:
        print(f'{score}分->良')
    elif score >= 80 and score < 100:
        print(f'{score}分->优')
    else:
        print(f'{score}分->你不及格，请努力吧！')


# 如果看到下面的代码，你要知道
if __name__ == '__main__':

    l_score = [45, 60, 88, 92, 55, 71]

    for score in l_score:

        score_Class(score)





