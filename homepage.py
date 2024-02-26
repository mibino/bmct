# -*- coding:utf-8 -*-
import wx
from launchgame import *
from user import *
import wx.html2

class homepage(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='基岩我的世界盒子', size=(800, 500),name='homepage',style=541072896)
		icon = wx.Icon(r'./logol.png')
		self.SetIcon(icon)
		self.homepage = wx.Panel(self)
		self.homepage.SetOwnBackgroundColour((255, 245, 196, 255))
		self.Centre()
		title_图片 = wx.Image(r'./img/title.png').ConvertToBitmap()
		self.title = wx.StaticBitmap(self.homepage, bitmap=title_图片,size=(800, 80),pos=(0, 0),name='title',style=0)
		self.title.SetOwnBackgroundColour((124, 205, 124, 255))
		self.user = wx.Button(self.homepage,size=(120, 80),pos=(0, 80),label='用户',name='userbutton')
		user_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
		self.user.SetFont(user_字体)
		self.user.SetForegroundColour((255, 255, 255, 255))
		self.user.SetOwnBackgroundColour((124, 205, 124, 255))
		self.user.Bind(wx.EVT_BUTTON,self.user_anbdj)
		self.bbs = wx.Button(self.homepage,size=(120, 80),pos=(0, 160),label='社区',name='bbs')
		bbs_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
		self.bbs.SetFont(bbs_字体)
		self.bbs.SetForegroundColour((255, 255, 255, 255))
		self.bbs.SetOwnBackgroundColour((124, 205, 124, 255))
		self.bbs.Bind(wx.EVT_BUTTON,self.bbs_anbdj)
		self.settings = wx.Button(self.homepage,size=(120, 80),pos=(0, 240),label='设置',name='settings')
		settings_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
		self.settings.SetFont(settings_字体)
		self.settings.SetForegroundColour((255, 255, 255, 255))
		self.settings.SetOwnBackgroundColour((124, 205, 124, 255))
		self.settings.Bind(wx.EVT_BUTTON,self.settings_anbdj)
		self.an6 = wx.Button(self.homepage,size=(120, 80),pos=(0, 380),label='启动游戏',name='button')
		an6_字体 = wx.Font(18,74,90,400,False,'Microsoft YaHei UI',28)
		self.an6.SetFont(an6_字体)
		self.an6.SetForegroundColour((255, 255, 255, 255))
		self.an6.SetOwnBackgroundColour((255, 128, 0, 255))
		self.an6.Bind(wx.EVT_BUTTON,self.an6_anbdj)
		self.homepagenews = wx.html2.WebView.New(self.homepage,size=(660, 380),pos=(120, 82))
		self.homepagenews.LoadURL("http://luxiaso.w1.luyouxia.net/launcher/")
		self.Bind(wx.EVT_CLOSE, self.OnFormClosed, self)


	def user_anbdj(self,event):
		self.frame = user()
		self.frame.Show(True)
		user.Show(True)


	def bbs_anbdj(self,event):
		print('bbs,按钮被单击')


	def settings_anbdj(self,event):
		print('settings,按钮被单击')


	def an6_anbdj(self,event):
		self.frame = launchgame()
		self.frame.Show(True)
		launchgame.Show(True)
		
	def OnFormClosed(self,event):
		wx.MessageBox("您将退出盒子", "提示" ,wx.OK | wx.ICON_INFORMATION)  
		quit()
