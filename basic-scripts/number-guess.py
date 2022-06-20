from random import randint

pcNumber = randint(1, 10)

print("--- ACERTE O NÚMERO ---")
playerNumber = int(input("Advinhe um número de 1 a 10: "))

if playerNumber == pcNumber:
    print("PARABÉNS, VOCÊ ACERTOU!")
else:
    print(f"VOCÊ ERROU, EU ESCOLHI {pcNumber}. TENTE NOVAMENTE.")
