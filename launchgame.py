# -*- coding:utf-8 -*-
import wx
import os
from installgame import *

class launchgame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='启动游戏', size=(500, 400),name='launchgame',style=541072896)
		icon = wx.Icon(r'./logol.png')
		self.SetIcon(icon)
		self.launchgame = wx.Panel(self)
		self.launchgame.SetOwnBackgroundColour((255, 245, 196, 255))
		self.Centre()
		self.an1 = wx.Button(self.launchgame,size=(120, 80),pos=(0, 0),label='安装游戏',name='button')
		an1_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
		self.an1.SetFont(an1_字体)
		self.an1.SetForegroundColour((255, 255, 255, 255))
		self.an1.SetOwnBackgroundColour((124, 205, 124, 255))
		self.an1.Bind(wx.EVT_BUTTON,self.installgame_anbdj)
		self.startgame = wx.Button(self.launchgame,size=(305, 145),pos=(162, 204),label='启动游戏！',name='startgame')
		startgame_字体 = wx.Font(20,74,90,400,False,'Microsoft YaHei UI',28)
		self.startgame.SetFont(startgame_字体)
		self.startgame.SetForegroundColour((255, 255, 255, 255))
		self.startgame.SetOwnBackgroundColour((124, 205, 124, 255))
		self.startgame.Bind(wx.EVT_BUTTON,self.startgame_anbdj)
		self.gamever = wx.TextCtrl(self.launchgame,size=(203, 26),pos=(211, 145),value='',name='text',style=0)
		self.l1 = wx.StaticText(self.launchgame,size=(251, 36),pos=(184, 104),label='输入游戏版本:',name='l1',style=2321)
		l1_字体 = wx.Font(20,74,90,400,False,'Microsoft YaHei UI',28)
		self.l1.SetFont(l1_字体)
		
		
	def startgame_anbdj(self,event):
		startgamever = self.gamever.GetValue()
		os.system("java -jar cmcl.jar config exitWithMinecraft false")
		os.system("java -jar cmcl.jar config checkAccountBeforeStart true")
		os.system("java -jar cmcl.jar config printStartupInfo true")
		os.system("java -jar cmcl.jar " + startgamever)

		
	def installgame_anbdj(self,event):
		self.frame = installgame()
		self.frame.Show(True)
		installgame.Show(True)
		
