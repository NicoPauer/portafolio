#!/usr/bin/python3

'''
	Autor: Nicolás Pauer
	Fecha: 02/07/2023
	Descripcion: Copia un archivo a partir de plantilla a una o varias carpetas
'''

import os

# Digo de que va el programa
print('Copia uno o varios archivos a varias carpetas.\n')

seguir = 'si'

while ((seguir == 'si') or (seguir == 'Si') or (seguir == 's') or (seguir == 'S')):
   # Actualizo nombre de plantilla	
	plantilla = input('Ingrese ruta de archivo a copiar: ')
   # Actulizo nombre de carpeta	
	carpeta = input('Ingrese nombre de carpeta: ')	
   # Voy mostrando progreso al usuario
	print('Copiando plantilla ' + plantilla + ' a  carpeta ' + carpeta + '...\n')
   # Hago una pausa cortita para tranquilizar al usuario y no le agarre deseperación	
	os.system('sleep 1')
   # Copio el archivo a la carpeta	
	os.system('cp -R ' + plantilla + ' ' + carpeta)
   # Pregunto al usuario si desea seguir	
	seguir = input('Desea seguir si/no: ')
