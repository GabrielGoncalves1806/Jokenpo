from random import choice
import PySimpleGUI as sg

#Definir Variáveis
images = ['Rock.png','Paper.png','Shears.png']
jokenpo = ['Rock.png','Paper.png','Shears.png']
player = ''
result = ''
#Definir Janelas

def name():
    layout = [
        [sg.Text('Nome: '),sg.Input(key='name',size=(20,1))],
        [sg.Button('Ok')]
        ]
    win_name = sg.Window('Login',layout)
    event, value = win_name.Read()
    nome = value['name']
    if event == 'Ok' or sg.WIN_CLOSED:
        win_name.close()
    return nome
nome = name()

def animation():
    layout_anim = [
                 [sg.Text(nome),sg.Text('                        '), sg.Text('COMPUTER')],
                 [sg.Image(player), sg.Text('X'),sg.Image(pc)],
                 [sg.Text(result)],
                 ]

    anim = sg.Window('Jokenpô',layout_anim)
    event, value = anim.Read()
    if event == sg.WIN_CLOSED:
        anim.close()
#Definir lógica das rodadas

while True:
    pc = choice(jokenpo)

    layout_menu = [
                 [sg.Text(f'Nome: {nome}')],
                 [sg.Button('Pedra'), sg.Button('Papel'), sg.Button('Tesoura')]
                 ]
    main = sg.Window('Jokenpô',layout_menu)
    event, value = main.Read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Pedra':
        player = 'Rock.png'
        main.close()
    elif event == 'Papel':
        player = 'Paper.png'
        main.close()
    else:
        player = 'Shears.png'
        main.close()
    
    #Vitórias
    if event == 'Pedra' and pc == 'Shears.png':
        result = 'VOCÊ VENCEU'
        animation()
    elif event == 'Papel' and pc == 'Rock.png':
        result = 'VOCÊ VENCEU'
        animation()
    elif event == 'Tesoura' and pc == 'Paper.png':
        result = 'VOCÊ VENCEU'
        animation()

    #Derrotas
    if event == 'Pedra' and pc == 'Paper.png':
        result = 'VOCÊ PERDEU'
        animation()
    elif event == 'Papel' and pc == 'Shears.png':
        result = 'VOCÊ PERDEU'
        animation()
    elif event == 'Tesoura' and pc == 'Rock.png':
        result = 'VOCÊ PERDEU'
        animation()
    #Empate
    if event == 'Pedra' and pc == 'Rock.png':
        result = 'EMPATE'
        animation()
    elif event == 'Papel' and pc == 'Paper.png':
        result = 'EMPATE'
        animation()
    elif event == 'Tesoura' and pc == 'Shears.png':
        result = 'EMPATE'
        animation()

    

    
        
    


















