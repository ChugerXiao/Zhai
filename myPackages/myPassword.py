from random import randint

passwordPanel = ['蛊', '坤', '临', '晋', '师', '否', '复', '巽', '乾', '丰', '蹇', '比', '小畜', '升', '小过', '兑', '明夷', '谦', '贲',
                 '咸', '井', '噬嗑', '姤', '遁', '随', '渐', '革', '剥', '大畜', '恒', '坎', '观', '同人', '蒙', '睽', '困', '履', '需',
                 '讼', '节', '泰', '萃', '大壮', '夬', '中孚', '鼎', '大有', '颐', '无妄', '家人', '损', '涣', '屯', '益', '震', '旅',
                 '艮', '豫', '归妹', '解', '未济', '既济', '离', '大过']

mixPanel = ['天', '地', '山', '泽', '水', '火', '风', '雷']

intervalPanel = ['吉', '凶', '元', '亨', '利', '贞']


def toScale(number):
    scale = ''
    number = int(number)
    while number != 0:
        remainder = str(number % 64)
        number = int(number / 64)
        if len(remainder) == 1:
            remainder = '0' + remainder
        scale = remainder + scale
    return scale


def toDec(number):
    power = dec = 0
    number = str(number)
    while len(number) != 0:
        scale = number[len(number) - 2:]
        number = number[: len(number) - 2]
        dec = dec + int(scale) * pow(64, power)
        power = power + 1
    return dec


def encryption(String: 'str'):
    password = ''
    character = [each for each in String]
    for each in range(len(character)):
        scale = toScale(ord(character[each]))
        singlePassword = ''
        while len(scale) != 0:
            tempNum = int(scale[len(scale) - 2:])
            scale = scale[:len(scale) - 2]
            ran = randint(0, 7)
            tempWord = passwordPanel[tempNum]
            if len(tempWord) == 1: tempWord = mixPanel[ran] + tempWord if bool(randint(0, 1)) else tempWord + mixPanel[
                ran]
            singlePassword = tempWord + singlePassword
        singlePassword = singlePassword + intervalPanel[randint(0, 5)]
        password = password + singlePassword
    return password


def decode(code: 'str'):
    origin = ''
    for each in intervalPanel:
        code = code.replace(each, 'interval')
    character = code.split('interval')
    character = [each for each in character if each]
    for each in range(len(character)):
        tempCode = ''
        while character[each] != '':
            singlePassword = character[each][len(character[each]) - 2:]
            character[each] = character[each][:len(character[each]) - 2]
            for mix in mixPanel:
                singlePassword = singlePassword.replace(mix, '')
            code = str(passwordPanel.index(singlePassword))
            tempCode = ('0' + code if len(code) == 1 else code) + tempCode
        tempOrigin = chr(toDec(tempCode))
        origin = origin + tempOrigin
    return origin
