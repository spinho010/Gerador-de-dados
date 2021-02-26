from tkinter import *
from random import randint

#função para gerar os dados
def generate():
    try:
        n1 = (randint(100, 999))
        n2 = (randint(100, 999))
        n3 = (randint(100, 999))
        n4 = (randint(10, 99))
        n5 = (randint(10, 99))
        n6 = (randint(100, 999))
        n7 = (randint(100, 999))
        n8 = (randint(1, 9))
        print(f'CPF GERADO COM SUCESSO! {n1}.{n2}.{n3}-{n4}')
        print(f'RG GERADO COM SUCESSO! {n5}.{n6}.{n7}.{n8}')
    except:
        print('HOUVE UM ERRO!')
    else:
        cpf1 = Label(janela, text=f'{n1}.{n2}.{n3}-{n4}', font='Arial 18', background='#fff', foreground='black')
        cpf1.place(x=70, y=40)

        rg1 = Label(janela, text=f'{n5}.{n6}.{n7}-{n8}', font='Arial 18', background='#fff', foreground='black')
        rg1.place(x=70, y=85)


#configurações da jenala
janela = Tk()
janela.geometry('400x500')
janela.title('GERADOR DE DADOS')
janela.configure(background='#008')
#configurações da jenala

#Primeira escrita na Tela
txt1 = Label(janela, text='CPF:.. ', font='Arial 18', background='#fff', foreground='black')
txt1.place(x=15, y=40)
#Primeira escrita na Tela

#Segunda escrita na Tela
txt2 = Label(janela, text='RG:.. ', font='Arial 18', background='#fff', foreground='black')
txt2.place(x=15, y=85)
#Segunda escrita na Tela

#Botão que vai acionar a def ou função
botao = Button(janela, text='GERAR',command=generate, font='Bold 15', background='#fff', foreground='#008', width=18)
botao.place(x=15, y=150)

#loop para janela permanecer aberta
janela.mainloop()
#fim