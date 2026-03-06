# exercicios.py

# 1) A + B é menor que C
def exercicio1()
    a = float(input(Digite A ))
    b = float(input(Digite B ))
    c = float(input(Digite C ))

    if a + b  c
        print(A + B é menor que C)
    else
        print(A + B não é menor que C)


# 2) Par ou ímpar
def exercicio2()
    n = int(input(Digite um número ))

    if n % 2 == 0
        print(Número PAR)
    else
        print(Número ÍMPAR)


# 3) Soma se iguais, multiplicação se diferentes
def exercicio3()
    a = int(input(Digite A ))
    b = int(input(Digite B ))

    if a == b
        c = a + b
    else
        c = a  b

    print(Resultado C =, c)


# 4) Dobro se positivo, triplo se negativo
def exercicio4()
    n = float(input(Digite um número ))

    if n = 0
        resultado = n  2
    else
        resultado = n  3

    print(Resultado, resultado)


# 5) Soma 5 se par, soma 8 se ímpar
def exercicio5()
    n = int(input(Digite um número ))

    if n % 2 == 0
        resultado = n + 5
    else
        resultado = n + 8

    print(Resultado, resultado)


# 6) Três números em ordem decrescente
def exercicio6()
    a = int(input(Digite o primeiro número ))
    b = int(input(Digite o segundo número ))
    c = int(input(Digite o terceiro número ))

    lista = [a, b, c]
    lista.sort(reverse=True)

    print(Ordem decrescente, lista)


# 7) Peso ideal
def exercicio7()
    altura = float(input(Digite sua altura (ex 1.75) ))
    sexo = input(Digite seu sexo (MF) ).upper()

    if sexo == M
        peso = (72.7  altura) - 58
    else
        peso = (62.1  altura) - 44.7

    print(Peso ideal, round(peso, 2), kg)


# 8) Cálculo do IMC
def exercicio8()
    peso = float(input(Digite seu peso (kg) ))
    altura = float(input(Digite sua altura (m) ))

    imc = peso  (altura  2)

    print(IMC, round(imc, 2))

    if imc  18.5
        print(Condição Abaixo do peso)
    elif imc  25
        print(Condição Peso normal)
    elif imc  30
        print(Condição Acima do peso)
    else
        print(Condição Obeso)


# Menu
while True
    print(n===== MENU =====)
    print(1 - Exercício 1)
    print(2 - Exercício 2)
    print(3 - Exercício 3)
    print(4 - Exercício 4)
    print(5 - Exercício 5)
    print(6 - Exercício 6)
    print(7 - Exercício 7)
    print(8 - Exercício 8)
    print(0 - Sair)

    opcao = input(Escolha uma opção )

    if opcao == 1
        exercicio1()
    elif opcao == 2
        exercicio2()
    elif opcao == 3
        exercicio3()
    elif opcao == 4
        exercicio4()
    elif opcao == 5
        exercicio5()
    elif opcao == 6
        exercicio6()
    elif opcao == 7
        exercicio7()
    elif opcao == 8
        exercicio8()
    elif opcao == 0
        break
    else
        print(Opção inválida!)