# myPackages
Some packages of mine.

----------------------------------------

这些是我为了方便平常使用而封装的一些常用代码。
使用方法示例：
```python
# 将.py文件和myPackages内文件放在同一文件夹下，然后加上以下代码。
import myOrders
from mySpider import writeFile
```

---

> myOrders.py
收录一些常用的日常代码
```python
import sys, math, win32con, win32api, win32gui, time, pyperclip

def showBar(small, big, preEqual: "int" = 5):pass
# 显示进程条，例如50%=====>-----。
# 参数：已执行进程数，总进程数，每一个格子代表的百分数

def judgingNumber(down, up, num):pass
# 比较输入数字大小，返回错误2，大于1，小于-1，在闭区间0。
# 参数：最小数，最大数，判断数

def copySelected():pass
# 复制选定的内容。

def fillIn(text):pass
# 模拟键盘输入。
# 参数：输入内容

def QQSend(receiver, msg, send: 'bool' = True):pass
# 发送QQ信息，需要打开QQ窗口。
# 参数：收信息人，信息内容（支持emoji），是否发送

def getAllWindows():pass
# 获取所有打开的窗口名字。
```
> mySpider.py
收录一些写爬虫时常用的代码
```python
import requests

def requestsWhileTimes(url, time, times=1, string='erro', cut: 'bool' = False, headers={}, params={}):pass
# 使用requests.get爬取网页多次，失败就重新爬取。
# 参数：网页，连接超时时间，尝试次数，提示错误信息，超过次数是否停止代码运行，headers，data

def requestsWhileSeccess(url, time, headers={}, params={}):pass
# 使用requests.get爬取网页直到成功。
# 参数：网页，连接超时时间，headers，data

def requestsResult(url, time, string, cut: 'bool' = False, headers={}, params={}):pass
# 使用requests.get爬取网页一次，失败了返回string。
# 参数：网页，连接超时时间，提示错误信息，超过次数是否停止代码运行，headers，data

def writeFile(video, filename):pass
# 下载文件。
# 参数：文件内容，文件命名

def writeArticle(title, article, filename):pass
# 下载文字。
# 参数：文字内容，章名，文字命名
```

> myPassword.py
收录竹隐紫铎斋自创的“六十四数周易加密法”
>><br/>注释：</br>
六十四数周易加密法，将一个字符串的编码转为64进制，然后使用周易六十四卦编码，中间会加入凑数位、分隔位、混淆位等。
**<br/>严肃声明：</br>
谢绝解密！！！找新加密方式解析的大佬请出门右拐。**
```python
import random

def toScale(number):pass
# 将一个十进制数转化为64进制数（输出字符串）。
# 参数：十进制数（支持字符串）

def toDec(number):pass
# 将一个64进制数转化为十进制数（输出字符串）。
# 参数：64进制数（支持字符串）

def encryption(String: 'str'):pass
# 将一个字符串使用六十四数周易法加密。
# 参数：需加密的字符串

def decode(code: 'str'):pass
# 将密码使用六十四数周易法解密。
# 参数：需解密的字符串
```