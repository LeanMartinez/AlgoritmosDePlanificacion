#lista = [['p1',3,1],['p2',5,0],['p3',2,3]]
lista = [['p1',3,0],['p2',1,1],['p3',2,2]]
instanciasDeTiempo = 0

def obtenerPrimeraEjecucion(lista):
	i = 1
	for x in lista:
		if i == 1:
			primerProcesoAIngresar = x
			i = i + 1
		else:
			if x[2] < primerProcesoAIngresar[2]:
				primerProcesoAIngresar = x
					
	return primerProcesoAIngresar 

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

def obtenerCantidadDeCpuTotal(lista):
	cantidad = 0
	for x in lista:
		cantidad = cantidad + x[1]

	return cantidad

proceso =  obtenerPrimeraEjecucion(lista)
cantidadCpuTotal = obtenerCantidadDeCpuTotal(lista)
for x in range(cantidadCpuTotal):
	#print proceso, instanciasDeTiempo
	if proceso == lista[lista.index(proceso)] and len(proceso) == 3:
		proceso.append(1)
		restarCPU(proceso)

	else:
		restarCPU(proceso)
	print proceso, instanciasDeTiempo
	instanciasDeTiempo = instanciasDeTiempo + 1
	proceso = comparar(proceso,lista, instanciasDeTiempo)

