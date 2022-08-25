from tkinter import S

import math 
a =int(input("valor1:"))
b =int(input("valor2:"))
s =int(input("valor3:"))

maior = (a + b+ math.abs(a-b))/2
print(f"é maior {maior}")
