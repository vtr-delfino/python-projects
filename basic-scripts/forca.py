def strToList(word):
    word = list(word)
    return word


def validade(letter, word):
    pos = []
    for i in word:
        if letter == i:
            pos.append(i)
        else:
            pos = 0
    if pos == 0:
        return 


word = str(input("Digite uma palavra para jogar: ")).lower()
strToList(word)

letter = str(input("Tente acertar uma letra: ")).lower()
validade(letter, word)
