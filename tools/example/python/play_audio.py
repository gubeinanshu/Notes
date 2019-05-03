#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
大概下面这样子,注意要安装第三方库的。
Add：添加文件，只能一个一个加 Play：开始播放 Pause：暂停 Next：下一首
"""
import tkinter
import tkinter.filedialog
from win32com.client import Dispatch
class Window:
    def __init__(self):
        self.root = root =tkinter.Tk()
        buttonAdd = tkinter.Button(root, text='Add', command=self.add)
        buttonAdd .place(x=150, y=15)
        buttonPlay = tkinter.Button(root, text='Play', command=self.play)
        buttonPlay.place(x=200, y=15)
        buttonPause = tkinter.Button(root, text='Pause', command=self.pause)
        buttonPause.place(x=250, y=15)
        buttonStop = tkinter.Button(root, text='Stop', command=self.stop)
        buttonStop.place(x=300, y=15)
        buttonNext = tkinter.Button(root, text='Next', command=self.next)
        buttonNext.place(x=300, y=15)

        frame = tkinter.Frame(root, bd=2)
        self.playList = tkinter.Text(frame)
        scrollbar = tkinter.Scrollbar(frame)
        scrollbar.config(command=self.playList.yview)
        self.playList.pack(side=tkinter.LEFT)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        frame.place(y=50)
        self.wmp = Dispatch('WMPlayer.OCX')
    def MainLoop(self):
        self.root.minsize(510, 380)
        self.root.maxsize(510, 380)
        self.root.mainloop()
    def add(self):
        file = tkinter.filedialog.askopenfilename(title='Python Music Player',
                                                  filetypes=[('MP3', '*.mp3'), ('WMA', '*.wma'), ('WAV', '*.wav')])
        if file:
            media = self.wmp.newMedia(file)
            self.wmp.currentPlaylist.appendItem(media)
            self.playList.insert(tkinter.END, file + '\n')

    def play(self):
        self.wmp.controls.play()
    def pause(self):
        self.wmp.controls.pause()
    def stop(self):
        self.wmp.controls.stop()
    def next(self):
        self.wmp.controls.next()
window = Window()
window.MainLoop()