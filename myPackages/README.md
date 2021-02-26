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

def fileTree(treePath):pass
# 获取目录所有的文件与子文件路径

def getCMDPutout(command):pass
# 实时获取cmd输出信息
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