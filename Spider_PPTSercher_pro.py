# coding=utf-8

from requests import get as _get
from os import system, mkdir, path, remove, rename, listdir
from shutil import move
from bs4 import BeautifulSoup
from myOrders import showBar
from rarfile import RarFile
from zipfile import ZipFile
from urllib3 import disable_warnings, exceptions

disable_warnings(exceptions.InsecureRequestWarning)


def init():
    sys = system('color F0') + system("mode con cols=70 lines=30") + system('title 视频下载器{}紫铎斋出品'.format(' ' * 20))
    return sys


def searcher():
    sys = system('cls')
    key = input('欢迎进入PPT下载器\n紫铎斋诸葛翛潇出品\n请输入查找的PPT类型关键词：')
    while True:
        if len(key.encode('gbk')) < 2:
            sys = system('cls')
            key = input('字节过短。。。\n请重新输入关键词：')
            continue
        try:
            msg = BeautifulSoup(str(
                BeautifulSoup(_get('http://www.ypppt.com/p/search.php?q={}'.format(key), verify=False).text,
                              'html.parser').find_all('div', class_='page-navi')[0]), 'html.parser').find_all('a')
            msg = str(msg[len(msg) - 1])
            num = int(msg[msg.find('TotalResult=') + 12:msg.find('&amp;PageNo')])
            if num > 300: num = 300
            page = int(msg[msg.find('PageNo=') + 7:msg.find('">末页')])
        except:
            sys = system('cls')
            key = input('没有找到你要的PPT模板。。。\n请换关键词：')
            continue
        sys = system('cls')
        DownloadNum = input('关键字为“{}”，输入“0”换关键字\n总共找到{}个匹配PPT\n请输入下载个数：'.format(key, num))
        while True:
            try:
                DownloadNum = int(DownloadNum)
                break
            except:
                sys = system('cls')
                DownloadNum = input('关键字为“{}”，输入“0”换关键字\n总共找到{}个匹配PPT\n请用阿拉伯数字正确输入下载个数：'.format(key, num))
                continue
        if DownloadNum == 0:
            sys = system('cls')
            key = input('请输入查找的PPT类型关键词：')
            continue
        DownloadNum = num if DownloadNum > num else DownloadNum
        responds = []
        print('找到资源，处理中。。。')
        for each in range(1, page + 1):
            headers = {
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
                'Host': 'www.ypppt.com',
                'Referer': 'http://www.ypppt.com/'
            }
            params = {"kwtype": each, 'q': key}
            try:
                responds = responds + BeautifulSoup(
                    _get('http://www.ypppt.com/p/search.php?keyword={}&PageNo={}'.format(key, each), params,
                         verify=False, headers=headers).text, 'html.parser').find_all('a', class_='img_preview')
                if len(responds) >= DownloadNum: break
            except:
                print('请检测网络连接')
                while True: pass

        sys = system('cls')
        print('正在读取下载网址。。。')
        code = [each.get('href')[14:each.get('href').find('.html')] for each in responds[0:DownloadNum] if each]
        return code, key


def processor(code):
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        'Host': 'www.ypppt.com'}
    downloadHref = BeautifulSoup(
        _get('http://www.ypppt.com/p/d.php?aid={}'.format(code), {"aid": code}, verify=False, headers=headers).text,
        'html.parser').find_all('a')[0].get('href')
    if downloadHref.find('pan.baidu') != -1:
        pass
    elif downloadHref.find('uploads') != -1:
        downloadHref = 'http://www.ypppt.com' + downloadHref
    return downloadHref


def judgeFile(filename, namelist, delete=True):
    if delete:
        if path.exists('temp\\{}.temp'.format(filename)):
            remove('temp\\{}.temp'.format(filename))
    for each in namelist:
        if each.find(filename) != -1:
            return -1
    return 0


def newDir():
    try:
        mkdir('temp')
    except:
        pass
    try:
        mkdir('PPT')
    except:
        pass


def downloader(code, key):
    newDir()
    error = exist = 0
    isError = isExist = ''
    nameList = listdir('PPT')
    extensions = []
    print('读取成功！开始下载')
    for each in range(len(code)):
        showBar(each + 1, len(code) + 1)
        filename = key + code[each]
        judgeCode = judgeFile(filename, nameList)
        if judgeCode == -1: continue
        try:
            downloadUrl = processor(code[each])
            extensions.append(downloadUrl[len(downloadUrl) - 4:len(downloadUrl)])
            with open('temp\\{}.temp'.format(filename), 'wb') as f:
                f.write(_get(downloadUrl, verify=False).content)
        except:
            pass
    print('\n下载完毕！正在解压')
    for each in range(len(code)):
        showBar(each + 1, len(code) + 1)
        filename = key + code[each]
        judgeCode = judgeFile(filename, nameList, False)
        if judgeCode == -1:
            exist = exist + 1
            continue
        extension = extensions[each]
        try:
            move('temp\\{}.temp'.format(filename), 'PPT\\{}{}'.format(filename, extension))
            if extension == '.rar':
                package = RarFile('PPT\\{}.rar'.format(filename))
            elif extension == '.zip':
                package = ZipFile('PPT\\{}.zip'.format(filename))
            else:
                print('\r{}{}解压失败，格式不支持。{}'.format(filename, extension, ' ' * 5))
                error = error + 1
                continue
            name = package.namelist()[0]
            package.extractall('PPT')
            package.close()
            try:
                rename('PPT\\{}'.format(name), 'PPT\\{}{}'.format(filename, name))
            except:
                pass
        except:
            print('\r{}{}解压失败，找不到文件。{}'.format(filename, extension, ' ' * 5))
            error = error + 1
    print('\n下载成功！处理文件中。。。')
    for each in listdir('PPT'):
        if path.splitext(each)[1] != '.ppt' and path.splitext(each)[1] != '.pptx' and not path.isdir('PPT\\' + each):
            remove('PPT\\' + each)
    if error > 0: isError = '，{}个错误'.format(error)
    if exist > 0: isExist = '，{}个文件已存在。'.format(exist)
    print('PPT下载成功，共{}个{}{}'.format(len(code), isError, isExist))
    while True: pass


if __name__ == '__main__':
    init()
    while True:
        try:
            codes, keys = searcher()
            downloader(codes, keys)
        except:
            print('\n\n出错了！请将错误发送给开发人员，QQ：3412546697，万分感谢')
            while True: pass
