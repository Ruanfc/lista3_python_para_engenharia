#!/usr/bin/env python3
#### Aqui o shebang do python é importante, pois é minha intenção rodar
#### o programa direto do terminal com argumento
import re
#import sys.argv
from sys import argv

# Executa leitura do arquivo como primeiro argumento e passa a uma string
try:
    arquivo = open(str(argv[1]), 'r')
except:
    arquivo = open('teste.txt', 'r')

texto = arquivo.read() # Passa o texto para uma string

arquivo.close() #fecha o arquivo

# Usa regex para obter o arquivo apenas com letras, underline e espaços
texto = re.sub('[^\w\s]+','', texto )
texto_lista = re.split('\s',texto) #Palavras do texto em uma lista

# Cria set para percorrer sem duplicatas
texto_set = set(texto_lista)
texto_set.remove('') # Remove elemento ''
# Cria o dicionário baseado no set e na lista
texto_dict = { elemento:texto_lista.count(elemento) for elemento in texto_set}

print(texto_dict)
