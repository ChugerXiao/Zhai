from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from json import loads, dumps
from requests import post as _post
from sentence import sentence
from pygame import mixer
from eyed3 import load
from time import sleep
from easygui import msgbox
from os import remove, path
from myOrders import showBar

voicePath = r'E:\作品\PY\speakVoice'  # 后不接/


def downVoice(text, fileName):
    AccessKeyID = 'LTAI4GEZBSdtbaheKuh51sKo'
    AccessKeySecret = 'DX6lXt37ZZSmxtitsjkIkjiaxpvUN5'
    AppKey = 'cFBq8YmZp4CASmhj'

    def getAliKey():
        client = AcsClient(AccessKeyID, AccessKeySecret, 'cn-shanghai')
        request = CommonRequest()
        request.set_method('POST')
        request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
        request.set_version('2019-02-28')
        request.set_action_name('CreateToken')
        re = client.do_action_with_exception(request)
        re = loads(re.decode())
        return re['Token'].get('Id')

    data = {
        'appkey': AppKey,  # 语音合成项目里的appkey
        "text": text,  # 要语音合成的文字
        'token': getAliKey(),  # 上一步的鉴权秘钥
        'format': 'mp3',  # 合成语音的格式
        "sample_rate": "16000",  # 比特率
        "volume": '90',  # 音量
        "pitch_rate": '-25',  # 语调
        "speech_rate": '30',  # 语速
        "voice": 'Aibao'  # 发音人 参数详见 https://help.aliyun.com/document_detail/84435.html
    }
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    r = _post('https://nls-gateway.cn-shanghai.aliyuncs.com/stream/v1/tts', data=dumps(data), headers=header)
    with open(fileName, 'wb+') as file:
        file.write(r.content)


def play(fileName):
    sec = load(fileName).info.time_secs
    mixer.init()
    mixer.music.load(fileName)
    mixer.music.play(start=0.0)
    sleep(int(sec) + 1)
    mixer.music.stop()
    with open(f'{voicePath}/nod.mp3', 'wb+') as f: pass
    mixer.music.load(f'{voicePath}/nod.mp3')


def downAll():
    print('Downloading...')
    nameList = []
    textList = []
    for n, t in sentence.items():
        nameList.append(n)
        textList.append(t)
    for each in range(len(nameList)):
        showBar(each, len(nameList))
        if not path.exists(f'{voicePath}/{nameList[each]}.mp3'):
            try:
                downVoice(textList[each], f'{voicePath}/{nameList[each]}.mp3')
            except:
                try:
                    play(f'{voicePath}/connectError.mp3')
                except:
                    msgbox(sentence['connectError'], 'connectError', '知道了')
                return


def speak(text):
    nameList = []
    textList = []
    for n, t in sentence.items():
        nameList.append(n)
        textList.append(t)
    try:
        index = textList.index(text)  # 查找字典
        fileName = f'{voicePath}/{nameList[index]}.mp3'
    except:
        fileName = f'{voicePath}/temp.mp3'
        try:
            remove(fileName)
        except:
            pass
    try:
        play(fileName)
    except:
        try:
            downVoice(text, fileName)
            play(fileName)
        except:
            try:
                play(f'{voicePath}/connectError.mp3')
            except:
                msgbox(sentence['connectError'], 'connectError', '知道了')
            return
