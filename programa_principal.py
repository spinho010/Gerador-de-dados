from tkinter import *
import os

janela = Tk()
janela.geometry('400x500')
janela.title('GERADOR DE DADOS')
janela.configure(background='#001')

txt1 = Label(janela, text='CPF: ', font='Bold 13', background='#001', foreground='#fff')
txt1.place(x=15, y=40)

cpf = Entry(janela)
cpf.place(x=65, y=40, width=250)


janela.mainloop()