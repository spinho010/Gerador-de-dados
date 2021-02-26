from tkinter import *
import os

janela = Tk()
janela.geometry('400x500')
janela.title('GERADOR DE DADOS')
janela.configure(background='#fff')

txt1 = Label(janela, text='CPF: ', font='Arial 13', background='#fff', foreground='black')
txt1.place(x=15, y=40)

txt2 = Label(janela, text='RG: ', font='Arial 13', background='#fff', foreground='black')
txt2.place(x=15, y=85)

botao = Button(janela, text='GERAR', font='Bold 10', background='#fff', foreground='#008', width=18)
botao.place(x=15, y=150)

janela.mainloop()