numero = int( input("Digite um número inteiro: ") )

adjacente = False
digito = numero

while digito > 0 and not adjacente:
    d1 = digito % 10
    d2 = (digito % 100) // 10
    if d1 == d2:
        adjacente = True

    digito = digito // 10

if adjacente:
    print("sim")
else:
    print("não")