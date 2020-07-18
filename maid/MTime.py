from speech import say
from random import choice
from datetime import datetime

# 时候、几点、时间
# 现在几点了
StrTime = [
    '现在是{}{}点{}分',
    '斋主，已经{}{}点{}分了',
    '现在到了{}{}点{}分了',
    '{}{}点{}分']
StrTimeNight = [
    '都这么晚了还不睡觉呀',
    '斋主快点睡觉哦',
    '斋主晚安']


def sayTime():
    time = datetime.now()
    hour = time.hour - 12 if time.hour > 12 else time.hour
    if time.hour < 6:
        apm = '凌晨'
    elif time.hour < 9:
        apm = '早上'
    elif time.hour < 12:
        apm = '上午'
    elif time.hour < 14:
        apm = '中午'
    elif time.hour < 18:
        apm = '下午'
    elif time.hour < 21:
        apm = '傍晚'
    else:
        apm = '晚上'
    say(choice(StrTime).format(apm, hour, time.minute))
    if time.hour > 22:
        say(choice(StrTimeNight))


# 日子、几号
# 今天几号了
StrDate = [
    '金天是{}年{}月{}日',
    '{}年{}月{}日']


def sayDate():
    time = datetime.now()
    say(choice(StrDate).format(time.year, time.month, time.day))


# 周几、星期几
# 今天周几
StrWeek = [
    '金天周{}',
    '周{}',
    '金天星期{}',
    '星期{}',
]


def sayWeek():
    say(choice(StrWeek).format(datetime.now().weekday() + 1))
