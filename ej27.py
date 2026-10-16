def main():

	producto = str(input("Introduce el nombre del producto: "))
	precio = float(input("Introduce el precio del producto: "))
	unidades = int(input("Introduce el número de unidades: "))
	
	precioUNI = precio * unidades
	
	print(f"El {producto} vale {precio:06.2f}, y contando con que se venden {unidades:03d}, tendrá un coste total de {precioUNI:08.2f}")

if __name__ == "__main__":
	main()