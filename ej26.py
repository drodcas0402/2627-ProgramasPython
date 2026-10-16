def main():
	
	cesta = str(input("Introduce tus productos de la cesta de la compra separada por comas: "))
	
	productos = cesta.split(',')
	
	for producto in productos:
		print(producto.strip())
		
if __name__ == "__main__":
	main()