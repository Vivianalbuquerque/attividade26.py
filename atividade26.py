# Exercício Python 26: Desenvolva um programa que leia o
# primeiro termo e a razão de uma Pogreçao Aritimetica.
# No final, mostre os 10 primeiros termos dessa progressão.
a1 = int(input("DIGITE O PRIMEIRO TERMO DA PA: "))
r = int(input("DIGITE ARAZÃO DA PA: "))

for i in range(10):
    print(i)
    termo =  a1 + i * r
    print(f"termo {i+1} : {termo}")
    