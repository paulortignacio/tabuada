import os
import time

def limpar():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    print("==============================================")
    print("|       Programa de Cálculo de Tabuada       |")
    print("==============================================")
    try:
        numero = int(input("Digite um número para calcular a tabuada: "))
    except:
        print("Digite um número válido!")
        time.sleep(2)
        continue
    print(f"A tabuada do {numero} é:")
    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1
    saida = input("Deseja continuar? (S/N)").upper()
    if saida == "N":
        print("Encerrando o programa... ")
        time.sleep(1)
        limpar()
        break

    else:
        print("Reiniciando o programa...")
        time.sleep(0.5)
        limpar()