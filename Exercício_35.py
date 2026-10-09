matriculado =  str(input("Está matriculado? "))

if matriculado ==  "Sim":
    str(input("Possui autorização? ")) == "Sim"
    if "Sim":
        print("Acesso permitido")
    else:
        print("Autorização necessária")
else:
    print("Matrícula necessária")