import random
	

def main():

	num1 = int(input("Introduce el primer número: "))
	num2 = int(input("Introduce el segundo número: "))
	
	numero = random.randint(num1,num2)
	
	print(numero)
	
if __name__ == "__main__":
	main()