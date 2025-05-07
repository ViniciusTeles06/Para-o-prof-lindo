nome = input("Nome do aluno: ")
notas = [float(input(f"Nota {i+1}: ")) for i in range(4)]
media = sum(notas) / 4
print(f"Média de {nome}: {media:.2f}")
if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")
