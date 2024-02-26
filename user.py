# -*- coding:utf-8 -*-
import wx
import os

class user(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title='用户', size=(500, 400),name='user',style=541072896)
		icon = wx.Icon(r'./logol.png')
		self.SetIcon(icon)
		self.user = wx.Panel(self)
		self.user.SetOwnBackgroundColour((255, 245, 196, 255))
		self.Centre()
		self.bq1 = wx.StaticText(self.user,size=(399, 22),pos=(51, 7),label='输入您要添加的账号（离线，建议记录添加账号的号数，比如0=1,1=2...)',name='staticText',style=2321)
		self.bq1.SetOwnBackgroundColour((255, 245, 196, 255))
		self.addname = wx.TextCtrl(self.user,size=(265, 32),pos=(109, 42),value='',name='text',style=0)
		self.an1 = wx.Button(self.user,size=(60, 41),pos=(207, 89),label='添加',name='button')
		an1_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
		self.an1.SetFont(an1_字体)
		self.an1.SetForegroundColour((255, 255, 255, 255))
		self.an1.SetOwnBackgroundColour((124, 205, 124, 255))
		self.an1.Bind(wx.EVT_BUTTON,self.an1_anbdj)
		self.bq2 = wx.StaticText(self.user,size=(398, 25),pos=(43, 142),label='输入要添加的账号的号数',name='staticText',style=2321)
		self.bjk2 = wx.TextCtrl(self.user,size=(270, 33),pos=(107, 175),value='',name='text',style=0)
		self.an2 = wx.Button(self.user,size=(66, 49),pos=(206, 221),label='确定',name='button')
		an2_字体 = wx.Font(12,74,90,400,False,'Microsoft YaHei UI',28)
		self.an2.SetFont(an2_字体)
		self.an2.SetForegroundColour((255, 255, 255, 255))
		self.an2.SetOwnBackgroundColour((124, 205, 124, 255))
		self.an2.Bind(wx.EVT_BUTTON,self.an2_anbdj)


	def an1_anbdj(self,event):
		adduseroffline = self.addname.GetValue()
		os.system("java -jar cmcl.jar account --login=offline --name=" + adduseroffline)


	def an2_anbdj(self,event):
		setuser = self.bjk2.GetValue()
		os.system("java -jar cmcl.jar account -s " + setuser)

