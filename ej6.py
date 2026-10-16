def main():
    precioT = float(input("Introduce el precio con IVA: "))

    precioF = precioT / 1.10

    print (f"El precio introducido sin el IVA del 10% es de {precioF}$")
if __name__ == "__main__":
    main()