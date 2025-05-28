# media com while
# 'nota_total' é o ocumulador de notas
notas_total = 0 
bimestre = 0

while bimestre < 4:
    nota = float(input('digite a nota aluno: '))
    nota_total =+ nota  # acumulando a nota total
    bimestre += 1
    print(f'A {nota} digitada do aluno foi armazenada com sucesso!')

media = nota_total / 4 #calculando a média após sair do loop
print(f'A média do aluno é {media}')
 