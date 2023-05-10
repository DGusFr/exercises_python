import math

def fahrenheit_para_celsius(f):
    c = 5 * ((f - 32) / 9)
    return c

def celsius_para_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

def calcula_numeros(num1, num2, num3):
    produto = (2 * num1) * (num2 / 2)
    soma = (3 * num1) + num3
    cubo = num3 ** 3
    return produto, soma, cubo

def peso_ideal(altura, genero):
    if genero == 'M':
        peso = (72.7 * altura) - 58
    elif genero == 'F':
        peso = (62.1 * altura) - 44.7
    else:
        return "Gênero inválido"
    return peso

def calcular_multa(peso):
    excesso = 0
    multa = 0
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4
    return excesso, multa

def calcular_salario(horas_trabalhadas, valor_hora):
    salario_bruto = horas_trabalhadas * valor_hora
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    descontos = ir + inss + sindicato
    salario_liquido = salario_bruto - descontos
    return salario_bruto, inss, sindicato, salario_liquido


def calcular_tinta(area):
    litros_tinta = area / 3 + (area / 3 * 0.1)
    latas = math.ceil(litros_tinta / 18)
    preco_total = latas * 80
    return latas, preco_total


def calcular_compra_tinta(area):
    litros = area / 6 * 1.1 # 10% de folga
    latas = math.ceil(litros / 18)
    galoes = math.ceil(litros / 3.6)
    preco_latas = latas * 80
    preco_galoes = galoes * 25
    mistura_latas = math.floor(litros / 18)
    mistura_galoes = math.ceil((litros - mistura_latas * 18) / 3.6)
    preco_mistura = mistura_latas * 80 + mistura_galoes * 25
    return latas, preco_latas, galoes, preco_galoes, mistura_latas, mistura_galoes, preco_mistura

def calcular_tempo_download(tamanho_arquivo, velocidade_internet):
    tamanho_arquivo_mb = tamanho_arquivo / 8 / 1024
    tempo_download_min = tamanho_arquivo_mb / velocidade_internet * 60
    return tempo_download_min

fahrenheit_para_celsius(86)
celsius_para_fahrenheit(30)
calcula_numeros(3, 7, 9)
peso_ideal(180, 'M')
calcular_multa(100)
calcular_salario(7, 4.5)
calcular_tinta(15)
calcular_compra_tinta(62)
calcular_tempo_download(534, 43)