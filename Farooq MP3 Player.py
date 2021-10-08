#project music player

from tkinter import Listbox, font
from tkinter.constants import CURRENT
import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os

musicplayer = tkr.Tk()
musicplayer.title("Farooq MP3 Player")
musicplayer.geometry('450x450')

directory = askdirectory()
os.chdir(directory)
songlist = os.listdir()
playlist = tkr.Listbox(musicplayer, font = 'Cambria 14 bold', bg='#fff385', selectmode = tkr.SINGLE)

for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def exitmusicplayer():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

# def prevSong():
#     currentIndex
#     lastSong = prevSonglist[currentIndex]
#     pygame.mixer.music.load(lastSong)

# def nextsong():
#     currentIndex++
#     nextsong = songlist[currentIndex]
#     pygame.mixer.music.load(nextsong)


button_play = tkr.Button(musicplayer, height=3, width=5, text='Play Music', font='Cambria 14 bold', command=play, bg='#59c5ff', fg = 'black')
button_paus = tkr.Button(musicplayer, height=3, width=5, text='Pause Music', font='Cambria 14 bold', command=pause, bg='#ff3636', fg = 'black')
button_resu = tkr.Button(musicplayer, height=3, width=5, text='Resume Music', font='Cambria 14 bold', command=resume, bg='#9999FF', fg = 'black')
button_stop = tkr.Button(musicplayer, height=3, width=5, text='Stop Music', font='Cambria 14 bold', command=exitmusicplayer, bg='#66FFCC', fg = 'black')

button_play.pack(fill='x')
button_paus.pack(fill='x')
button_resu.pack(fill='x')
button_stop.pack(fill='x')

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font='Cambria 12 bold', textvariable=var)
playlist.pack(fill='both', expand='yes')
songtitle.pack()

musicplayer.mainloop() 