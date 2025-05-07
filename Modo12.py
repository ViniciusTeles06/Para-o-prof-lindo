valor = float(input("Valor do produto: "))
print("1 - Dinheiro/Pix (15% desc.)\n2 - Cartão à vista (10% desc.)\n3 - Cartão 2x (sem juros)\n4 - Cartão 3x+ (10% juros)")
opcao = int(input("Escolha a opção de pagamento: "))
if opcao == 1:
    total = valor * 0.85
elif opcao == 2:
    total = valor * 0.90
elif opcao == 3:
    total = valor
elif opcao == 4:
    total = valor * 1.10
else:
    total = valor
    print("Opção inválida, valor sem desconto.")
print(f"Total a pagar: R${total:.2f}")