import frozen
import os
# import requests,math,os,shutil,frozen
from bs4 import BeautifulSoup
from math import ceil
from multiprocessing import Pool
# path.append('E:\\作品\\PY\\lib')
from requests import packages, get
# from os import getcwd,path,mkdir,chdir
from shutil import move
from sys import path, stdout

packages.urllib3.disable_warnings()


# 请求get网站times次，直到响应，多次无响应输出string，cut控制是否结束程序。
def requestsWhileTimes(url, time, times=1, string='erro', cut: 'bool' = False, headers={}, params={}):
    while times > 0:
        try:
            file = get(url, timeout=time, stream=True, verify=False, headers={}, params={})
        except:
            times = times - 1
            if times == 0:
                print(string)
                while cut: a = 1
                file = 0
        else:
            times = 0
    return file


# 进度条，默认5%一格
def showSectionBar(section, small, big, preEqual: 'int' = 5):
    proportion = float(small / (big - 1)) * 100
    stdout.write('\r第' + str(section) + '集：%.1f%%' % proportion + '{}>{}'.format('#' * int(proportion / preEqual),
                                                                                 '-' * ceil((
                                                                                                    100 - proportion) / preEqual)) + '  ')
    stdout.flush()


# 比较输入数字大小，返回错误2，大于1，小于-1，在闭区间0.
def judgingNumber(down, up, num):
    try:
        num = float(num)
    except:
        return 2
    try:
        if down > up: return 2
    except:
        return 2
    if num > up:
        judge = 1
    else:
        judge = -1 if num < down else 0
    return judge


# C
def requestsWhileTimesWrite(url, time, times=1, string='error'):
    while times > 0:
        try:
            file = get(url, timeout=time, stream=True, verify=False)
        except:
            times = times - 1
            if times == 0:
                writeError(string, 'Error.txt')
                file = 0
        else:
            times = 0
    return file


# 一直请求get网站，直到在超时时间内响应。
def requestsWhileSeccess(url, time, headers={}, params={}):
    while True:
        try:
            file = get(url, timeout=time, stream=True, verify=False, headers={}, params={})
            return file
        except:
            a = 1


# 在超时时间内请求get网站，成功返回网站内容，失败输出string，cut控制是否结束程序。
def requestsResult(url, time, string, cut: 'bool' = False, headers={}, params={}):
    try:
        file = get(url, timeout=time, stream=True, verify=False, headers={}, params={})
    except:
        print(string)
        while cut: a = 1
        file = 0
    return file


# 将video写入名为filename的视频类文件中。（只测试了.ts）
def writeVideo(video, filename):
    with open(filename, 'ab') as f:
        for file in video.iter_content(chunk_size=1024):
            if file:
                f.write(file)


