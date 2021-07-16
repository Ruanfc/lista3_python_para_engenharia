#!/usr/bin/env python3
import fileinput

def checkpoint(page,tipo='a'):
    output = open("output.txt", tipo)
    output.write(f"\n-------- PAGE {page} --------\n")
    output.close()

def record(string, tipo='a'):
    output = open("output.txt", tipo)
    output.write(string)
    output.close()

# Zera o arquivo
record("------ Arquivo lorem.txt paginado -----\n", 'w')

new_string = ""
for count, line in enumerate(fileinput.input(['lorem.txt'])):
    if count % 60 == 0:
        checkpoint(int(count % 60 +1 ))

    # Adiciona o resto da linha anterior
    line = new_string.replace('\n', '') + ' ' + line
    if len(line) > 76: # Se a linha tiver mais de 76 chars
        # Quebra a linha no último espaço
        address = line.rfind(' ') 
        new_string = line[address +1 :]
        line = line[:address] + '\n'
        record(line) #Joga nova linha para o arquivo
