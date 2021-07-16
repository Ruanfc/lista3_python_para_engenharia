#!/usr/bin/env python3
import math

numtipos = ["float", "complex", "int"]
vectipos = ["list", "tuple", "set"]
numtipos = ["<class '" + tip + "'>" for tip in numtipos]
vectipos = ["<class '" + tip + "'>" for tip in vectipos]

tipo = lambda x: str(type(x))
# x é qualquer tipo numérico, ou vetor ou tupla
# y é uma tupla com número indefinido de elementos.
# refer to: https://note.nkmk.me/en/python-args-kwargs-usage/
def soma(x, *y):
    if tipo(x) in vectipos:
        return sum(x) + sum(y)
    else:  # Caso x seja algum tipo numérico
        return x + sum(y)


# Soma de vetores
# para dar certo, tem colocar a saída como lista e inserir tuple ao zip
def somav(x, y):
    zipped = tuple(zip(x, y))
    somavetorial = [xi + yi for xi, yi in zipped]
    return somavetorial


# Subtração escalar
def sub(x, y):
    if tipo(x) in numtipos and tipo(y) in numtipos:
        return x - y
    else:
        raise Exception("Os tipos dos argumentos devem ser numéricos")


# Subtração de vetores
def subv(x, y):
    if tipo(x) in vectipos and tipo(y) in vectipos:
        if len(y) != len(x):
            raise Exception("Os vetores devem ter comprimentos iguais")
        return [xi - yi for xi, yi in tuple(zip(x, y))]
    else:
        raise Exception("Os tipos devem ser lista, tupla, ou set")


# Multiplicação escalar
def multi(x, y):
    if tipo(x) in numtipos and tipo(y) in numtipos:
        return x * y  # Multiplicação entre dois escalares
    elif tipo(x) in numtipos and tipo(y) in vectipos:
        esc = x
        vec = y
    elif tipo(y) in numtipos and tipo(x) in vectipos:
        esc = y
        vec = x
    return [coord * esc for coord in vec]  # Mult. entre escalar e vetor


# Produto interno entre dois vetores
def dot(x, y):
    z = [xi * yi for xi, yi in tuple(zip(x, y))]
    return sum(z)


def cross(x, y):
    if len(x) != 3 or len(y) != 3:
        raise Exception("Os elementos de entrada devem ter comprimento 3")
    else:
        z = []
        z.append(x[1] * y[2])
        z.append(x[2] * y[0])
        z.append(x[0] * y[1])
    return z


# Multiplica cada elemento dado entre si
def produto(x, *y):  # tem que ter pelo menos um argumento
    if not y:  # Checa se a tupla y está vazia
        if tipo(x) in numtipos:
            return x
        else:
            acc = 1
            for xi in x:
                acc = acc* xi
    else:
        if tipo(x) in numtipos:
            acc = x
            for yi in y:
                acc = acc* yi
        else:
            acc = 1
            for xi in x:
                acc = acc* xi
            for yi in y:
                acc = acc* yi
    return acc

#  if tipo(x) in vectipos:
#      return sum(x) + sum(y)
#  else:  # Caso x seja algum tipo numérico
#      return x + sum(y)


#   resultado = 1
#   for var in x:
#       resultado = resultado * var
#   return resultado


def divisao(x, y):
    return x / y


def power(x, y):
    return x ** y


def logaritmo(base, logaritmando):
    return math.log(logaritmando) / math.log(base)


def sind(x):
    return math.sin(math.radians(x))


def cosd(x):
    return math.cos(math.radians(x))


def tg(x):
    return math.tan(math.radians(x))


def sqrt(x):
    return x ** 0.5


def inv(x):
    return 1 / x


def ab(x):
    if x < 0:
        x = -x
    return x


# -------------------------------------------------------
# Vou simplificar minha vida e colocar só inteiros
def fatorial(x):
    if tipo(x) != numtipos[-1]:
        raise Exception("O argumento deve ser inteiro")
    else:
        resultado = 1
        while x > 1:
            resultado = resultado * x
            x = x - 1
        return resultado


# -------------------------------------------------------
# Permutação
def permut(n, p):
    if n < p:
        raise Exception(
            "O primeiro argumento (n) deve ser maior ou igual ao segundo (p)."
        )
    return fatorial(n) / fatorial(n - p)


# Combinação
def comb(n, p):
    if n < p:
        raise Exception(
            "O primeiro argumento (n) deve ser maior ou igual ao segundo (p)."
        )
    return fatorial(n) / (fatorial(n - p) * fatorial(p))


# -------------------------------------------------------
# Procedimentos auxiliares
# Determina se p é divisivel por n
def divifunc(p):
    return lambda n: p % n == 0


# Determina se p é primo
def primo(p):
    divisivel = divifunc(p)
    for j in range(2, (p >> 1) + 1):
        if divisivel(j):
            return False
            break
    return True


# -------------------------------------------------------
# retorna uma lista de primos até x
def primosTil(x):
    primos = []  # Acumula os primos
    k = 2  # Primeiro número a testar se é primo k=2

    while k <= x:
        if primo(k):  # Pergunta se k é primo
            primos.append(k)  # Se o for, adiciona à lista
        k += 1

    return primos[:]  # retorna lista dos primos


# -------------------------------------------------------
# Retorna o MMC da lista números de entrada
def MMC(numeros):
    divisores = []  # Cria lista para armazenar os divisores dos números
    k = 2
    maxiter = max(numeros)
    while k <= maxiter:
        # Se o número for divisível por k, então divide por k e armazena temporariamente
        numeros_buff = []
        for numero in numeros:
            if numero % k == 0:
                numeros_buff.append(numero // k)
            else:
                numeros_buff.append(numero)
        # Se a nova lista for a mesma da lista anterior então muda o valor de k
        if numeros_buff[:] == numeros[:]:
            k = k + 1
        else:  # Senão, adiona k a uma lista
            divisores.append(k)
            numeros = numeros_buff[:]  # Atualiza a linha
        # Agora podemos multiplicar cada elemento do vetor
    return produto(divisores)


#def MDC(numeros):
#    intervalo = range(2, 1 + max(numeros))
#    divisores = [[k for k in intervalo if numero % k == 0] for numero in numeros]
#    # Para achar o MDC é preciso pegar a interseção dos valores e retornar o último
#    divisores = union([set(divisor) for divisor in divisores])
#    mdc = max(divisores)
#    return mdc

def MDC(a,b):
    if tipo(a) == tipo(b) == numtipos[-1]:
        if (b == 0):
            return a
        else:
            return MDC(b, a % b)
    else:
        raise Exception('Os tipos de entada devem ser inteiros.')
