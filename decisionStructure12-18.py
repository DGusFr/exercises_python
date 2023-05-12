import math

def calcula_folha_pagamento(valor_hora, horas_trabalhadas):
    salario_bruto = valor_hora * horas_trabalhadas
    if salario_bruto <= 900:
        ir = 0
    elif salario_bruto <= 1500:
        ir = salario_bruto * 0.05
    elif salario_bruto <= 2500:
        ir = salario_bruto * 0.1
    else:
        ir = salario_bruto * 0.2

    inss = salario_bruto * 0.1
    fgts = salario_bruto * 0.11
    descontos = ir + inss + (salario_bruto * 0.03)
    salario_liquido = salario_bruto - descontos

    print(f"Salário Bruto: ({valor_hora} * {horas_trabalhadas}): R$ {salario_bruto:.2f}")
    print(f"(-) IR ({ir * 100 / salario_bruto:.0f}%): R$ {ir:.2f}")
    print(f"(-) INSS (10%): R$ {inss:.2f}")
    print(f"FGTS (11%): R$ {fgts:.2f}")
    print(f"Total de descontos: R$ {descontos:.2f}")
    print(f"Salário Liquido: R$ {salario_liquido:.2f}")


def dia_da_semana(numero):
    dias = {
        1: "Domingo",
        2: "Segunda",
        3: "Terça",
        4: "Quarta",
        5: "Quinta",
        6: "Sexta",
        7: "Sábado"
    }
    if numero in dias:
        return dias[numero]
    else:
        return "Valor inválido"

def calcula_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 9:
        conceito = "A"
    elif media >= 7.5:
        conceito = "B"
    elif media >= 6:
        conceito = "C"
    elif media >= 4:
        conceito = "D"
    else:
        conceito = "E"

    if conceito in ["A", "B", "C"]:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"

    print(f"Nota 1: {nota1:.1f}")
    print(f"Nota 2: {nota2:.1f}")
    print(f"Média: {media:.1f}")
    print(f"Conceito: {conceito}")
    print(f"Situacao: {situacao}")

def calcula_raizes_equacao_segundo_grau(a, b, c):
    if a == 0:
        print("A equação não é do segundo grau.")
        return

    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")
        return
    elif delta == 0:
        x = -b / (2*a)
        print(f"A equação possui apenas uma raiz real: x = {x}")
        return
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raízes reais: x1 = {x1} e x2 = {x2}")
        return

