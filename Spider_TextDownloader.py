import requests, sys, random, myOrders
from bs4 import BeautifulSoup

sectionName = []
sectionUrl = []

if __name__ == '__main__':
    index = input('欢迎进入小说下载器，暂时只支持www.50xs.net网站的链接\n请输入目录页网址：')  # 目录网页
    section = requests.get(index)
    section.encoding = section.apparent_encoding
    bs_1 = BeautifulSoup(section.text, 'html.parser')
    section = BeautifulSoup(str(bs_1.find_all('div', 'zjbox')[0]), 'html.parser').find_all('a')
    filename = BeautifulSoup(str(bs_1.find_all('div', id='info')[0]), 'html.parser').find_all('h1')[0].text
    print('开始下载小说：' + filename)

    for each in section[:]:
        sectionName.append(each.string)
        sectionUrl.append('http://www.50xs.net' + each.get('href'))

    for each in range(len(section)):
        article = requests.get(sectionUrl[each])
        article.encoding = article.apparent_encoding
        article = BeautifulSoup(article.text, 'html.parser').find_all('div', id='content')
        article = article[0].text.replace('\xa0' * 4, '').replace('\n', '').replace('        ', '').replace(
            '武林小说 www.50xs.net ，最快更新', '').replace('最新章节！', '')
        with open(filename + '.txt', 'a', encoding='utf-8') as f:
            f.write(sectionName[each] + '\n')
            f.writelines(article)
            f.write('\n\n')
        myOrders.showBar(each, len(section))
    print(filename + '下载成功！！！')
