repetir = "s"
while repetir == "s" or repetir == "S":
    n = int(input("Digite um nùmero: "))
    if n > 0:
        if n % 2 == 0:
            print("par e positivo")
        else:
            print("ímpar e positivo")
    else:
        if n % 2 == 0:
            print("par e negativo")
        else:
            print("impar e negativo")
    repetir = input("Deseja verificar outro numero? ")