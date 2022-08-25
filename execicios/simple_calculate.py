qntP1 =int(input("Informe a quantidade do produto 1"))
precoP1 =float(input("Informe o preço do produto 1"))
codigoP1 = int(input("informe o código do produto 1 "))
valor1 = qntP1 * precoP1

qntP2 =int(input("Informe a quantidade do produto 2"))
precoP2 =float(input("Informe o preço do produto 2"))
codigoP2 = int(input("informe o código do produto 2 "))
valor2 = qntP2 * precoP2


print(f"O produto do código {codigoP1} vai custar R${valor1}")
print(f"O produto do código {codigoP2} vai custar R${valor2}")