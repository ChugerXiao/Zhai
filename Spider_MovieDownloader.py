from sys import path,stdout
from requests import packages,get
from math import ceil
from shutil import move
import frozen,os
from bs4 import BeautifulSoup
from multiprocessing import Pool

#请求get网站times次，直到响应，多次无响应输出string，cut控制是否结束程序。
def requestsWhileTimes(url,time,times = 1,string = 'erro',cut:'bool' = False):
	while times > 0:
		try:file = get(url,timeout = time,stream = True,verify = False)
		except:
			times = times - 1 
			if times == 0:
				print(string)
				while cut:a = 1
				file = 0
		else:times = 0
	return file

#进度条，默认5%一格
def showSectionBar(section,small,big,preEqual:'int' = 5):
	proportion = float(small / (big - 1))*100
	stdout.write('\r第' + str(section) + '集：%.1f%%'%proportion + '{}>{}'.format('#' * int(proportion / preEqual),'-' * ceil((100 - proportion) / preEqual)) + '  ')
	stdout.flush()

#比较输入数字大小，返回错误2，大于1，小于-1，在闭区间0.
def judgingNumber(down,up,num):
	try:num = float(num)
	except:return 2
	try:
		if down > up:return 2
	except:return 2
	if num > up:
		judge = 1
	else:
		judge = -1 if num < down else 0
	return judge

#C
def requestsWhileTimesWrite(url,time,times = 1,string = 'error'):
	while times > 0:
		try:file = get(url,timeout = time,stream = True,verify = False)
		except:
			times = times - 1 
			if times == 0:
				writeError(string,'Error.txt')
				file = 0
		else:times = 0
	return file

#一直请求get网站，直到在超时时间内响应。
def requestsWhileSeccess(url,time,headers = {},data = {}):
	while True:
		try:
			file = get(url,timeout = time,stream = True,verify = False,headers = {},data = {})
			return file
		except:a = 1

#在超时时间内请求get网站，成功返回网站内容，失败输出string，cut控制是否结束程序。
def requestsResult(url,time,string,cut:'bool' = False,headers = {},data = {}):
	try:file = get(url,timeout = time,stream = True,verify = False,headers = {},data = {})
	except:
		print(string)
		while cut:a = 1
		file = 0
	return file

#将video写入名为filename的视频类文件中。（只测试了.ts）
def writeVideo(video,filename):
	with open(filename,'ab') as f:
		for file in video.iter_content(chunk_size = 1024):
			if file:
				f.write(file)

#C
def writeError(Error,filename):
	with open(filename,'a',encoding = 'utf-8') as f:
		f.writelines(Error)
		f.write('\n')

def download(code,section):
	path = os.getcwd().replace('\\temp','')
	url = 'https://bili918.net/index.php/vod/play/id/' + code + str(section) + '.html'
	indexUrl = requestsWhileTimes(url,30,3,'\r第{}集下载失败{}'.format(section,' ' * 50),False)
	if indexUrl == 0:return
	name = BeautifulSoup(indexUrl.text,'html.parser').find_all('h1',class_="fn-left")[0].string.replace('《','').replace('》高清在线观看','')
	if os.path.exists('{}\\temp\\{}第{}集.temp'.format(path,name,section)):os.remove('{}\\temp\\{}第{}集.temp'.format(path,name,section))
	if os.path.exists('{}\\{}\\{}第{}集.ts'.format(path,name,name,section)):	print("第{}集已存在,跳过本次下载".format(section))
	else:
		indexUrl = str(BeautifulSoup(indexUrl.text,'html.parser').find_all('div',id="zanpiancms_player")[0])
		indexUrl = (indexUrl[indexUrl.find('"url"') + 7:indexUrl.find('"url_next"') - 2]).replace('\\','').replace('index.m3u8','1000k/hls/index.m3u8')
		code_2 = indexUrl.replace('/1000k/hls/index.m3u8','')
		indexMsg = requestsWhileTimes(indexUrl,30,3,'\r第{}集下载失败{}'.format(section,' ' * 50),False)
		if indexMsg == 0:return
		indexMsg = indexMsg.text.split('\n')
		print('\r开始下载第{}集{}'.format(section,' ' * 50))
		index = []
		error = 0
		for each in range(len(indexMsg)):
			if str(indexMsg[each]).endswith('.ts'):
				index.append(indexMsg[each])
		for each in range(len(index)):
			showSectionBar(section,each,len(index),2)
			movie = requestsWhileTimesWrite(code_2 + '/1000k/hls/' + index[each],20,10,'第{}集    {}下载失败'.format(section,index[each]))
			if movie == 0:
				error = error + 1
				continue
			times = 10
			while times > 0:
				try:writeVideo(movie,'{}第{}集.temp'.format(name,section))
				except:
					times = times - 1
					if times == 0:
						error = error + 1
						writeError('第{}集    {}写入失败'.format(section,index[each]),'Error.txt')
				else:times = 0
		try:move('{}\\temp\\{}第{}集.temp'.format(path,name,section),'{}\\{}\\{}第{}集.ts'.format(path,name,name,section))
		except:error = -1
		if error == 0:print('\r第{}集下载成功！！！{}'.format(section,' ' * 50))
		elif error == -1:print('\r第{}集下载失败，找不到文件。{}'.format(section,' ' * 40))
		else:print('\r第{}集下载完成，错误{}处。{}'.format(section,error,' ' * 40))

if __name__ == '__main__':
	multiprocessing.freeze_support()
	packages.urllib3.disable_warnings()
	try:
		code = input('欢迎进入视频下载器\n请输入下载ID：')
		homeUrl = 'https://bili918.net/index.php/vod/detail/id/' + code + '.html'
		msgBs = BeautifulSoup(requestsWhileTimes(homeUrl,60,1,'网站繁忙，请稍后尝试。',True).text,'html.parser')
		num = len(msgBs.find_all('a',class_ = 'btn')) - 4#获取集数
		code = msgBs.find_all('a',class_ = 'btn')[1].get('href').replace('/index.php/vod/play/id/','').replace('1.html','')
		try:name = msgBs.find_all('h1')[1].string
		except:
			print('没查询到这个ID，请重试。')
			while True:a = 1
		print('《{}》，总共{}集，加载中……'.format(name,num))
		try:os.mkdir(name)
		except:pass
		try:os.mkdir('temp')
		except:pass
		finally:os.chdir('temp')
		startset = input('从第几集开始（0是从头下载）：')
		endset = input('到第几集结束（0是下载剩下集数）：')
		startCode = judgingNumber(1,num,startset)
		endCode = judgingNumber(1,num,endset)
		start = int(startset) if startCode == 0 else 1
		end = int(endset) + 1 if endCode == 0 else int(num + 1)
		pool = Pool(8)
		for section in range(start,end):#[start,end)
			pool.apply_async(download,args = (code,section))
		pool.close()
		pool.join()
		print('《{}》下载完毕'.format(name))
		while True:a = 1
	except:
		print('\n\n出错了！请将错误发送给开发人员，QQ：3412546697，万分感谢')
		while True:a = 1