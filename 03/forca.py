from tkinter import *
from PIL import ImageTk, Image
import os

#Palavra secreta
#-----------------------------------------------------------------------------------------------
palavra = input("Escreva a palava secreta: ")
letras = '_'*len(palavra) # Mistério a ser revelado
#-----------------------------------------------------------------------------------------------

root = Tk()
root.title("Jogo da forca")
root.geometry('300x300')
root.config(bg="white")

#Imagem
forca = [ ImageTk.PhotoImage(Image.open("forca-{}.gif".format(str(num)))) for num in range(16) ]
count = int(0)
panel = Label(root, image = forca[count])
panel.grid(row=0, column= 0, columnspan=3)


#Preciso melhorar isso. Código repetido. HELP!
def letras_handler(string):
    try:
        global label_letras
        label_letras.grid_remove()
    except:
        pass
    label_letras = Label(root, text=string, bg = "white")
    label_letras.grid(columnspan=3)


# Cria uma entrada para o texto
e = Entry(root, borderwidth = 5)
e.grid(row=1, column = 0, columnspan=2)

# Criação de labels de aviso
def label_handler(string):
    # Caso a pessoa tenha acertado joga a resposta na tela
    global letras
    if string == "Acertou":
        letras = palavra
    # Elimina as labels da tela
    try:
        global label
        label.grid_remove()
        global letras_label
        letras_label.grid_remove()
    except:
        pass
    label = Label(root, text=string, bg = "white")
    label.grid(columnspan=3)
    letras_label = Label(root, text=letras.replace("", " ")[1:-1], bg = "white")
    letras_label.grid(columnspan=3)
    
    # Apaga a string da entrada
    e.delete(0,END)

# print para o tkinter
printTk = lambda entry_string : label_handler(entry_string)

# From xournal
def input_text(entrada):
    global label
    global count
    if count >= 14:
        letra_errada = 'GAME OVER'
    else:
        letra_errada = 'Letra errada!'
    if len(entrada) == 1:
        insert_char(entrada)
        printTk('') if entrada in palavra else printTk(letra_errada)
    elif len(entrada) == len(palavra):
        printTk('Acertou') if entrada == palavra else printTk('Errou!')
        # print('Acertou') if entrada == palavra else print('Errou!')
    else:
        # print('Número de letras inapropriado')
        printTk('No. de letras inapropriado')

def str_assign(string, index, char):
    s = list(string)
    s[index] = char
    return "".join(s)

# Insert char from xournal
def insert_char(letra):
    global count
    global letras
    characters = list(palavra)
    indexes = []
    check = False
    for index, character in enumerate(characters):
        if (character == letra):
            indexes.append(index) # junta os endereços
            #letras[index] = letra
            letras = str_assign(letras, index, letra)
            check = True
    if not check:
        if count < len(forca) - 1:
            count = count +1
        print("count = " + str(count))
        trocarImagem(count)

# trocarImagem colocar a imagem de acordo com o inteiro indicado
def trocarImagem(endereco):
    panel.configure(image = forca[endereco])
    panel.image = forca[int(endereco)]
    

# Lamda command to get text from entry
get_text = lambda : input_text(e.get())
get_bind = lambda event : input_text(e.get())

# Cria um bind para executar a rotina input_text
root.bind('<Return>', get_bind)

# Botão para submeter a string
button = Button(root, text = "Submeter", command = get_text)
button.grid(row=1, column = 2)


root.mainloop()
