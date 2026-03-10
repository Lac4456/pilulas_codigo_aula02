import math
assinantes = int(input("Numero atual de assinantes: "))
mensalidade = float(input("Valor da mensalidade: R$"))
taxa = float(input("Taxa media de crescimento %:"))
meses = int(input("Quantidade de meses da projeção: "))

assinantesF = assinantes * math.pow((1+taxa/100), meses)
receitaF = assinantesF * mensalidade

print(f"Assinantes estimados: {assinantesF:.0f}")
print(f"Receita final: {receitaF:.2f}")