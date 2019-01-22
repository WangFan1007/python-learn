import requests
from bs4 import BeautifulSoup




response = requests.get('http://cd.ganji.com/zpjigongyibangongren/')
besoup = BeautifulSoup(response.text,'html.parser')
div = besoup.find('div',{"data-widget":"app/ms_v2/wanted/list.js#companyAjaxBid"})
# print(div)
ret = div.find_all('dl')

# print(ret)
for dl in ret:
    dt = dl.find('dt')
    print(dt.text)

    a = dt.find('a')
    href = a.attrs.get('href')
    print(href)


img = requests.get('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1548148640997&di=bca9afc3845a8023741265fabcdbd74f&imgtype=0&src=http%3A%2F%2Fs9.rr.itc.cn%2Fr%2FwapChange%2F20165_24_13%2Fa1lcda0105167206362.jpg')
with open('/Users/ffine/Desktop/temp/Excalibur.jpg','wb') as file:
    file.write(img.content)