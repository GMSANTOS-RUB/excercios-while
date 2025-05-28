#media com break
soma = 0
nota = 0

while True:
    nota= float(input('digite a nota do aluno: \n ou \ndigite a 99 para sair: ' ))
    if nota ==99:
        break
    soma += nota 
    print(f' a média do aluno é {soma / 4}')