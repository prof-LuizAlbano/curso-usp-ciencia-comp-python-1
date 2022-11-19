print("Soma dos digitos de um número")

numero = int( input("Digite um número inteiro: ") )

soma = 0
digito = numero

while digito > 0 :
    soma = soma + digito % 10
    digito = digito // 10
    print("Soma:", soma, " - Digito:", digito)

print("A soma dos digitos do numero", numero, "é igual a:", soma)