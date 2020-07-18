# coding=utf-8

from requests import post, get as _get
from mySpider import writeFile
from os import system, path, mkdir
from json import loads
from urllib.parse import quote


def init():
    try:
        mkdir('music')
    except:
        pass
    source = ['netease', 'qq', 'kugou', 'kuwo', 'xiami', 'baidu', '1ting', 'migu', 'lizhi', 'qingting', 'ximalaya',
              'kg']
    sys = system('color F0') + system("mode con cols=70 lines=30") + system(
        'title 音乐下载器{}紫铎斋出品'.format(' ' * 20)) + system('cls')
    print('\n{}感谢使用紫铎斋音乐下载器！{}\n'.format('-' * 22, '-' * 22))
    print(
        '  目前支持以下源：\n\n  0. 网易云{}1. QQ音乐\n  2. 酷狗音乐{}3. 酷我音乐\n  4. 虾米{}5. 百度音乐\n  6. 一听音乐{}7. 咪咕\n  8. 荔枝{}9. 蜻蜓\n  10. 喜马拉雅{}11. 全民K歌'.format(
            ' ' * 24, ' ' * 22, ' ' * 26, ' ' * 22, ' ' * 26, ' ' * 21))
    SourceCode = input('\n注：有一些源暂时无解析，等待一段时间就可能能用了。\n推荐：酷狗音乐、咪咕、网易云。\n\n请输入站点编号：')
    while 1:
        try:
            SourceCode = int(SourceCode)
            Type = source[SourceCode]
            break
        except:
            sys = system('cls')
            print('\n{}感谢使用紫铎斋音乐下载器！{}\n'.format('-' * 22, '-' * 22))
            print(
                '  目前支持以下源：\n\n  0. 网易云{}1. QQ音乐\n  2. 酷狗音乐{}3. 酷我音乐\n  4. 虾米{}5. 百度音乐\n  6. 一听音乐{}7. 咪咕\n  8. 荔枝{}9. 蜻蜓\n  10. 喜马拉雅{}11. 全民K歌'.format(
                    ' ' * 24, ' ' * 22, ' ' * 26, ' ' * 22, ' ' * 26, ' ' * 21))
            SourceCode = input('\n注：有一些源暂时无解析，等待一段时间就可能能用了。\n推荐：酷狗音乐、咪咕、网易云。\n\n请输入正确的站点编号：')
    return Type


def searcher(Type):
    sys = system('cls')
    while 1:
        name = input('请输入你想下载的歌曲：')
        nameCode = quote(name)
        url = 'https://www.socarchina.com/vipmusic/'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Length': '63',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Cookie': 'Brjo_2132_saltkey=UM0H0Cs6; Brjo_2132_lastvisit=1594892754; Brjo_2132_sid=mHc1X3; Brjo_2132_pc_size_c=0; Brjo_2132_sendmail=1; _uab_collina=159489635439437499862825; Hm_lvt_96e8508a8fb22d0cd3c3f57935679158=1594896357; Brjo_2132_lastact=1594896366%09forum.php%09image; UM_distinctid=173573b3e837cd-0e734a44273d72-4353760-144000-173573b3e84790; CNZZDATA3060925=cnzz_eid%3D1699485804-1594894289-%26ntime%3D1594894289; Hm_lpvt_96e8508a8fb22d0cd3c3f57935679158=1594896368',
            'Host': 'www.socarchina.com',
            'Origin': 'https://www.socarchina.com',
            'Referer': 'https://www.socarchina.com/vipmusic/?name={}&type={}'.format(nameCode, Type),
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }
        data = {
            'input': name,
            'filter': 'name',
            'type': Type,
            'page': '1'
        }
        fileName = urlS = 0
        print('搜索中。。。请稍后')
        try:
            res = post(url, data=data, headers=headers).text
            res = loads(res)['data']
        except:
            sys = system('cls')
            print('TimeOutError\n网络异常，请检查网络，稍后重试。')
            while 1: pass
        title, downUrl, author = [i['title'] for i in res], [i['url'] for i in res], [i['author'] for i in res]
        for each in range(len(author)):
            if author[each] == '':
                author[each] = '未知歌手'
        sys = system('cls')
        if len(title) == 0:
            print('没有找到匹配结果。可以尝试减少关键字。')
            continue
        for each in range(len(title)):
            print('{}. {} - {}'.format(each, author[each], title[each]))
        code = input('10.重新搜索\n11.更换源站\n请输入要下载的歌曲编号：')
        while 1:
            try:
                code = int(code)
                if code == 10 or code == 11: break
                fileName, urlS = '{} - {}'.format(author[code], title[code]), downUrl[code]
                if urlS[len(urlS) - 4:len(urlS) - 3] != '.':
                    sys = system('cls')
                    for each in range(len(title)):
                        print('{}. {} - {}'.format(each, author[each], title[each]))
                    code = input('10.重新搜索\n11.更换源站\n这个源出了点小问题。。。请选择其他源或其他歌手：')
                    continue
                if path.exists('music\\' + fileName + urlS[len(urlS) - 4:len(urlS)]):
                    sys = system('cls')
                    for each in range(len(title)):
                        print('{}. {} - {}'.format(each, author[each], title[each]))
                    code = input('10.重新搜索\n11.更换源站\n{}已存在。\n请选择：'.format(fileName))
                    continue
                try:
                    print('加载中。。。')
                    video = _get(urlS)
                    writeFile(video, 'music\\' + fileName + urlS[len(urlS) - 4:len(urlS)])
                    sys = system('cls')
                except:
                    sys = system('cls')
                    print('TimeOutError\n网络异常，请检查网络，稍后重试。')
                    while 1: pass
                for each in range(len(title)):
                    print('{}. {} - {}'.format(each, author[each], title[each]))
                code = input('10.重新搜索\n11.更换源站\n{}下载成功！！！\n请选择：'.format(fileName))
            except:
                sys = system('cls')
                for each in range(len(title)):
                    print('{}. {} - {}'.format(each, author[each], title[each]))
                code = input('10.重新搜索\n11.更换源站\n请正确输入编号：')
                continue

        if code == 10:
            sys = system('cls')
            continue
        if code == 11:
            Type = init()
            sys = system('cls')
            continue
    return Type


if __name__ == '__main__':
    TypeMain = init()
    TypeMain = searcher(TypeMain)
