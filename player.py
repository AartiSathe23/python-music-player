from tkinter import *
import time 
from tkinter import filedialog
from pygame import mixer
import os
from PIL import Image,ImageTk,ImageFilter
from datetime import datetime
import pygame
from tkinter import ttk

mixer.init()
pygame.init()
class Player:
    def __init__(self,root):
        self.root=root
        self.root.title("Mp3 Player")
        self.root.geometry('400x450+500+200')
        self.root.configure(bg="cornsilk3")
        self.root.resizable(False,False)
        self.index=0
        self.playlist = []

        lower_frame=Frame(self.root,background="white",width=400,height=80)
        lower_frame.place(x=0,y=220)

        # image_icon=ImageTk.PhotoImage(file="musicplayer.png")
        # root.iconphoto(False,image_icon)

      #   Menu=ImageTk.PhotoImage(file="vinylplayer.jpeg")
      #   Label(self.root,image=Menu).place(x=20,y=20,width=360,height=180,Image.ANTIALIAS)

        Menu_image = Image.open("images/vinylplayer.jpeg")
        Menu_image= Menu_image.resize((360, 180), Image.LANCZOS)
        self.Menu = ImageTk.PhotoImage(Menu_image)
        Label(self.root, image=self.Menu).place(x=20, y=20, width=360, height=180)

        lower2_frame=Frame(self.root,width=400,height=120)
        lower2_frame.place(x=0,y=330)

        scroll = Scrollbar(lower2_frame, orient=VERTICAL)
        self.Playlist = Listbox(lower2_frame, width=100, font=("Times new roman", 10), bg="lightsalmon2", fg="black", selectbackground="steelblue4", cursor="hand2", yscrollcommand=scroll.set)
        scroll.config(command=self.Playlist.yview)
        scroll.pack(side=RIGHT, fill=Y)
        self.Playlist.pack(side=LEFT, fill=BOTH,expand=True)

      #   self.timeline = ttk.Progressbar(self.root, orient="horizontal", length=360,mode="determinate")
      #   self.timeline.place(x=20, y=195)

      #   self.elapsed_time_label = Label(self.root, text="0:00", bg="cornsilk3", fg="black", font=("Arial", 10))
      #   self.elapsed_time_label.place(x=20, y=195)

      #   self.total_duration_label = Label(self.root, text="0:00", bg="cornsilk3", fg="black", font=("Arial", 10))
      #   self.total_duration_label.place(x=340, y=195)
        browse_button=Button(self.root,text="Browse music",font=("Arial",12,"bold"),bg="gray35",fg="gold",bd=2,relief=RIDGE,width=12,cursor="hand2",command=self.AddMusic)
        browse_button.place(x=0,y=300)

        exit_button=Button(self.root,text="Exit",font=("Arial",12,"bold"),bg="gray35",fg="gold",bd=2,relief=RIDGE,width=13,command=self.Exit,cursor="hand2")
        exit_button.place(x=265,y=300) 

        # add_button = Button(self.root, text="Add Song", command=self.AddMusic)
        # add_button.place(x=0, y=270)

        clear_button = Button(self.root, text="Clear Playlist",font=("Arial",12,"bold"),bg="gray35",fg="gold",bd=2,relief=RIDGE,width=13, command=self.ClearPlaylist)
        clear_button.place(x=130, y=300)

        play_btn_image = Image.open("images/play.jpg")
        play_btn_image = play_btn_image.resize((50, 50), Image.LANCZOS)
        self.play_btn = ImageTk.PhotoImage(play_btn_image)
        play = Button(lower_frame, image=self.play_btn, bg="white", bd=0, height=50, width=50, command=self.PlayMusic, cursor="hand2")
        play.place(x=130, y=15)

        pause_btn_image=Image.open("images/pausebtn.png")
        pause_btn_image=pause_btn_image.resize((42,42),Image.LANCZOS)
        self.pause_btn=ImageTk.PhotoImage(pause_btn_image)
        pause=Button(lower_frame,image=self.pause_btn,bg="white",bd=0,height=50,width=50,borderwidth=0,command=self.PauseMusic,cursor="hand2")
        pause.place(x=40,y=15)

        resume_btn_image=Image.open("images/resume.jpg")
        resume_btn_image=resume_btn_image.resize((70,70),Image.LANCZOS)
        self.resume_btn=ImageTk.PhotoImage(resume_btn_image)
        resume=Button(lower_frame,image=self.resume_btn,bg="white",bd=0,height=50,width=50,borderwidth=0,command=self.ResumeMusic,cursor="hand2")
        resume.place(x=220,y=15)

        next_btn_image=Image.open("images/next.jpg")
        next_btn_image=next_btn_image.resize((40,40),Image.LANCZOS)
        self.next_btn=ImageTk.PhotoImage(next_btn_image)
        next=Button(lower_frame,image=self.next_btn,bg="white",bd=0,height=50,width=50,borderwidth=0,command=self.NextMusic,cursor="hand2")
        next.place(x=310,y=15)

    def AddMusic(self):
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            songs = os.listdir(path)

            for song in songs:
                if song.endswith(".mp3"):
                    self.playlist.append(song)
                    self.Playlist.insert(END, song)

    def ClearPlaylist(self):
        self.playlist = []  
        self.Playlist.delete(0, END)  
        
    def PlayMusic(self):
       music_name=self.Playlist.get(ACTIVE)
       print(music_name+"(ACTIVE)")
       mixer.music.load(self.Playlist.get(ACTIVE))
       mixer.music.play()
      #  self.update_timeline()
      #  self.update_time_labels() 

    def PauseMusic(self):
        mixer.music.pause()
    
    def NextMusic(self):
     if self.Playlist.size() > 0:
        self.index += 1
        if self.index >= self.Playlist.size():
            self.index = 0
        
        self.Playlist.selection_clear(0, END)
        self.Playlist.activate(self.index)
        self.Playlist.selection_set(self.index)
        self.PlayMusic()

    def ResumeMusic(self):
        mixer.music.unpause()

    def Exit(self):
       exit()

   #  def volume(self):
   #     self.volume_test=f"volume:{int(self.volume*100)}%"
   #     text=self.font.render(self.volume_text,True,(255,255,255))
   #     self.screen.blit(text,(150,150))

   #  def update_time_labels(self):
   #    current_pos = mixer.music.get_pos() // 1000
   #    minutes, seconds = divmod(current_pos, 60)
   #    self.elapsed_time_label.config(text=f"{minutes}:{seconds:02}")

   #    if mixer.music.get_busy():
   #      self.root.after(1000, self.update_time_labels)

   #  def update_timeline(self):
   #      current_pos = mixer.music.get_pos()  
   #      self.timeline["value"] = current_pos  
   #      total_duration = mixer.Sound(self.Playlist.get(ACTIVE)).get_length()
   #      total_minutes, total_seconds = divmod(int(total_duration), 60)
   #   self.total_duration_label.config(text=f"{total_minutes}:{total_seconds:02}")
root=Tk()
obj=Player(root)
root.mainloop()
