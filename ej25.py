def main():
	fecha = str(input("Introduce una fecha de nacimiento en formato dd/mm/aaaa: "))
	
	dia, mes, año = fecha.split('/')
	
	dia = int(dia)
	mes = int(mes)
	
	print(f"Día: {dia}")
	print(f"Mes: {mes}")
	print(f"Año: {año}")
	
if __name__ == "__main__":
	main()