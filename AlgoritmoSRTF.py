lista = [['p1',3,1],['p2',5,0],['p3',2,3]]
#lista = [['p1',3,0],['p2',1,2],['p3',2,3]]
instanciasDeTiempo = 0

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

def comparar(proceso, lista, instanciasDeTiempo):
	if proceso[1] == 0:
		for x in lista:
			if x[0] == proceso[0]:
				ubicacion = lista.index(x)
				lista.pop(ubicacion)
				if lista==[]:
					print "Fin"
				else:
					return lista[ubicacion-1]
	else:			
		siguienteProceso = None
		for x in lista:
			if len(x) > 3:
				if proceso[1] > x[1]:
					siguienteProceso = x
				else:
					if siguienteProceso == None:
						siguienteProceso = proceso
			else:
				if proceso[1] > x[1] and x[2] == instanciasDeTiempo:
					siguienteProceso = x
				else:
					if siguienteProceso == None:
						siguienteProceso = proceso
		
			
		return siguienteProceso


proceso =  obtenerPrimeraEjecucion(lista)
for x in range(10):
	print proceso, instanciasDeTiempo
	if proceso == lista[lista.index(proceso)] and len(proceso) == 3:
		proceso.append(1)
		restarCPU(proceso)

	else:
		restarCPU(proceso)
	print proceso, instanciasDeTiempo
	instanciasDeTiempo = instanciasDeTiempo + 1
	proceso = comparar(proceso,lista, instanciasDeTiempo)

