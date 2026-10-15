def main():
   horastrabajo = int(input("horas de trabajo: "))
   preciohora = int(input("Coste por hora: "))

   importetotal = horastrabajo * preciohora
   
   print("Importe total: " + str(importetotal))


if __name__ == "__main__":
   main()