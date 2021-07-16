#!/usr/bin/env python3

import dbm  # Banco de dados simples
import re

# Declarações auxiliares
_nome_ = "Nome:"
_telefone_ = "Telefone:"
_email_ = "Email:"
_endereco_ = "Endereco:"
toStr = lambda byte: byte.decode("utf-8")  # Usado para transformar bytes em string

# -------------------------------------------------------------------------
# Procedimentos auxiliares


def registrar():  # Registra os dados de um novo contato, sobrescreve se houver
    print("Registrando contato:")
    nome = input(_nome_ + " ")
    telefone = input(_telefone_ + " ")
    email = re.sub("\,", ".", input(_email_ + " "))
    endereco = re.sub("\,", ".", input(_endereco_ + " "))
    info = _telefone_ + telefone + ", " + _email_ + email + ", " + _endereco_ + endereco
    #db[nome] = info
    _w_(nome,info)


def apagar():  # Remove contato respectivo ao nome dado
    print("Apagando contato:")
    nome = input(_nome_ + " ")
    confirmacao = input("Tem certeza? (s/n)")
    if confirmacao == "s":
        #del db[nome]
        _d_(nome)


def consultar():  # Consulta a situação de um dado contato com seu IMC
    print("Consultando situação de contato:")
    nome = input(_nome_ + " ")
    try:
        #info = str(db.get(nome))
        info = toStr(_r_(nome))
    except ValueError:
        return
    print(info)


def list_contato(extremo):
    buffemail = []
    buffnome = []
    buffendereco = []
    db = dbm.open(file="data", flag="c")
    k = db.firstkey()
    db.close()
    while k != None:
        nome = toStr(k)
        telefone, email, endereco = toStr(_r_(nome)).split(", ")  # Coleta as informações
        buffemail.append(email)
        buffnome.append(nome)
        buffendereco.append(endereco)

        db = dbm.open(file="data", flag="c")
        k = db.nextkey(k)
        db.close() # Fecha o arquivo
    # Escreve todos os contatos
    if extremo == 4:
        print(buffnome)
        return

# Escrita de dados com dbm
def _w_(key, string):
    # Abre o arquivo de dados
    db = dbm.open(file="data", flag="c")
    db[key] = string
    db.close()

# Leitura de dados com dbm
def _r_(key):
    # Abre o arquivo de dados
    db = dbm.open(file="data", flag="c")
    __string =  db[key]
    db.close()
    return __string

# Limpa de dados com dbm
def _d_(key):
    # Abre o arquivo de dados
    db = dbm.open(file="data", flag="c")
    del db[key]
    db.close()



menuString = """Menu Principal:
    0. Sair;
    1. Registrar/Atualizar contato;
    2. Apagar contato;
    3. Consultar contato;
    4. Imprime os nomes de cada contato;
    """
menu = -1
while menu != 0:
    print(menuString)
    menu = int(input("R.: "))
    if menu == 1:
        registrar()
    elif menu == 2:
        apagar()
    elif menu == 3:
        consultar()
    elif menu == 4:
        list_contato(menu)

# Melhorias a serem feitas
# Deixar arquivo apenas quando for realizar leitura ou escrita, é mais seguro.
