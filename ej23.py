def main():
	correo = str(input("Introduce un correo: "))
	
	arroba = correo.find('@')
	
	print(f"{correo[:arroba]}@ceu.es")

if __name__ == "__main__":
	main()