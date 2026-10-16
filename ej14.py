def main():
	payasos = -1
	muñecas = -1
	
	while payasos < 0:
		payasos = int(input("Introduce el número de payasos en el paquete: "))
	
	while muñecas < 0:
		muñecas = int(input("Introduce el número de muñecas en el paquete: "))
	
	peso = (payasos * 112) + (muñecas * 75)
	
	print(f"El peso del paquete será de {peso}g")
if __name__ == "__main__":
	main()