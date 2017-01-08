import sys

if len(sys.argv) == 3:
	texto = sys.argv[1]
	repeticiones = int(sys.argv[2])
	for x in range(repeticiones):
		print(texto)

else:

	print("Error, introduce los argumentos correctamente")
	print("Ejemplo: escribir_linias.py 'Texto' 5")