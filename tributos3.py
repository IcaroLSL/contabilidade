tributosDeCompraEmPorcentagem = {}
tributosDeCompraEmValores = {}
tributosDeVendaEmPorcentagem = {}
tributosDeVendaEmValores = {}
somaDeTributosCompra = 0
somaDeTributosVendas = 0
somaDeTributosVendasEmPorcentagem = 0.0

precoDeCompra = float(input("Insira o valor gasto na compra -> ").replace(",", "."))
quantidadeDeProdutosComprada = float(input("Insira a quantidade dos produtos que você comprou -> ").replace(",", "."))
custosAdicionais = round(eval(input("Insira os valores de custo adicional se houver -> ").replace(",", ".")), 2)
lucro = float(input("Insira o valor que deseja ter de lucro -> ").replace(",", "."))/100
quatidadeVendida = float(input("Insira a quantidade vendida de produtos -> ").replace(",", "."))/100

quantidadeDeTributosCompra = int(input("Insira a quantidade de tributos de compra -> "))

listaTemporaria = []
for _ in range(quantidadeDeTributosCompra):
    chave = input("Qual o nome do tributo de compra atual -> ")
    tributosDeCompraEmPorcentagem[chave] = float(input("Insira o valor de cada tributo de compra -> ").replace(",", ".")) / 100
for i in tributosDeCompraEmPorcentagem:
    valor = tributosDeCompraEmPorcentagem[i]
    listaTemporaria.append(round(valor * precoDeCompra, 2))
    tributosDeCompraEmValores[i] = round(valor * precoDeCompra, 2)
somaDeTributosCompra = round(sum(listaTemporaria), 2)

quantidadeDeTributosVenda = int(input("Insira a quantidade de tributos de venda -> "))

listaTemporaria = []
for _ in range(quantidadeDeTributosVenda):
    chave = input("Qual o nome do tributo de venda atual -> ")
    valor = float(input("Insira o valor de cada tributo de venda -> ").replace(",", "."))/100
    tributosDeVendaEmPorcentagem[chave] = valor
    listaTemporaria.append(valor)
somaDeTributosVendasEmPorcentagem = sum(listaTemporaria)

valorEmEstoque = round((precoDeCompra+custosAdicionais-somaDeTributosCompra)/quantidadeDeProdutosComprada, 2)
PrecoDeVendaPorUnidade = round(valorEmEstoque/(1-(lucro+somaDeTributosVendasEmPorcentagem)),2)
receita = round(PrecoDeVendaPorUnidade*(quantidadeDeProdutosComprada*quatidadeVendida), 2)

listaTemporaria = []
for i in tributosDeVendaEmPorcentagem:
    valor = tributosDeVendaEmPorcentagem[i]
    listaTemporaria.append(round(valor*receita, 2))
    tributosDeVendaEmValores[i] = round(valor * receita, 2)
somaDeTributosVendas = round(sum(listaTemporaria), 2)

receitaLiquida = round(receita-somaDeTributosVendas, 2)
custo = (quantidadeDeProdutosComprada*quatidadeVendida)*valorEmEstoque
lucroBruto = round(receitaLiquida-custo, 2)
valorEmEstoqueNoRestante = round((quantidadeDeProdutosComprada*(1-quatidadeVendida))*valorEmEstoque, 2)


print(f"\nValor do estoque -> {valorEmEstoque}\nValor Unitário do produto -> {PrecoDeVendaPorUnidade}")
print("DRE:")
print(f"Receita -> {receita} ATIVO")
for i in tributosDeCompraEmValores:
    print(f"{i} - {(tributosDeVendaEmPorcentagem[i]*100):.2f}% -> {tributosDeVendaEmValores[i]}")
print(f"Receita líquido -> {receitaLiquida}\nCusto -> {custo}\nLucro Bruto -> {lucroBruto} =  patrimônio líquido\nEstoque final -> {valorEmEstoqueNoRestante} ATIVO")

igualdadeEntreOstributos = input("A quantidade de imposto na compra é a mesma que na venda? ").lower()
if igualdadeEntreOstributos == "s" or igualdadeEntreOstributos == "sim" or igualdadeEntreOstributos == "y" or igualdadeEntreOstributos == "yes":
    igualdadeEntreOstributos = True
else:
    igualdadeEntreOstributos = False
if igualdadeEntreOstributos:
    for i in tributosDeCompraEmValores:
        valorDaAnalise = tributosDeCompraEmValores[i] - tributosDeVendaEmValores[i]
        if valorDaAnalise > 0:
            resultadoAnalise = "credor"
            print(f"{i} -> {abs(valorDaAnalise)} {resultadoAnalise}")
        elif valorDaAnalise < 0:
            resultadoAnalise = "devedor"
            print(f"{i} -> {abs(valorDaAnalise)} {resultadoAnalise}")
else:
    print("essa função ainda não foi implementada sera nessesario uma analise manual")
    print(f"imposto compra -> {tributosDeCompraEmValores}")
    print(f"imposto venda -> {tributosDeVendaEmValores}")
    