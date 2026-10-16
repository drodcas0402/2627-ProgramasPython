def main():
	n = float(input("Introduce un número a dividir: "))
	m = float(input("Introduce un número para dividir al anterior: "))
	
	if m == 0:
		división = "infinito"

	else:
		división = n // m
		comprobante_resto = n/m
		if división == comprobante_resto:
			r = 0
		else:
			r = n % m
	
	if m != 0:	
		print(f"La división de {n} entre {m} da un cociente {división} y un resto {r}")
	else:
		print(f"La división de {n} entre {m} da un resultado de {división}")
		
if __name__ == "__main__":
	main()