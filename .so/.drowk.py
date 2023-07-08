#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opción")
	print ("\t1 - Instalar Ubuntu 20.04 (Terminal)")
	print ("")
	print ("\t2 - Instalar Ubuntu 20.04 (RDP)")
	print ("")
	print ("\t3 - Instalar Kali Linux (Terminal)")
	print ("")
	print ("\t4 - Instalar Kali Linux (RDP)")
	print ("")
	print ("\t9 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		os.system('bash .drow-ubuntu')
		print ("")
		input("Has pulsado la opción 1...\npulsa una tecla para continuar")
	elif opcionMenu=="2":
		os.system('bash .drow-ubunturdp')
		print ("")
		input("Has pulsado la opción 2...\npulsa una tecla para continuar")
	elif opcionMenu=="3":
		os.system('bash .drow-linux')
		print ("")
		input("Has pulsado la opción 3...\npulsa una tecla para continuar")
	elif opcionMenu=="4":
		os.system('bash .drow-linuxrdp')
		input("")
	elif opcionMenu=="9":
		break
	else:
		print ("")
