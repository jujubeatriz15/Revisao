#calculo do imc
repetir = "s"
while repetir == "s" or repetir == "S":
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite seu altura: "))
    imc = peso / altura ** 2
    if imc < 18.6:
        print("Abaixo do peso")
    elif imc >=18.6 and imc <= 24.9:
        print("Peso ideal, parabéns!")
    elif imc >= 25 and imc <= 29.9:
        print("Levemente acima do peso")
    elif imc >= 30 and imc <= 34.9:
        print("Obesidade grau 1")
    elif imc >=35 and imc <= 40:
        print("Obesidade grau 2")
    else:
        print("Obesidade grau 3 (procure um médico já!)")
    repetir = input("Deseja verificar outro numero? ")
