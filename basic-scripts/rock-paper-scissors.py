from random import randint

def jogada(playerChoice):
    moves = ["pedra", "papel", "tesoura"]
    pcChoice = moves[randint(0, 2)]
    if (
        playerChoice == moves[0] and pcChoice == moves[2]
        ) or (
            playerChoice == moves[1] and pcChoice == moves[0]
            ) or (playerChoice == moves[2] and pcChoice == moves[1]):
        return print(f"PARABÉNS, VOCÊ GANHOU! EU ESCOLHI {pcChoice.upper()}")
    elif playerChoice == pcChoice:
        return print(f"EITA, EMPATAMOS! EU TAMBÉM ESCOLHI {pcChoice.upper()}")
    else:
        return print(f"PERDEU, EU ESCOLHI {pcChoice.upper()}")
    
print("--- PEDRA, PAPEL OU TESOURA ---")
playerChoice = str(input("Digite a sua jogada: ").lower())

jogada(playerChoice)
