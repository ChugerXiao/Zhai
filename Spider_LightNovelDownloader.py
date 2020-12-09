from requests import get as _get
from bs4 import BeautifulSoup as _Bs
from mySpider import writeArticle
from myOrders import showBar
from os.path import exists
from os import system


def getFirstHref(url):
    oral = _get(url)
    oral.encoding = oral.apparent_encoding
    capitalList = _Bs(oral.text, 'html.parser').find_all('ul', id="chapterList")[0]
    capitalList = _Bs(str(capitalList), 'html.parser').find_all('a')
    nameList = [each.text for each in capitalList if each]
    FirstHref = capitalList[0].get('href')
    bookName = _Bs(oral.text, 'html.parser').find_all('meta', property="og:novel:book_name")[0].get('content') + '.txt'
    print('Get book information success!')
    return nameList, FirstHref, bookName


def downloader(FirstHref, bookName):
    oral = _get('https://www.x23qb.com' + FirstHref)
    oral.encoding = oral.apparent_encoding
    content = _Bs(oral.text, 'html.parser').find_all('div', id="TextContent")[0].text
    for delete in ['style_tp();', 'style_bm();', 'chapter();', '铅笔小说', '(www.x23qb.com)']:
        content = content.replace(delete, '')
    content = '\n\n'.join(each.replace(' ', '').replace('\xa0', ' ') for each in content.split('\n') if
                          each.replace(' ', '').replace('　', ''))
    with open(bookName, 'a', encoding='utf-8') as f:
        f.writelines(content)
    msg = str(_Bs(oral.text, 'html.parser').find_all('p', class_="mlfy_page")[0])
    msg = _Bs(msg, 'html.parser').find_all('a')[4].get('href')
    if msg.find('_') != -1:
        msg = downloader(msg, bookName)
    return msg

def init(bookName):
    if exists(bookName):
        try:
            system('del {}'.format(bookName))
        except:
            print('error!')
            while 1:pass

if __name__ == '__main__':
    bookCode = input("Please put in book code:")
    name, href, fileName = getFirstHref(f'https://www.x23qb.com/book/{bookCode}/')
    init(fileName)
    with open(fileName, 'a', encoding='utf-8') as f:
        f.write(fileName.replace('.txt',''))
    for num in range(len(name)):
        showBar(num, len(name))
        writeArticle(f'\n\n\n\n{name[num]}\n\n', '', fileName)
        href = downloader(href, fileName)
