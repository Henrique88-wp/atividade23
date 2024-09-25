# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.
num2 = int(input("digite um valor"))
for numero in range(1,11):
   print(f"{numero}*{num2}={numero*num2}")