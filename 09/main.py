#!/usr/bin/env python3

# mensalidade é a prestação
# atraso é o atraso em dias
def valorPagamento(mensalidade, atraso):
    if atraso <= 0:
        return mensalidade
    else:
        return 1.03*mensalidade + 0.001*atraso

info = []
while(True):
    e = input("Prestação e atraso separados por espaço: ")
    if e == "sair" or e == "quit" or e == "exit" or e=="0":
        break
    dados = e.split()
    if len(dados) > 2:
        print("Use apenas um espaço para inserir dados")
        continue
    try:
        _setelement = (float(dados[0]), int(dados[1]))
        info.append(_setelement)
    except ValueError:
        print("O valores deve ser float e int respectivamente")
    except IndexError:
        print("Use um espaço entre a prestação e o atraso")

print("-"*10)
print("Relatório do dia".center(24, "-"))
print("As prestação pagas no dia foram:")
count = 0
soma = 0
for prest, dias in info:
    count = count + 1
    valor = valorPagamento(prest,dias)
    print("*** Prestação de R${:.2f};".format(valor))
    soma = soma + valor
print("Totalizando R${:.2f}".format(soma))
