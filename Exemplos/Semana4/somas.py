print("Digite uma sequencia de valores a serem somados, terminando a leitura em zero.")

soma = 0
valor = 1

while valor != 0:
    valor = int( input("Digite um valor a ser somado: ") )
    soma += valor

print("A soma dos valores digitados é", soma)