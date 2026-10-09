idade = int(input("Qual sua idade? "))
possui_ingresso = str(input("Possui ingresso? "))

if idade >= 18 and possui_ingresso == "Sim":
    print("Entrada permitida")
elif idade >= 18 and possui_ingresso == "Não":
    print("Ingresso necessário")
elif idade <= 18:
    print("Idade insuficiente")