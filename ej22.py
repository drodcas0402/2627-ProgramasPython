def main():
	frase = str(input("Introduce una frase: "))
	vocal = str(input("Introduce una vocal: "))
	
	final = frase.replace(vocal, vocal.upper())
	
	print(final)
	
if __name__ == "__main__":
	main()