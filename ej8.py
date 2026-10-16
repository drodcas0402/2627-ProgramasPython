def main():
    num1 = float(input("Introduce el primer número a sumar: "))
    num2 = float(input("Introduce el segundo número a sumar: "))

    num1 = num1 + num2

    num2 = float(input("Introduce el tercer número a sumar: "))
    
    num1 = num1 + num2 
    
    print(f"El número resultado de la suma de los 3 introducidos será de: {num1}")
if __name__ == "__main__":
    main()