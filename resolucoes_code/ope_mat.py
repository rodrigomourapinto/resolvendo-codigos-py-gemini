# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
def main():
    questao_3()
    print("\n", "#" * 50)
    questao_4()
    print("\n", "#" * 50)
    questao_5()

def questao_3():
    # Recebendo os dois números do usuário (convertendo para float)
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Realizando as operações
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2

    # Verificando a divisão para evitar erro por divisão por zero
    if num2 != 0:
        divisao = num1 / num2
    else:
        divisao = "Erro (divisão por zero)"

    # Exibindo os resultados formatados
    print(f"\n--- Resultados ---")
    print(f"Soma: {soma}")
    print(f"Subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")


def questao_4():
    # Recebendo o número inteiro
    numero = int(input("Digite um número inteiro: "))

    # Verificando se é par ou ímpar usando condicional
    if numero % 2 == 0:
        print(f"O número {numero} é **PAR**.")
    else:
        print(f"O número {numero} é **ÍMPAR**.")

    ## 5 
    # Recebendo as três notas
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Calculando a média aritmética
    media = (nota1 + nota2 + nota3) / 3

    # Exibindo o resultado formatado
    print(f"A média das notas é: {media:.2f}")


def questao_5():
    # Recebendo a palavra, removendo espaços e convertendo para minúsculas
    palavra = input("Digite uma palavra: ").strip().lower()

    # Invertendo a string usando slicing
    palavra_invertida = palavra[::-1]

    # Verificando se é um palíndromo
    if palavra == palavra_invertida:
        print(f"A palavra '{palavra}' é um **palíndromo**! 🔄")
    else:
        print(f"A palavra '{palavra}' NÃO é um palíndromo.")

if __name__ == "__main__":
    main()