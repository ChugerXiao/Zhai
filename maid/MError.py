from random import choice
from speech import say

StrConnectError = [
    '斋主，请连接网络',
    '回斋主，没有检测到网络链接呢',
    '没有接入网络，我没办法知道更多信息哦',
    '无法投射到局域网，请斋主检查网络']


def sayConnectError():
    say(choice(StrConnectError))


StrFileBroken = [
    '斋主，文件被损坏',
    '斋主，主要文件丢失了',
    '斋主，请将我格式化',
    '斋主，文件错误，请初始化']


def sayFileBroken():
    say(choice(StrFileBroken))
    exit()
