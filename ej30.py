def main():
	
	num = int(input("Introduce un número: "))
	
	if num <= 1:
		print(f"El número {num} no es primo")
		
	else:
		primo = True
		
		for i in range(2, num):
			if num % i == 0:
				primo=False
				break
			
		if primo:	
			print(f"El número {num} es primo")
		else:
			print(f"El número {num} no es primo")
				
if __name__ == "__main__":
	main()