numero = int(input("Digite um número inteiro: "))

divisor = 2
indicadorPrimo = True

while divisor < numero and indicadorPrimo:
    if numero % divisor == 0:
        indicadorPrimo = False
    divisor += 1

if indicadorPrimo:
    print("primo")
else:
    print("não primo")