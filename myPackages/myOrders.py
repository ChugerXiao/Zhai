from sys import stdout
from math import ceil
from win32con import KEYEVENTF_KEYUP, WM_PASTE, WM_KEYDOWN, VK_RETURN
from win32api import keybd_event
from win32gui import FindWindow, SendMessage, IsWindowVisible, IsWindow, IsWindowEnabled, ShowWindow, GetWindowText, \
    EnumWindows
from time import sleep
from pyperclip import copy, paste


# 显示进程条，例如50%=====>-----。
# 参数：已执行进程数，总进程数，每一个格子代表的百分数
def showBar(small, big, preEqual: "int" = 5):
    proportion = float(small / (big - 1)) * 100
    stdout.write('\r%.1f%%' % proportion + '{}>{}'.format('=' * int(proportion / preEqual),
                                                          '-' * ceil((100 - proportion) / preEqual)))
    stdout.flush()


# 比较输入数字大小，返回错误2，大于1，小于-1，在闭区间0。
# 参数：最小数，最大数，判断数
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


# 复制选定的内容。
def copySelected():
    keybd_event(17, 0, 0, 0)
    keybd_event(67, 0, 0, 0)
    sleep(0.01)
    keybd_event(67, 0, KEYEVENTF_KEYUP, 0)
    keybd_event(17, 0, KEYEVENTF_KEYUP, 0)


# 模拟键盘输入。
# 参数：输入内容
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


# 发送QQ信息，需要打开QQ窗口。
# 参数：收信息人，信息内容（支持emoji），是否发送
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


# 获取所有打开的窗口名字。
def getAllWindows():
    titles = set()

    def menu(handle, m):
        if IsWindow(handle) and IsWindowEnabled(handle) and IsWindowVisible(handle):
            titles.add(GetWindowText(handle))

    EnumWindows(menu, 0)
    titles = [each for each in titles if each]
    titles.sort()
    return titles
