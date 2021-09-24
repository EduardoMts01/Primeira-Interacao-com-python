from tkinter import *
import tkinter.filedialog
import pygame

pygame.init()
janela = Tk()
janela.geometry('800x600')
janela.title("Eduardo")
img = PhotoImage(file="imagens/imagem1.png")
img2 = PhotoImage(file="imagens/test.png")
img3 = PhotoImage(file="imagens/pause.png")
img4 = PhotoImage(file="imagens/proximo.png")
img5 = PhotoImage(file="imagens/antes.png")
img6 = PhotoImage(file="imagens/SAIR (2).png")
img7 = PhotoImage(file="imagens/ADC.png")
local_imagem = Label(janela, image=img).pack()
tamanho = 0
musicas=[]
musica = ""
playlist = []
i = 0
def  Adic():
        global musicas
        musicas =( tkinter.filedialog.askopenfilename(initialdir="C:/Users/",
                                                        filetypes=(("Arquivo de audio", ".mp3"), ("All Files", ".*")),
                                                     multiple=True))

        global tamanho
        tamanho = len(musicas)

        for i in range(0,tamanho):
                musica = i
                i = i + 1
        playlist.append(musicas)
        print(playlist)

def Play():
        print(musicas[1])
        global musica
        global i
        musica = i
        pygame.mixer.init()
        pygame.mixer.music.load(musicas[musica])
        pygame.mixer.music.play()
        print(musicas[musica])
                #i = i + 1
        print(tamanho)
        test = Label(janela, text=musicas[musica].split("C:/Users/Eduardo M/Downloads/CD")).place(x=120, y=550)

def depois():
        global i
        i = i + 1
        musica = i 
        pygame.mixer.init()
        pygame.mixer.music.load(musicas[musica])
        pygame.mixer.music.play()
        print(musicas[musica])
        #print(music1)
    #print(musicaAtual,"Essa é a música atual")
def antes():
        global i
        i = i - 1
        musica = i 
        pygame.mixer.init()
        pygame.mixer.music.load(musicas[musica])
        pygame.mixer.music.play()
        print(musicas[musica])
def abc():
        print("Eduardo")

Adicionar = Button(janela,image=img7, command=Adic).place(x=10, y=10)
sair = Button(janela, image=img6, command=janela.quit).place(x=730,y=490)
cmd =  Button(janela, image=img3, command=Play).place(x=200, y=485)
prox =  Button(janela, image=img4, command=depois).place(x=250, y=490)
anter =  Button(janela, image=img5, command=antes).place(x=150, y=490)


janela.mainloop()
