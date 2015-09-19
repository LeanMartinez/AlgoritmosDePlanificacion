lista = [['p1',3,2],['p2',4,0],['p3',3,1]]

#esto es una prueba
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

proceso =  obtenerPrimeraEjecucion(lista)
print restarCPU(proceso)


