ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = 2025
idade_anos = ano_atual - ano_nasc
meses = idade_anos * 12
dias = idade_anos * 365
print(f"Você viveu: {idade_anos} anos, {meses} meses e {dias} dias.")
