def main():
	precio = str(input("Introduce el precio de un producto con dos decimales: "))
	
	precio = precio.replace('.', ',')
	euros, centimos = precio.split(',')
	
	print(f"{euros} euros y {centimos} céntimos")
	
if __name__ == "__main__":
	main()