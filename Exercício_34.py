saldo = float(input("Qual seu saldo? "))
valor_da_compra = float(input("Qual o valor total de sua compra? "))

if saldo >= valor_da_compra:
    str(input("Confirmar compra? ")) == "Sim" or "Não"
    if "Sim":
        print("Compra realizada")
    else:
        print("Compra cancelada")
elif saldo < valor_da_compra:
    print("Saldo insuficiente")