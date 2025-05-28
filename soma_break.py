#o break interrompe o loop

soma = 0

while True:
    x = int(input('digite um número para ser somado:  \n 0 para sair:'))
    if x == 0:
        break
    soma += x # type: ignore
    print(f'a soma dos números digitados é {soma}')