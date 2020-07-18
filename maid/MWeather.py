from requests import packages, get
from bs4 import BeautifulSoup
from MConfig import *
from MError import *
from random import choice

packages.urllib3.disable_warnings()

StrWeatherToday = [
    '斋主，金天{}白天{}，气温在{}，晚上{}，气温{}。金天紫外线强度{}，空气污染指数{}，{}',
    '回斋主，{}白天{}，{}。晚上{}，{}。紫外线{}，空气污染{}，斋主，{}']


def init():
    global code, city
    city = readCity()
    if city == '皋安':
        code = 101240508
    elif city == '青倒':
        code = 101120201
    elif city == '黄倒':
        code = 101120206
    elif city == '太安':
        code = 101120801
    else:
        StrFileBroken()


def sayWeatherToday():
    init()
    url = 'http://www.weather.com.cn/weather1d/{}.shtml'.format(code)
    try:
        msg = get(url, timeout=10, stream=True, verify=False)
    except:
        sayConnectError()
        return 0
    msg.encoding = msg.apparent_encoding
    try:
        tem = BeautifulSoup(msg.text, 'html.parser').find_all('p', class_="tem")
    except:
        sayConnectError()
        return 0
    wea = BeautifulSoup(msg.text, 'html.parser').find_all('p', class_="wea")
    msg = str(BeautifulSoup(msg.text, 'html.parser').find_all('ul', class_="clearfix")).split('<span>')
    say(choice(StrWeatherToday).format(city, wea[0].text, tem[0].text.replace('\n', ''), wea[1].text,
                                     tem[1].text.replace('\n', ''), msg[10][0:msg[10].find('<')],
                                     msg[15][0:msg[15].find('<')],
                                     msg[13][msg[13].find('<p>') + 3:msg[13].find('</p>')]))


StrWeatherThreeDay = [
    '斋主，{}金天{},{}，明天{}，{}，后天{},{}',
    '回斋主，{}县金天{},{}，明天{}，{}，后天{},{}']


def sayWeatherThreeDay():
    init()
    url = 'http://www.weather.com.cn/weather/{}.shtml'.format(code)
    try:
        msg = get(url, timeout=10, stream=True, verify=False)
    except:
        sayConnectError()
        return 0
    msg.encoding = msg.apparent_encoding
    try:
        wea = BeautifulSoup(msg.text, 'html.parser').find_all('p', class_="wea")
    except:
        sayConnectError()
        return 0
    tem = BeautifulSoup(msg.text, 'html.parser').find_all('p', class_="tem")
    say(choice(StrWeatherThreeDay).format(city, wea[0].text, tem[0].text.replace('\n', '').replace('/', '到'), wea[1].text,
                                        tem[1].text.replace('\n', '').replace('/', '到'), wea[2].text,
                                        tem[2].text.replace('\n', '').replace('/', '到')))
