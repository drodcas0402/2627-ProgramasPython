def main():
    nombre = str(input("Introduce tu nombre: "))
    letras = len(nombre.replace(" ", ""))
    print (f"el nombre {nombre.upper()} tiene {letras} letras")

if __name__ == "__main__":
    main()
