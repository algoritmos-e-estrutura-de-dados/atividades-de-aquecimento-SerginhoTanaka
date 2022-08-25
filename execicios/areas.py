import math 
a = float(input("Informe o valor A"))
b = float(input("Informe o valor B"))
c = float(input("Informe o valor C"))

triangulo = a * c 
circulo = math.pi * (b*b)
trapezio = a * b * c 
quadrado = b *b
retangulo = a * b 

print(f"TRIANGULO = {triangulo}")
print(f"TRIANGULO = {circulo}")
print(f"TRIANGULO = {trapezio}")
print(f"TRIANGULO = {quadrado}")
print(f"TRIANGULO = {retangulo}")