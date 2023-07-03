#!/usr/bin/python3

'''
    Autor: Nicolas Pauer
    Mail: nicolaspauer20@gmail.com
    Fecha: 03/07/2023
    
	Copia una carpeta a cada una de las sub-carpetas
	para que tengan la misma estructura de directorios
	para ser mas facil navegar por ellas y organizarlas
	mejor.
'''

# Modulo de sistema	
import os


# Modificar tupla con nombre de cada una de las subcarpetas donde crear la misma carpeta
subcarpetas = ()
# Obtiene carpeta a agregar dentro de cada una de ellas, la creo y la copio en bucle hasta terminar

print('Copia una carpeta a cada una de las sub-carpetas.\n')
carpeta = input('Ingrese nombre de carpeta a agregar: ')

for subcarpeta in subcarpetas:
  # Muestra que carpeta copio y a donde
	print('\nCopiando carpeta "' + carpeta + '" a sub-carpeta "' + subcarpeta + '".\n')
  # Crea la carpeta	
	os.system('mkdir ' + carpeta)
  # La mueve a cada una de las sub-carpetas	
	os.system('mv ' + carpeta + ' ' + subcarpeta)
  # Espero 1 segundo antes de copiar la siguiente
	print('Copiada ' + carpeta + ' a ' + subcarpeta + '...\n')
	os.system('sleep 1')
