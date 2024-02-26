# -*- coding:utf-8 -*-
import wx
from homepage import *
from launchgame import *
from installgame import *
from user import *
import os
import wx.html2


class Launcher(wx.App):
	def  OnInit(self):
		self.frame = homepage()
		self.frame.Show(True)
		return True

if __name__ == '__main__':
	app = Launcher()
	app.MainLoop()
