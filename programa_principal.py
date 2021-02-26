from tkinter import *
from defs import *
import os

def generate():
    try:
        n1 = (randint(100, 999))
        n2 = (randint(100, 999))
        n3 = (randint(100, 999))
        n4 = (randint(10, 99))
        print(f'CPF GERADO COM SUCESSO! {n1}.{n2}.{n3}-{n4}')
    except:
        print('HOUVE UM ERRO!')
    else:
        cpf1 = Label(janela, text=f'{n1}.{n2}.{n3}-{n4}', font='Arial 13', background='#fff', foreground='black')
        cpf1.place(x=58, y=40)



janela = Tk()
janela.geometry('400x500')
janela.title('GERADOR DE DADOS')
janela.configure(background='#fff')

txt1 = Label(janela, text='CPF: ', font='Arial 13', background='#fff', foreground='black')
txt1.place(x=15, y=40)

txt2 = Label(janela, text='RG: ', font='Arial 13', background='#fff', foreground='black')
txt2.place(x=15, y=85)

botao = Button(janela, text='GERAR',command=generate, font='Bold 10', background='#fff', foreground='#008', width=18)
botao.place(x=15, y=150)

janela.mainloop()