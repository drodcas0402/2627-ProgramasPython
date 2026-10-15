def main():

	nombre = str(input("Introduce tu nombre: ")) 
	
	num = -1
	
	while num < 0:
		num = int(input("Introduce un número positivo: "))
		
		if num < 0:
			print("Introduce un número mayor que 0")
	
	rep = 0
	
	while rep != num:
		
		print(f"{nombre}")
		rep = rep + 1
		
if __name__ == "__main__":
	main()