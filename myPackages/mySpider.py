import requests


# 请求get网站times次，直到响应，多次无响应输出string，cut控制是否结束程序。
def requestsWhileTimes(url, time, times=1, string='erro', cut: 'bool' = False, headers={}, params={}):
    while times > 0:
        try:
            file = requests.get(url, timeout=time, stream=True, verify=False, headers={}, params={})
        except:
            times = times - 1
            if times == 0:
                print(string)
                while cut: a = 1
                file = 0
        else:
            times = 0
    return file


# 一直请求get网站，直到在超时时间内响应。
def requestsWhileSeccess(url, time, headers={}, params={}):
    while True:
        try:
            file = requests.get(url, timeout=time, stream=True, verify=False, headers={}, params={})
            return file
        except:
            a = 1


# 在超时时间内请求get网站，成功返回网站内容，失败输出string，cut控制是否结束程序。
def requestsResult(url, time, string, cut: 'bool' = False, headers={}, params={}):
    try:
        file = requests.get(url, timeout=time, stream=True, verify=False, headers={}, params={})
    except:
        print(string)
        while cut: a = 1
        file = 0
    return file


# 将video写入名为filename的视频类文件中。（只测试了.ts）
def writeFile(video, filename):
    with open(filename, 'ab') as f:
        for file in video.iter_content(chunk_size=1024):
            if file:
                f.write(file)


# 将以title为标题的article写入名为filename的记事本中。
def writeArticle(title, article, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(title + '\n')
        f.writelines(article)
        f.write('\n\n')
