def maior_num(a, b):
    if a > b:
        return a
    else:
        return b

def verifica_sinal(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"

def verifica_sexo(letra):
    if letra.upper() == 'F':
        return "Feminino"
    elif letra.upper() == 'M':
        return "Masculino"
    else:
        return "Sexo Inválido"

def verifica_vogal(letra):
    vogais = ['a', 'e', 'i', 'o', 'u']
    if letra.lower() in vogais:
        return "vogal"
    else:
        return "consoante"

def verifica_aprovacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media == 10:
        return "Aprovado com Distinção"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def maior_numero(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def maior_e_menor(a, b, c):
    maior = a
    menor = a
    
    if b > maior:
        maior = b
    if c > maior:
        maior = c
        
    if b < menor:
        menor = b
    if c < menor:
        menor = c
        
    print(f"O maior número é {maior} e o menor número é {menor}")

def produto_mais_barato(preco1, preco2, preco3):
    if preco1 <= preco2 and preco1 <= preco3:
        print("Compre o primeiro produto.")
    elif preco2 <= preco1 and preco2 <= preco3:
        print("Compre o segundo produto.")
    else:
        print("Compre o terceiro produto.")

def ordem_decrescente(a, b, c):
    lista = [a, b, c]
    lista.sort(reverse=True)
    print(lista)

def saudacao_turno(turno):
    if turno == 'M':
        print("Bom dia!")
    elif turno == 'V':
        print("Boa tarde!")
    elif turno == 'N':
        print("Boa noite!")
    else:
        print("Valor inválido!")

def reajuste_salario(salario_atual):
    if salario_atual <= 280:
        percentual_aumento = 20
    elif salario_atual <= 700:
        percentual_aumento = 15
    elif salario_atual <= 1500:
        percentual_aumento = 10
    else:
        percentual_aumento = 5
        
    aumento = salario_atual * percentual_aumento / 100
    novo_salario = salario_atual + aumento
    
    print(f"Salário antes do reajuste: R${salario_atual:.2f}")
    print(f"Percentual de aumento aplicado: {percentual_aumento}%")
    print(f"Valor do aumento: R${aumento:.2f}")
    print(f"Novo salário após o aumento: R${novo_salario:.2f}")


# Encontrar o maior e o menor número
maior_e_menor(5, 10, 3)

# Encontrar o produto mais barato
produto_mais_barato(20, 15, 10)

# Mostrar os números em ordem decrescente
ordem_decrescente(7, 2, 10)

# Saudar de acordo com o turno
saudacao_turno('M')

# Calcular o aumento de salário
reajuste_salario(1000)

