def fatorial(x):
	produto = 1
	for numero in range(1,x+1):
		produto = produto * numero
	return produto
x = int(input("digite um numero: "))
print(f' o fatorial de {list(range(1,x+1))} ou {x}! eh = {fatorial(x)}' )