# C
def writeError(Error, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.writelines(Error)
        f.write('\n')


def download(code, section):
    path = os.getcwd().replace('\\temp', '')
    url = 'https://bili918.net/index.php/vod/play/id/' + code + str(section) + '.html'
    # indexUrl = str(BeautifulSoup(requests.get(url,stream = True,verify = False).text,'html.parser').find_all('div',id="zanpiancms_player")[0])
    indexUrl = requestsWhileTimes(url, 30, 3, '\r第{}集下载失败{}'.format(section, ' ' * 50), False)
    if indexUrl == 0: return
    name = BeautifulSoup(indexUrl.text, 'html.parser').find_all('h1', class_="fn-left")[0].string.replace('《',
                                                                                                          '').replace(
        '》高清在线观看', '')
    if os.path.exists('{}\\temp\\{}第{}集.temp'.format(path, name, section)): os.remove(
        '{}\\temp\\{}第{}集.temp'.format(path, name, section))
    if os.path.exists('{}\\{}\\{}第{}集.ts'.format(path, name, name, section)):
        print("第{}集已存在,跳过本次下载".format(section))
    else:
        indexUrl = str(BeautifulSoup(indexUrl.text, 'html.parser').find_all('div', id="zanpiancms_player")[0])
        indexUrl = (indexUrl[indexUrl.find('"url"') + 7:indexUrl.find('"url_next"') - 2]).replace('\\', '').replace(
            'index.m3u8', '1000k/hls/index.m3u8')
        code_2 = indexUrl.replace('/1000k/hls/index.m3u8', '')
        # indexMsg = requests.get(indexUrl).text.split('\n')
        indexMsg = requestsWhileTimes(indexUrl, 30, 3, '\r第{}集下载失败{}'.format(section, ' ' * 50), False)
        if indexMsg == 0: return
        indexMsg = indexMsg.text.split('\n')
        print('\r开始下载第{}集{}'.format(section, ' ' * 50))
        index = []
        error = 0
        for each in range(len(indexMsg)):
            if str(indexMsg[each]).endswith('.ts'):
                index.append(indexMsg[each])
        for each in range(len(index)):
            showSectionBar(section, each, len(index), 2)
            movie = requestsWhileTimesWrite(code_2 + '/1000k/hls/' + index[each], 20, 10,
                                            '第{}集    {}下载失败'.format(section, index[each]))
            if movie == 0:
                error = error + 1
                continue
            # faild = True
            # while faild:
            # 	try:movie = requests.get(code_2 + '/1000k/hls/' + index[each],timeout = 20)
            # 	except:faild = True
            # 	else:faild = False
            # with open(name + '第' + str(section) + '集.ts','ab') as f:
            # 	for file in movie.iter_content(chunk_size = 1024):
            # 		if file:
            # 			f.write(file)
            times = 10
            while times > 0:
                try:
                    writeVideo(movie, '{}第{}集.temp'.format(name, section))
                except:
                    times = times - 1
                    if times == 0:
                        error = error + 1
                        writeError('第{}集    {}写入失败'.format(section, index[each]), 'Error.txt')
                else:
                    times = 0
        try:
            move('{}\\temp\\{}第{}集.temp'.format(path, name, section),
                 '{}\\{}\\{}第{}集.ts'.format(path, name, name, section))
        except:
            error = -1
        if error == 0:
            print('\r第{}集下载成功！！！{}'.format(section, ' ' * 50))
        elif error == -1:
            print('\r第{}集下载失败，找不到文件。{}'.format(section, ' ' * 40))
        else:
            print('\r第{}集下载完成，错误{}处。{}'.format(section, error, ' ' * 40))


def searcher():
    keycode = print('欢迎进入视频下载器\n紫铎斋诸葛翛潇出品')
    while True:
        if keycode != None: order = os.system('cls')
        target = 'https://bili918.net/index.php/vod/search.html'
        headers = {
            'Host': 'bili918.net',
            'Referer': 'https://bili918.net/index.php/vod/search.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        params = {'wd': input('请输入需要下载的视频名称：')}
        print('查询中。。。')
        try:
            original = get(target, timeout=60, headers=headers, params=params)
        except:
            print('网站繁忙，请稍后尝试。')
            continue
        original.encoding = original.apparent_encoding
        urls = BeautifulSoup(str(BeautifulSoup(original.text, 'html.parser').find_all('div', class_='player-info-img')),
                             'html.parser').find_all('a')
        msg = BeautifulSoup(original.text, 'html.parser').find_all('h3')
        if len(msg) == 0:
            order = os.system('cls')
            keycode = None
            print('无搜索结果，请换关键词。')
            continue
        for each in range(1, len(msg)):
            print('{} {}'.format(each, str(msg[each])[4:str(msg[each]).find('<em>')]))
        keycode = print('0 重新搜索\n如果以上没有所需视频，请尽可能详细输入名字。')
        while keycode != 0:
            try:
                key = int(input('请输入需要下载的视频前面的编号：'))
            except:
                print('请正确输入！', end='')
                continue
            keycode = judgingNumber(0, len(msg) - 1, key)
            # if keycode != 0:
            # 	print('请正确输入编号：')
            # 	key = 0
            # else:
            # 	code = urls[int(key) - 1].get('href')
            # 	return code
            if keycode == 0:
                if int(key) != 0:
                    code = urls[int(key) - 1].get('href')
                    return code
            else:
                print('请正确输入！', end='')


if __name__ == '__main__':
    multiprocessing.freeze_support()  # 包装exe线程支持
    order = os.system('color F0') + os.system("mode con cols=70 lines=30") + os.system(
        'title 视频下载器{}紫铎斋出品'.format(' ' * 20))
    try:
        code = searcher()
        homeUrl = 'https://bili918.net' + code
        # msgBs = BeautifulSoup(requests.get(homeUrl,stream = True,verify = False).text,'html.parser')
        print('获取网址中。。。')
        msgBs = BeautifulSoup(requestsWhileTimes(homeUrl, 60, 1, '网站繁忙，请稍后尝试。', True).text, 'html.parser')
        num = len(msgBs.find_all('a', class_='btn')) - 4  # 获取集数
        code = msgBs.find_all('a', class_='btn')[1].get('href').replace('/index.php/vod/play/id/', '').replace('1.html',
                                                                                                               '')
        name = msgBs.find_all('h1')[1].string
        order = os.system('cls')
        startCode = endCode = print('《{}》，总共{}集，加载中……'.format(name, num))
        try:
            os.mkdir(name)
        except:
            pass
        try:
            os.mkdir('temp')
        except:
            pass
        finally:
            os.chdir('temp')
        while startCode != 0:
            try:
                start = int(input('从第几集开始下载：'))
            except:
                print('请正确输入！', end='')
                continue
            startCode = judgingNumber(0, num, start)
            if startCode != 0:
                print('请正确输入！', end='')
            elif start == 0:
                start = 1
        while endCode != 0:
            try:
                end = int(input('到第几集结束（0是到最后一集）'))
            except:
                print('请正确输入！', end='')
                continue
            endCode = judgingNumber(0, num, end)
            if endCode != 0:
                print('请正确输入！', end='')
            elif end == 0:
                end = num
        # startset = input('从第几集开始（0是从头下载）：')
        # startCode = judgingNumber(0,num,startset)
        # endset = input('到第几集结束（0是下载剩下集数）：')
        # endCode = judgingNumber(0,num,endset)
        # start = int(startset) if startCode == 0 else 1
        # end = int(endset) + 1 if endCode == 0 else int(num + 1)
        order = os.system('cls')
        print('开始下载《{}》。。。'.format(name))
        pool = Pool(8)
        for section in range(start, end + 1):  # [start,end)
            pool.apply_async(download, args=(code, section))
        pool.close()
        pool.join()
        print('《{}》下载完毕'.format(name))
        while True: a = 1
    except:
        print('\n\n出错了！请将错误发送给开发人员，QQ：3412546697，万分感谢')
        while True: a = 1
