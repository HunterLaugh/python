# coding:utf-8

from tkinter import *


class Application(Frame):
	def _init_(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.createWidgets()
		
	def createWidgets(self):
		self.helloLabel=Label(self,text='Hello, world!')
		self.helloLabel.pack()
		self.quitButton=Button(self, text='Quit',command=self.quit)
		self.quitButton.pack()

#　实例化		
app=Application()

# 设置窗口标题
app.master.title('Hello World')

app.mainloop()
