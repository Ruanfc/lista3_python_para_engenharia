from tkinter import *
from PIL import ImageTk, Image
from random import randint

root = Tk()
root.title("Jogo da velha")
root.geometry('300x300')
root.config(bg="white")


#column row
cr = [(0,0), (1,0), (2,0)
     ,(0,1), (1,1), (2,1)
     ,(0,2), (1,2), (2,2)]

# Carrega e redimensiona as imagens
batsu = ImageTk.PhotoImage(Image.open("batsu.png").resize((50,50), Image.ANTIALIAS))
maru = ImageTk.PhotoImage(Image.open("maru.png").resize((50,50), Image.ANTIALIAS))
none = ImageTk.PhotoImage(Image.open("none.png").resize((50,50), Image.ANTIALIAS))

def printTk(string):
    try:
        global label
        label.grid_remove()
    except:
        pass
    label = Label(root, text=string, bg = "white")
    label.grid(columnspan=3)

vencedor = ""
fields = []


def mark_symbol(_index, _symbol):
    global symbol
    global fields
    global vencedor
    if vencedor != "":
        printTk(vencedor +" é o vencedor")
        return
    print(str(_index))
    fields[_index].configure(image = _symbol)
    fields[_index].image = _symbol
    #Verificar se o jogador venceu ## Corrigir field.image
    marked_symbol = [] 
    for field in fields:
        if field.cget('image') == str(_symbol):
            marked_symbol.append(fields.index(field))

    column_verify = [_marked % 3 for _marked in marked_symbol]
    print("column_verify = " + str(column_verify))
    isColumn = False
    for i in range(3):
        if column_verify.count(i) == 3:
            isColumn = True

    row_verify = [_marked // 3 for _marked in marked_symbol]
    print("row_verify = " + str(row_verify))
    isRow = False
    for i in range(3):
        if row_verify.count(i) == 3:
            isRow = True

    print(marked_symbol)
    isDiag = False
    if set(marked_symbol).issuperset({0,4,8}) or set(marked_symbol).issuperset({2,4,6}):
        isDiag = True
    print("_symbol is " + str(_symbol))
    if isColumn or isRow or isDiag:
        if str(_symbol) == "pyimage1":
            vencedor = "Batsu"
        elif str(_symbol) == "pyimage2":
            vencedor = "Maru"
        printTk(vencedor + " é o Vencedor")

    elif _symbol == batsu:
        symbol = maru
        printTk("É a vez de Maru")
    else:
        symbol = batsu
        printTk("É a vez de Batsu")

mark = lambda : mark_symbol(index,symbol)
def mark_func(_ind):
    global symbol
    # Literaliza o index
    return lambda : mark_symbol(_ind,symbol)

# Ajeita os botões no grid
for index in range(len(cr)):
    _botao = Button(root
            ,bg="white", height = 50, width = 50, image=none
            ,command = mark_func(index))
            #,command = lambda : mark_func(index, symbol))
            #,command = mark)
    fields.append(_botao)
    # print(str(index))
    fields[-1].grid(column=cr[index][0], row=cr[index][1])


dado = randint(0,1)
if dado == 1:
    ## Começa o jogador O
    symbol = maru
    printTk("É a vez de Maru")
else:
    ## Começa o jogador X
    symbol = batsu
    printTk("É a vez de Batsu")

root.mainloop()
