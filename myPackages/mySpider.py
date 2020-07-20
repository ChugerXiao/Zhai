import requests


# 使用requests.get爬取网页多次，失败就重新爬取。
# 参数：网页，连接超时时间，尝试次数，提示错误信息，超过次数是否停止代码运行，headers，data
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


# 使用requests.get爬取网页直到成功。
# 参数：网页，连接超时时间，headers，data
def requestsWhileSeccess(url, time, headers={}, params={}):
    while True:
        try:
            file = requests.get(url, timeout=time, stream=True, verify=False, headers={}, params={})
            return file
        except:
            a = 1


# 使用requests.get爬取网页一次，失败了返回string。
# 参数：网页，连接超时时间，提示错误信息，超过次数是否停止代码运行，headers，data
def requestsResult(url, time, string, cut: 'bool' = False, headers={}, params={}):
    try:
        file = requests.get(url, timeout=time, stream=True, verify=False, headers={}, params={})
    except:
        print(string)
        while cut: a = 1
        file = 0
    return file


# 下载文件。
# 参数：文件内容，文件命名
def writeFile(video, filename):
    with open(filename, 'ab') as f:
        for file in video.iter_content(chunk_size=1024):
            if file:
                f.write(file)


# 下载文字。
# 参数：文字内容，章名，文字命名
def writeArticle(title, article, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(title + '\n')
        f.writelines(article)
        f.write('\n\n')
