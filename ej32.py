def main():

    contador = 0
    num = int(input("Introduce el número para calcular serie de fibonacci: "))

    fibo1 = 0
    fibo2 = 1

    while contador != num:
        contador = contador + 1
        proximo = fibo1 + fibo2
        fibo1 = fibo2
        fibo2 = proximo

        print (fibo2)
if __name__ == "__main__":
    main()