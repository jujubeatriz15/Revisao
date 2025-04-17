a = int(input("digite o valor de A: "))
b = int(input("digite o valor de B: "))
c = int(input("digite o valor de C: "))

soma = a + b
if soma < c:
    print(f"A soma de {soma} é menor que C")
else:
    print(f"A soma de {soma} não é menor que C")