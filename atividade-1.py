# exercicios.py

# 1) A + B é menor que C
def exercicio1():
    a = float(input("Digite A: "))
    b = float(input("Digite B: "))
    c = float(input("Digite C: "))

    if a + b < c:
        print("A + B é menor que C")
    else:
        print("A + B não é menor que C")


# 2) Par ou ímpar
def exercicio2():
    n = int(input("Digite um número: "))

    if n % 2 == 0:
        print("Número PAR")
    else:
        print("Número ÍMPAR")


# 3) Soma se iguais, multiplica se diferentes
def exercicio3():
    a = int(input("Digite A: "))
    b = int(input("Digite B: "))

    if a == b:
        c = a + b
    else:
        c = a * b

    print("Resultado C =", c)


# 4) Dobro se positivo, triplo se negativo
def exercicio4():
    n = float(input("Digite um número: "))

    if n >= 0:
        resultado = n * 2
    else:
        resultado = n * 3

    print("Resultado:", resultado)


# 5) Soma 5 se par ou soma 8 se ímpar
def exercicio5():
    n = int(input("Digite um número: "))

    if n % 2 == 0:
        resultado = n + 5
    else:
        resultado = n + 8

    print("Resultado:", resultado)


# 6) Mostrar três números em ordem decrescente
def exercicio6():
    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))
    c = int(input("Digite o terceiro número: "))

    lista = [a, b, c]
    lista.sort(reverse=True)

    print("Ordem decrescente:", lista)


# 7) Calcular peso ideal
def exercicio7():
    altura = float(input("Digite sua altura (ex: 1.75): "))
    sexo = input("Digite seu sexo (M/F): ").upper()

    if sexo == "M":
        peso = (72.7 * altura) - 58
    else:
        peso = (62.1 * altura) - 44.7

    print("Peso ideal:", round(peso, 2), "kg")


# 8) Calcular IMC
def exercicio8():
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    imc = peso / (altura ** 2)

    print("IMC:", round(imc, 2))

    if imc < 18.5:
        print("Condição: Abaixo do peso")
    elif imc < 25:
        print("Condição: Peso normal")
    elif imc < 30:
        print("Condição: Acima do peso")
    else:
        print("Condição: Obeso")


# 9) Condição de pagamento
def exercicio9():
    preco = float(input("Digite o preço do produto: "))

    print("Forma de pagamento:")
    print("1 - À vista dinheiro/cheque (10% desconto)")
    print("2 - À vista cartão crédito (15% desconto)")
    print("3 - Em 2x sem juros")
    print("4 - Em 2x com 10% de juros")

    codigo = int(input("Escolha a opção: "))

    if codigo == 1:
        total = preco * 0.90
    elif codigo == 2:
        total = preco * 0.85
    elif codigo == 3:
        total = preco
    elif codigo == 4:
        total = preco * 1.10
    else:
        print("Código inválido")
        return

    print("Valor a pagar: R$", round(total, 2))


# 10) Média de aproveitamento
def exercicio10():
    numero = input("Número do aluno: ")

    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    me = float(input("Média dos exercícios: "))

    ma = (n1 + n2 * 2 + n3 * 3 + me) / 7

    if ma >= 90:
        conceito = "A"
    elif ma >= 75:
        conceito = "B"
    elif ma >= 60:
        conceito = "C"
    elif ma >= 40:
        conceito = "D"
    else:
        conceito = "E"

    if conceito in ["A", "B", "C"]:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    print("\nNúmero do aluno:", numero)
    print("Notas:", n1, n2, n3)
    print("Média dos exercícios:", me)
    print("Média de aproveitamento:", round(ma, 2))
    print("Conceito:", conceito)
    print("Situação:", situacao)


# MENU PRINCIPAL
while True:
    print("\n===== MENU =====")
    print("1 - Exercício 1")
    print("2 - Exercício 2")
    print("3 - Exercício 3")
    print("4 - Exercício 4")
    print("5 - Exercício 5")
    print("6 - Exercício 6")
    print("7 - Exercício 7")
    print("8 - Exercício 8")
    print("9 - Exercício 9")
    print("10 - Exercício 10")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        exercicio1()
    elif opcao == "2":
        exercicio2()
    elif opcao == "3":
        exercicio3()
    elif opcao == "4":
        exercicio4()
    elif opcao == "5":
        exercicio5()
    elif opcao == "6":
        exercicio6()
    elif opcao == "7":
        exercicio7()
    elif opcao == "8":
        exercicio8()
    elif opcao == "9":
        exercicio9()
    elif opcao == "10":
        exercicio10()
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida!")
