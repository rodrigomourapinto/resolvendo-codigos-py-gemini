# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
# Recebendo a string do usuário
texto = input("Digite o texto que deseja repetir: ")

# Recebendo o número inteiro e convertendo de string para int
vezes = int(input("Digite um número inteiro de repetições: "))

# Exibindo o resultado
print(f"O texto repetido é: {f"{texto} " * vezes}")