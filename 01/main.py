import smtplib, ssl

# Procedimento para mandar email
def alerta_email():
    port = 465  # for ssl
    password = input("Escreva sua senha: ")
    fromaddr = "ruan.cartier@ufpe.br"
    toaddrs = ["denki.cartier@gmail.com", "ruankiuby@gmail.com"]
    msg = """Subject: Temperatura da maquina

    A temperatura da maquina atingiu os 40 graus Celsius"""
    msg = "From: %s\nTo: %s\n%s\n\n" % (fromaddr, ", ".join(toaddrs), msg)

    server = smtplib.SMTP_SSL("smtp.gmail.com", port)
    server.login(fromaddr, password)
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


import serial
from time import sleep

# A cada cinco miutos verifica a porta serial
while True:
    ser = serial.Serial(port="/dev/pts/7")  # Substituir a porta serial para uso próprio
    s = int(ser.readline())
    ser.close()
    if s >= 40:
        alerta_email()
    sleep(300)  # Faz leitura da porta serial em um período de pelo menos 5 minutos
