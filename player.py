import os
from tkinter import *
from tkinter import font
from random import randrange
import pygame
from pygame import mixer

mixer.init()  # initialize pygame mixer
root = Tk()
root.title("Music Player")
root.iconbitmap(r'icon.ico')
root.geometry("500x300")
root.resizable(0, 0)  
mixer.music.set_volume(0.8)
re = 1
arr = os.listdir("songs")


def p():  # Function to play song
    print((playlist.get(ACTIVE)))

    pygame.mixer.music.load("songs/"+playlist.get(ACTIVE)+".mp3")
    pygame.mixer.music.play(loops=0)


def pa():  # Function to pause/play song
    global re
    if(re == 0):
        mixer.music.unpause()
        re = 1
    else:
        mixer.music.pause()
        re = 0


def s():  # Function to stop song
    mixer.music.stop()


def n():  # Function to play next song
    v = playlist.curselection()

    ss = playlist.get(v[0]+1)

    pygame.mixer.music.load("songs/"+ss+".mp3")
    pygame.mixer.music.play(loops=0)

    playlist.selection_clear(0, END)
    playlist.activate(v[0]+1)
    playlist.selection_set(v[0]+1, last=None)
    playlist.see(v[0]+1)


def pr():  # Function to play previous song
    v = playlist.curselection()

    ss = playlist.get(v[0]-1)

    pygame.mixer.music.load("songs/"+ss+".mp3")
    pygame.mixer.music.play(loops=0)

    playlist.selection_clear(0, END)
    playlist.activate(v[0]-1)
    playlist.selection_set(v[0]-1, last=None)
    playlist.see(v[0]-1)

num=["#422040","#255F85","#E9724C","#F38375","#031D44","#F0372D"]
jj=randrange(6)
# create Playlist window
playlist = Listbox(root, bg=num[jj], fg="#E5F4E3",
                   width=80, font=("Rockwell", 15))
playlist.pack()
for track in arr:
    track = track[0:len(track)-4]
    playlist.insert(END, track)
buttons_frame = Frame(root)
buttons_frame.pack()

# Create buttons
play = Button(buttons_frame, text="Play", bg="black", fg="white", padx=15, pady=5, font=("Rockwell", 15),
              command=p, borderwidth=0.5)
pause = Button(buttons_frame, text="Pause/Play", bg="black", fg="white", padx=10, pady=5, font=("Rockwell", 15),
               command=pa, borderwidth=0.5)
stop = Button(buttons_frame, text="Stop", bg="black", fg="white", padx=10, pady=5, font=("Rockwell", 15),
              command=s, borderwidth=0.5)

prev = Button(buttons_frame, text="Prev", bg="black", fg="white", padx=10, pady=5, font=("Rockwell", 15),
              command=pr, borderwidth=0.5)
nextt = Button(buttons_frame, text="Next", bg="black", fg="white", padx=10, pady=5, font=("Rockwell", 15),
               command=n, borderwidth=0.5)
prev.grid(row=1, column=0)
play.grid(row=1, column=1)
pause.grid(row=1, column=2)
nextt.grid(row=1, column=3)
stop.grid(row=1, column=4)
root.mainloop()

#Made By Saksham Tomar