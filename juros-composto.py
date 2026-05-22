# Autor: Gabriela Souza
# Projeto: Calculadora de Juros Compostos
# Data: 2026-05-22

# Entrada de dados
valorInicial = float(input("Digite o valor inicial: R$ "))
taxaJuros = float(input("Digite a taxa de juros (%): "))
periodo = int(input("Digite o período (meses): "))

# Cálculos
valorFinal = valorInicial * (1 + (taxaJuros / 100)) ** periodo
jurosCompostos = valorFinal - valorInicial

# Saída de dados
print("================================")
print("  Calculadora de Juros Compostos  ")
print("================================")
print(f"Valor investido: R$ {valorInicial:.2f}")
print(f"Juros Compostos: R$ {jurosCompostos:.2f}")
print(f"Valor Final: R$ {valorFinal:.2f}")