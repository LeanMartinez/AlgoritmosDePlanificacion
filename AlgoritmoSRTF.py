lista = [['p1',3,2],['p2',5,0],['p3',2,1]]


def obtenerPrimeraEjecucion(lista):
	i = 1
	for x in lista:
		if i == 1:
			llegada = x[2]
			i = i + 1
		else:
			if x[2] < llegada:
				llegada = x[2]
				return x 

def restarCPU(proceso):
	proceso[1] = proceso[1] -1
	return proceso

def comparar(proceso, lista):
	for x in lista:
		if proceso[1] > x[1]:
			return x
		else:
			return proceso

proceso =  obtenerPrimeraEjecucion(lista)
print proceso
print restarCPU(proceso)
remplazo = comparar(proceso,lista)
print remplazo

