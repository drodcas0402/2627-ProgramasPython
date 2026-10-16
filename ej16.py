def main():
	
	pan_diaant = -1

	while pan_diaant < 0:
		pan_diaant = int(input("Introduce el número de barras de pan que no se vendieron el día anterior: "))
		
		if pan_diaant < 0:
			print("Por favor introduzca un número mayor o igual a 0")


	if pan_diaant > 0:
		
		precio = 3.49 * pan_diaant

		descuento = precio - (precio * 0.6)

		print(f"La cantidad de panes a descontar era de {pan_diaant:.2f}, cuyo precio era de {precio:.2f}$, y tras el descuento aplicado del 60% es de {descuento:.2f}$")
		
	else:
		print("No hay pan del día anterior")

if __name__ == "__main__":
	main()