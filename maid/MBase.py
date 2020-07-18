from speech import say
from random import choice

# 没事、闭嘴、不要说话
StrBye = [
    '抱歉，打扰了',
    '好的，有事再叫我',
    '啊，我自作多情了吗']


def sayBye():
    say(choice(StrBye))


# 紫铎
StrHello = [
    '咋了，斋主',
    '怎么了，斋主',
    '有事吗',
    '叫我干什么',
    '斋主请吩咐']


def sayHello():
    say(choice(StrHello))


# 没有数据时
StrAgain = [
    '你说啥来着？',
    '抱歉啊，刚刚走神了',
    '啊，可以再说一遍吗',
    '没听清啊']


def sayAgain():
    say(choice(StrAgain))


# 紫铎
# 叫两遍紫铎
StrTwice = [
    '你说吧，我听着呢',
    '咋了，斋主',
    '怎么了，斋主',
    '有事吗',
    '叫我干什么',
    '斋主请吩咐',
    '用不着一直叫我哦',
    '您只用吩咐一遍就行了呢']


def sayTwice():
    say(choice(StrTwice))


# 能听懂、听得懂
# 你能听懂我说话吗
StrUnderstand = [
    '应该可以吧',
    '对不起，有些知识是我的盲区，需要斋主的设定',
    '大部分还是可以听懂的',
    '我会不断更新学习，最后应该能像一个人类一样与你交流的吧']


def sayUnderstand():
    say(choice(StrUnderstand))
