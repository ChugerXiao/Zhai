from MTime import *
from MBase import *
from MWeather import *
from MConfig import *
from MOpen import *
from MRegister import *


def Say(Loop=True):
    while Loop:
        Loop = False
        talk = input_()
        if talk.find('没事') != -1 or talk.find('闭嘴') != -1 or talk.find('不要说话') != -1:
            sayBye()
        elif talk.find('能听懂') != -1 or talk.find('听得懂') != -1:
            sayUnderstand()

        elif talk.find('时候') != -1 or talk.find('几点') != -1 or talk.find('时间') != -1:
            sayTime()
        elif talk.find('日子') != -1 or talk.find('几号') != -1:
            sayDate()
        elif talk.find('周几') != -1 or talk.find('星期几') != -1:
            sayWeek()

        elif talk.find('今天') != -1 and talk.find('天气') != -1:
            sayWeatherToday()
        elif talk.find('这几天') != -1 and talk.find('天气') != -1:
            sayWeatherThreeDay()

        elif talk.find('更换城市') != -1:
            changeCity()
        elif talk.find('格式化配置文件') != -1:
            configInit()

        elif talk.find('打开') != -1:
            doOpen(talk)
        elif talk.find('搜索') != -1:
            doSearch(talk)

        elif talk.find('健康打卡') != -1:
            doHealthSignIn()

        elif talk.find('紫铎') != -1:
            sayTwice()
            Loop = True
        else:
            sayAgain()
            Loop = True


if __name__ == '__main__':
    while True:
        speak = input_()
        if speak.find('紫铎') != -1:
            sayHello()
            Say()
