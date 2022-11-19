meuCartao = int(input("Digite o número de seu cartão de crédito: "))

cartaoLido = 1
encontreiCartaoNaLista = False

while cartaoLido != 0 and not encontreiCartaoNaLista:
    cartaoLido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaoLido == meuCartao :
        encontreiCartaoNaLista = True

if encontreiCartaoNaLista:
    print("Meu cartão está na lista lida.")
else:
    print("Meu cartão NÃO está na lista lida.")
