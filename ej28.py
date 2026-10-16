def main():
    a = float(input("Introduce la medida en cm del primer lado (solo num): "))
    b = float(input("Introduce la medida en cm del segundo lado (solo num): "))
    c = float(input("Introduce la medida en cm del tercer lado (solo num): "))
    
    if (a + b > c) and (a + c > b) and (b + c > a):
        s = (a + b + c) / 2  
        area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        
        print(f"El área del triángulo será de {area:.2f} cm²")
    else:
        print("Esta operación es imposible.")
        
if __name__ == "__main__":
    main()