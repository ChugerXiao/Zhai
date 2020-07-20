# myPackages
Some packages of mine.

----------------------------------------

这些是我为了方便平常使用而封装的一些常用代码。
使用方法例：
```python
import myOrders
from mySpider import writeFile
```

> myOrders
收录一些常用的日常代码
```python
def showBar(small, big, preEqual: "int" = 5):pass
# 显示进程条，例如50%=====>-----
# 参数：已执行进程数，总进程数，每一个格子代表的百分数

def judgingNumber(down, up, num):pass
# 比较输入数字大小，返回错误2，大于1，小于-1，在闭区间0.
# 参数：最小数，最大数，判断数

def copySelected():pass
# 复制选定的内容

def fillIn(text):pass
# 模拟键盘输入
# 参数：输入内容

def QQSend(receiver, msg, send: 'bool' = True):pass
# 发送QQ信息，需要打开QQ窗口。
# 参数：
```