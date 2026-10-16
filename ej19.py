def main():
    nombre = str(input("Introduce tu nombre: "))
    letras = len(nombre.replace(" ", ""))
    print (letras)

if __name__ == "__main__":
    main()