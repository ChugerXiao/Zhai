from sys import stdout
from math import ceil
from win32con import KEYEVENTF_KEYUP, WM_PASTE, WM_KEYDOWN, VK_RETURN
from win32api import keybd_event
from win32gui import FindWindow, SendMessage, IsWindowVisible, IsWindow, IsWindowEnabled, ShowWindow, GetWindowText, \
    EnumWindows
from time import sleep
from pyperclip import copy, paste


# 进度条，默认5%一格
def showBar(small, big, preEqual: "int" = 5):
    proportion = float(small / (big - 1)) * 100
    stdout.write('\r%.1f%%' % proportion + '{}>{}'.format('=' * int(proportion / preEqual),
                                                          '-' * ceil((100 - proportion) / preEqual)))
    stdout.flush()


# 比较输入数字大小，返回错误2，大于1，小于-1，在闭区间0.
def judgingNumber(down, up, num):
    try:
        num = float(num)
    except:
        return 2
    try:
        if down > up:
            return 2
    except:
        return 2
    if num > up:
        judge = 1
    else:
        judge = -1 if num < down else 0
    return judge


def copySelected():
    keybd_event(17, 0, 0, 0)
    keybd_event(67, 0, 0, 0)
    sleep(0.01)
    keybd_event(67, 0, KEYEVENTF_KEYUP, 0)
    keybd_event(17, 0, KEYEVENTF_KEYUP, 0)


def fillIn(text):
    try:
        clipboard = paste()
    except:
        clipboard = ''
    copy(text)
    keybd_event(17, 0, 0, 0)
    keybd_event(86, 0, 0, 0)
    sleep(0.01)
    keybd_event(86, 0, KEYEVENTF_KEYUP, 0)
    keybd_event(17, 0, KEYEVENTF_KEYUP, 0)
    sleep(0.01)
    copy(clipboard)


def QQSend(receiver, msg, send: 'bool' = True):
    clipboard = paste()
    copy(msg)
    windows = getAllWindows()
    result = False
    for each in range(len(windows)):
        if windows[each] == receiver:
            result = True
            break
        elif windows[each].find(receiver) != -1 and windows[each].find('个会话') != -1:
            receiver = windows[each]
            result = True
            break
    if result:
        QQ = FindWindow('TXGuiFoundation', receiver)
        ShowWindow(QQ, 1)
        SendMessage(QQ, WM_PASTE, 0, 0)
        if send:
            SendMessage(QQ, WM_KEYDOWN, VK_RETURN)
            ShowWindow(QQ, 6)
        copy(clipboard)
        return 0
    else:
        copy(clipboard)
        return -1


def getAllWindows():
    titles = set()

    def menu(handle, m):
        if IsWindow(handle) and IsWindowEnabled(handle) and IsWindowVisible(handle):
            titles.add(GetWindowText(handle))

    EnumWindows(menu, 0)
    titles = [each for each in titles if each]
    titles.sort()
    return titles
