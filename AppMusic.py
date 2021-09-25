from tkinter import *
import tkinter.filedialog 
import pygame
from pygame import *


pygame.init()
janela = Tk()
janela.geometry('800x600')
janela.title("Eduardo")
img = PhotoImage(file="imagem1.png")
img2 = PhotoImage(file="test.png")
img3 = PhotoImage(file="pause.png")
img4 = PhotoImage(file="proximo.png")
img5 = PhotoImage(file="antes.png")
img6 = PhotoImage(file="SAIR (2).png")
img7 = PhotoImage(file="ADC.png")
local_imagem = Label(janela, image=img).pack()
tamanho = 0
musicas=[]
musica = ""
playlist = []
banda = ""
i = 0
z = 0
c = 0
musica_tocando = False
def  Adic():
        global banda
        banda=( tkinter.filedialog.askdirectory(initialdir="C:/Users/"))
def selctMusic():
        global musicas
        musicas =( tkinter.filedialog.askopenfilename(initialdir=banda,
                                                        filetypes=(("Arquivo de audio", ".mp3"), ("All Files", ".*")),
                                                     multiple=True))

        global tamanho
        tamanho = len(musicas)

        for i in range(0,tamanho):
                musica = i
                i = i + 1
        playlist.append(musicas)
        print(playlist)
        

def abc():
        global z
        z +=1
        if musica_tocando == False:
                          command = retornaMusica()
        elif musica_tocando == True:
                        print(musica_tocando)
        else:
                if z==1:
                        command = Play()

def Play():
       
        global musica
        global i
        musica = i
        pygame.mixer.init()
        pygame.mixer.music.load(musicas[musica])
        pygame.mixer.music.play()
        test = Label(janela, text=musicas[musica].split("C:/Users/Eduardo M/Downloads/CD")).place(x=120, y=550)
        musica_tocando = True

#def Pausa():
       
      #  global musica
       # global i
        #global musica_tocando
        #musica = i
        #pygame.mixer.init()
        #pygame.mixer.music.load(musicas[musica])
        #pygame.mixer.music.pause()
        #musica_tocando = False
        #print(musica_tocando)
        
def retornaMusica():
        global musica
        global i
        global musica_tocando
        musica = i
        pygame.mixer.init()
        pygame.mixer.music.load(musicas[musica])
        while pygame.mixer.music.get_busy():
                time.Clock().tick(10)
                for event in event.get():       
                    if event.type == tocar:
                            if musica_tocando: 
                                    pygame.mixer.music.pause()
                                    musica_tocando = False
                            else:
                                    pygame.mixer.music.unpause()
                                    musica_tocando = True
                                    print("Oi")
        
def depois():
        global i
        global c
        i = i + 1
        musica = i 
        pygame.mixer.init()
        pygame.mixer.music.load(musicas[musica])
        pygame.mixer.music.play()
        print(musicas[musica])
        if i == tamanho:
                c = i
                for c in range(0,tamanho):
                        musica = c 
                        pygame.mixer.init()
                        pygame.mixer.music.load(musicas[musica])
                        pygame.mixer.music.play()
                        c = (c + c) - c
                      

def antes():
        global i
        global c
        i = i - 1
        musica = i 
        pygame.mixer.init()
        pygame.mixer.music.load(musicas[musica])
        pygame.mixer.music.play()
        print(musicas[musica])
        if i == 0:
                c = i
                for c in range(0,tamanho):
                        musica = c 
                        pygame.mixer.init()
                        pygame.mixer.music.load(musicas[musica])
                        pygame.mixer.music.play()
                        c = (c - c) + c
                       


Adicionar = Button(janela,image=img7, command=Adic).place(x=10, y=10)
sair = Button(janela, image=img6, command=janela.quit).place(x=730,y=490)
tocar =  Button(janela, image=img3, command=abc).place(x=200, y=485)
prox =  Button(janela, image=img4, command=depois).place(x=250, y=490)
anter =  Button(janela, image=img5, command=antes).place(x=150, y=490)
sele = Button(janela, text="SELECIONAR", command=selctMusic).place(x=10, y=50)

janela.mainloop()
