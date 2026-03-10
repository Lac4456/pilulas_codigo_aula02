import locale
locale.setlocale(locale.LC_ALL, "pt_br.UTF-8")

valor1 = float(input("Digite o valor 1: R$"))
valor2 = float(input("Digite o valor 2: R$"))
valor3 = float(input("Digite o valor 3: R$"))

valorF = valor1 + valor2 + valor3

print(f"Valor 1: {locale.currency(valor1, grouping=True)}")
print(f"Valor 2: {locale.currency(valor2, grouping=True)}")
print(f"Valor 3: {locale.currency(valor3, grouping=True)}")
print(f"Valor final: {locale.currency(valorF, grouping=True)}")