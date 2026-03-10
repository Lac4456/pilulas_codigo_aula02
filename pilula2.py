import random
cotacaoI = float(input("Cotação atual do dolar: R$"))
variacao = random.uniform(-0.015, 0.015)
cotacaoF = cotacaoI * (1 + variacao)
print(f"Variação simulada: {variacao:.3%}")
print(f"Nova cotação: R${cotacaoF:.2f}")