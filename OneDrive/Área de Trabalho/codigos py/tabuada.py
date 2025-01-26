def tabuada(y):
	x = int(y) * 10 
	return range(0, x+1 , y)

y = int(input(" escolha a tabuada(1 a 10):  "))

print(list(tabuada(y)))