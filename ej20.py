def main():
    
    teléfono = str(input("Introduce tu número de teléfono con prefijo: "))
    
    teléfono = teléfono.replace("+","").replace("-","")

    teléfono = teléfono[2:]
    
    print(f"El teléfono sin prefijos es: {teléfono}")

if __name__ == "__main__":
    main()