vidaUtil = float(input("Insira a vida útil do produto em anos-> ").replace(",", "."))
valorDoBem = float(input("Insira o valor do bem -> ").replace(".", ""))
imposto = float(eval(input("digite o imposto do bem ->").replace(",", ".")))
desgastePorAno = 100/vidaUtil
desgastePorMes = desgastePorAno/12
desgasteDoBem = valorDoBem*(desgastePorMes/100)
print(f"\nDesgaste por ano -> {desgastePorAno}\nDesgaste por mês -> {desgastePorMes}\n")

