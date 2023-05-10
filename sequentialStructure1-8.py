import math

def alo_mundo():
    print("Alo mundo")

def pedir_numero():
    num = input("Digite um número: ")
    print("O número informado foi", num)

def soma_numeros():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    soma = num1 + num2
    print("A soma dos dois números é", soma)

def calcular_media():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    nota4 = float(input("Digite a quarta nota: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4
    print("A média das notas é", media)

def converter_metros_para_centimetros():
    metros = float(input("Digite a medida em metros: "))
    centimetros = metros * 100
    print(metros, "metros equivalem a", centimetros, "centímetros")

def calcular_area_do_circulo():
    raio = float(input("Digite o raio do círculo: "))
    area = math.pi * raio ** 2
    print("A área do círculo é", area)

def calcular_area_do_quadrado():
    lado = float(input("Digite o lado do quadrado: "))
    area = lado ** 2
    print("A área do quadrado é", area)
    print("O dobro da área do quadrado é", area * 2)

def calcular_salario():
    valor_hora = float(input("Digite o valor da sua hora de trabalho: "))
    horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
    salario = valor_hora * horas_trabalhadas
    print("O seu salário no referido mês é R$", salario)

"""
alo_mundo()
pedir_numero()
soma_numeros()
calcular_media()
converter_metros_para_centimetros()
calcular_area_do_circulo()
calcular_area_do_quadrado()
calcular_salario()
"""
