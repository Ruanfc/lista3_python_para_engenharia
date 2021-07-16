#!/usr/bin/env python3
#Gera um ipsum lorem com o nome de 'lorem.txt' no diretório
import lorem
t = ''
for i in range(100):
    t = t + lorem.text()
arquivo = open('lorem.txt', 'w')
arquivo.write(t) # Escreve o ipsum lorem no arquivo
arquivo.close() # Fecha o arquivo

