numero = int( input("Digite um número inteiro: ") )

soma = 0
digito = numero

while digito > 0 :
    soma = soma + digito % 10
    digito = digito // 10

print(soma)