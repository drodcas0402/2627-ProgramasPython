def main():
    importe = float(input("Escribe el importe a pagar:" ))
    iva = float(input("Introduce el IVA a aplicar: "))

    importe = iva / 100 * importe + importe

    print(f"El importe con iva  tendrá un total de {importe} $")

if __name__ == "__main__":
    main()