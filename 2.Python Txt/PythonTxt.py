f = open('./pythontxt.txt', mode='a', encoding='utf-8')

for i in range(1, 11, 1):
    f.write(str(i))
    f.write('\n')


f_r = open('./pythontxt.txt', mode='r', encoding='utf-8')

print(f_r.readline())

for item in f_r.readlines():

    print(item.strip())

