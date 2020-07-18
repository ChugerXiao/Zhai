from pyperclip import paste, copy
from myOrders import copySelected, QQSend
from time import sleep
from speech import say
from datetime import datetime
from win32api import keybd_event
from win32con import KEYEVENTF_KEYUP


def doHealthSignIn():
    clipboard = paste()
    copySelected()
    sleep(0.01)
    keybd_event(46, 0, 0, 0)
    keybd_event(46, 0, KEYEVENTF_KEYUP, 0)
    receiver = '测控一班666'
    msg = paste()
    copy(clipboard)
    time = datetime.now()
    lines = len([each for each in msg.split('\n') if each])
    myMsg = '\n{}.本人廖辰玮，目前在江西省高安市，今日本人和家人体温正常，我承诺本人身体健康情况和行程信息准确上报，服从学校疫情防控要求。'
    if msg.find('今日本人和家人体温正常') != -1 and msg.find('廖辰玮') != -1:
        say('您今日已完成签到')
    elif msg.find('今日本人和家人体温正常') != -1:
        msg = msg + myMsg.format(lines)
        code = QQSend(receiver, msg.replace('\n\n','\n'))
        if code == -1:
            say('签到失败，请斋主打开群聊界面')
        else:
            say('签到成功')
    else:
        msg = '{}.{}'.format(time.month, time.day) + myMsg.format(1)
        code = QQSend(receiver, msg, False)
        if code == -1:
            say('签到失败，请斋主打开群聊界面')
        else:
            say('未找到别人的签到信息，请斋主手动发送第一条')
