try:
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))
    resultado = x/y
    print(f"Resultado da divisão: {resultado}")
except ValueError:
    print("Erro: você deve digitar apenas números.")
except ZeroDivisionError:
    print("Erro: não é possível dividir por zero.")
