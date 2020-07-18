from os import startfile
from myOrders import copySelected
from webbrowser import open as openWeb
from time import sleep
from pyperclip import paste


def doOpen(talk):
    if talk.find('软件包') != -1:
        startfile(r'D:\软件')
    if talk.find('作品') != -1:
        startfile(r'E:\作品')
    if talk.find('QQ接收') != -1:
        startfile(r'C:\Users\ERICAN\Documents\Tencent Files\2920233418\FileRecv')


def doSearch(talk):
    if talk.find('选中的东西') != -1 or talk.find('这个') != -1:
        copySelected()
        sleep(0.01)
        openWeb('https://www.baidu.com/s?wd={}'.format(paste()))
    # else talk.find
