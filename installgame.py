# -*- coding:utf-8 -*-
import wx
import os

class installgame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='安装游戏', size=(500, 400),name='frame',style=541072896)
		icon = wx.Icon(r'./logol.png')
		self.SetIcon(icon)
		self.azyx = wx.Panel(self)
		self.azyx.SetOwnBackgroundColour((255, 245, 196, 255))
		self.Centre()
		self.bq1 = wx.StaticText(self.azyx,size=(328, 22),pos=(72, 26),label='输入要安装的游戏版本',name='staticText',style=2321)
		bq1_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
		self.bq1.SetFont(bq1_字体)
		self.bjk1 = wx.TextCtrl(self.azyx,size=(322, 31),pos=(75, 55),value='',name='text',style=0)
		self.igame = wx.Button(self.azyx,size=(184, 78),pos=(149, 96),label='安装',name='igame')
		igame_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
		self.igame.SetFont(igame_字体)
		self.igame.SetForegroundColour((255, 255, 255, 255))
		self.igame.SetOwnBackgroundColour((124, 205, 124, 255))
		self.igame.Bind(wx.EVT_BUTTON,self.igame_anbdj)
		self.source_bmcl = wx.Button(self.azyx,size=(184, 78),pos=(10, 200),label='选择BMCLAPI镜像源',name='source_bmcl')
		source_bmcl_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
		self.source_bmcl.SetFont(source_bmcl_字体)
		self.source_bmcl.SetForegroundColour((255, 255, 255, 255))
		self.source_bmcl.SetOwnBackgroundColour((124, 205, 124, 255))
		self.source_bmcl.Bind(wx.EVT_BUTTON,self.sourcebmcl_anbdj)
		self.source_mojang = wx.Button(self.azyx,size=(184, 78),pos=(200, 200),label='选择Mojang官方源',name='source_mojang')
		source_mojang_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
		self.source_mojang.SetFont(source_mojang_字体)
		self.source_mojang.SetForegroundColour((255, 255, 255, 255))
		self.source_mojang.SetOwnBackgroundColour((124, 205, 124, 255))
		self.source_mojang.Bind(wx.EVT_BUTTON,self.sourcemojang_anbdj)


	def igame_anbdj(self,event):
		igamever = self.bjk1.GetValue()
		installgame_msg = "开始安装:" + igamever
		installgame_msg2 =  igamever + " 安装完成"
		wx.MessageBox(installgame_msg, "提示" ,wx.OK | wx.ICON_INFORMATION)  
		os.system("java -jar cmcl.jar install " + igamever)
		wx.MessageBox(installgame_msg2, "提示" ,wx.OK | wx.ICON_INFORMATION)  
		
		
	def sourcebmcl_anbdj(self,event):
		os.system("java -jar cmcl.jar config downloadSource 1")
		wx.MessageBox("您已切换下载源为 BMCLAPI", "提示" ,wx.OK | wx.ICON_INFORMATION)  
	
	def sourcemojang_anbdj(self,event):
		os.system("java -jar cmcl.jar config downloadSource 0")
		wx.MessageBox("您已切换下载源为 Mojang", "提示" ,wx.OK | wx.ICON_INFORMATION)  
