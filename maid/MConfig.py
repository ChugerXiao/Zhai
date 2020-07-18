from speech import input as input_
from MError import *


def readCity():
    try:
        with open('config', 'r', encoding='utf-8') as f:
            city = f.readlines()[1].replace('\n', '')
            return city
    except:
        sayFileBroken()


StrChooseCity = [
    '好的，您需要更换到哪个常用城市呢？',
    '啊，您要更改常用城市了吗',
    '您现在到哪了呀',
    '收到，城市更换到哪里？',
    '更换中，对了，更换到哪里呢？']


def changeCity():
    say(choice(StrChooseCity))
    city = input_()
    if city.find('皋安') != -1:
        city = '皋安\n'  # 高安
    elif city.find('青倒') != -1:
        city = '青倒\n'  # 青岛
    elif city.find('泰安') != -1:
        city = '太安\n'  # 泰安
    elif city.find('黄岛') != -1:
        city = '黄倒\n'  # 黄岛
    else:
        say('常用城市中好像没有这个城市呢')
        return 0
    try:
        with open('config', 'r+', encoding='utf-8') as f:
            config = f.readlines()
        with open('config', 'w+', encoding='utf-8') as f:
            if config[1] == city:
                say('您已经设置了{}哦'.format(city.replace('\n', '')))
            else:
                config[1] = city
                f.writelines(config)
                say('更改至{}成功'.format(city.replace('\n', '')))
    except:
        sayFileBroken()


def configInit():
    say('斋主，确定要格式化配置文件吗？权限密令是？')
    if input_().find('竹隐紫铎斋斋主') == -1:
        say('权限密令错误')
        return 0
    else:
        say('确认身份，正在格式化中')
        try:
            with open('config', 'w+', encoding='utf-8') as f:
                f.writelines('#城市信息\n皋安\n')
            say('格式化成功，文件已恢复')
        except:
            say('初始化失败，请检查源代码。')
            exit()
