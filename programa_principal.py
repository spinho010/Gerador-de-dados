from tkinter import *
import os

janela = Tk()
janela.geometry('400x500')
janela.title('GERADOR DE DADOS')
janela.configure(background='#001')

txt1 = Label(janela, text='CPF: ', font='Bold 13', background='#001', foreground='#fff')
txt1.place(x=15, y=40)

txt2 = Label(janela, text='RG: ', font='Bold 13', background='#001', foreground='#fff')
txt2.place(x=15, y=85)

janela.mainloop()