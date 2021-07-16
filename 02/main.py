import matematica as m

func = [
    [],
    lambda x: m.soma(*x),
    lambda x: m.somav(*x),
    lambda x: m.sub(*x),
    lambda x: m.subv(*x),
    lambda x: m.multi(*x),
    lambda x: m.dot(*x),
    lambda x: m.cross(*x),
    lambda x: m.produto(*x),
    lambda x: m.divisao(*x),
    lambda x: m.power(*x),
    lambda x: m.logaritmo(*x),
    lambda x: m.sind(x),
    lambda x: m.cosd(x),
    lambda x: m.tg(x),
    lambda x: m.sqrt(x),
    lambda x: m.inv(x),
    lambda x: m.ab(x),
    lambda x: m.fatorial(x),
    lambda x: m.permut(*x),
    lambda x: m.comb(*x),
    lambda x: m.primo(x),
    lambda x: m.primosTil(x),
    lambda x: m.MMC(x),
    lambda x: m.MDC(*x),
]


menuString = """Menu Principal:
    0. Sair;
    1. soma;
    2. somav;
    3. sub;
    4. subv;
    5. multi;
    6. dot;
    7. cross;
    8. produto;
    9. divisão;
    10. pow;
    11. logaritmo;
    12. seno(em graus)
    13. cosseno(em graus)
    14. tangente (graus)
    15. sqrt
    16. 1/x
    17. abs
    18. fatorial
    19. permutação
    20. combinação
    21. O número é primo?
    22. Números primos até x
    23. MMC
    24. MDC

    """
menu = len(func)
while 0 < menu <= len(func):
    print(menuString)
    menu = int(input("R.: ")) #Lê o comando do menu e assegura que é inteiro
    if menu == 0:
        break
    # O usuário insere os argumento em uma string
    arguments = str(input("Insira os argumentos separados por vírgula: "))
    # A string é avaliada e levada como argumento para a função catalogada
    print(str(func[menu](eval(arguments))))
