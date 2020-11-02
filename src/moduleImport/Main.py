# it will import only the summation() from calculation.py
from src.moduleImport.Calculation import *

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
print("Sum = ", summation(a, b))
print("Multi:", multiplication(a, b))
