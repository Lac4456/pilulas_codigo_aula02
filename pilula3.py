import datetime
import locale
locale.setlocale(locale.LC_ALL, "pt_br.UTF-8")
dataCompra = input("Digite a data da compra (dd/mm/aaaa): ")
prazoGar = int(input("Digite o prazo da garantia (em meses): "))
dataI = datetime.datetime.strptime(dataCompra, "%d/%m/%Y")
dataF = dataI + datetime.timedelta(days= prazoGar * 30)
print(f"Garantia valida ate: {dataF.strftime("%d/%m/%Y")}")
print(f"Dia da semana: {dataF.strftime("%A")}")