#!/usr/bin/env python3

info = dict()
while(True):
    e = input("Insira nome e idade separador por espaço: ")
    if e == "sair" or e == "quit" or e == "exit":
        break
    dados = e.split()
    if len(dados) > 2:
        print("Use apenas um espaço para inserir dados")
        continue
    try:
        info.update({dados[0]:int(dados[1])})
    except ValueError:
        print("A idade deve ser um número inteiro")
    except IndexError:
        print("Use um espaço entre o nome e a idade")

### Agora podemos criar as duas listas
under30 = [pessoa for pessoa, idade in info.items() if idade < 30]
over30 = [pessoa for pessoa, idade in info.items() if idade >= 30]

print("under30 = " + str(under30))
print("over30 = " + str(over30))
