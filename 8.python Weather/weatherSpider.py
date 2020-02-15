import requests
from bs4 import BeautifulSoup

# csv
def spider (month):
    #方法里面的内容一定要要缩进一下

    f = open('./weather.csv',mode='a',encoding='utf-8')

    r = requests.get(f'http://www.tianqihoubao.com/lishi/beijing/month/2019{month}.html')

    print(r.status_code) # 200 说明就成功的  否则都是失败的

    soup = BeautifulSoup(r.text,'html.parser')

    trs = soup.find_all('tr')[1:]

    for tr in trs:

        tds = tr.find_all('td')

        for td in tds:
            f.write(strFormate(td.text)+',')
            print(strFormate(td.text))
        f.write('\n')


def strFormate(str):

    splitValue = str.split('/')

    if len(splitValue) == 1:

        return str.strip()

    else:
        return f'{splitValue[0].strip()}/{splitValue[1].strip()}'


if __name__ == '__main__':

    for i in range(1,13,1):
        if i<10:
            spider(f'0{i}')
        else:
            spider(str(i))







