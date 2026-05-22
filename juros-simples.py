# Autor: Gabriela Souza
# Projeto: Calculadora Simples
# Data: 2026-05-21

# Entrada de dados
valorInicial = float(input("Digite o valor inicial: R$ "))
taxaJuros = float(input("Digite a taxa de juros (%): "))
periodo = int(input("Digite o período (meses): "))

# Cálculos
jurosSimples = valorInicial * (taxaJuros / 100) * periodo
valorFinal = valorInicial + jurosSimples

print("================================")
print("  Calculadora de Juros Simples  ")
print("================================")
print(f"Valor investido: R$ {valorInicial:.2f}")
print(f"Juros: R$ {jurosSimples:.2f}")
print(f"Valor Final: R$ {valorFinal:.2f}")