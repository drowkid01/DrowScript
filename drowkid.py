#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os
 
def menu():
	"""
	"""
	os.system('clear')
	os.system('cd .tools;python3 .banner-kid') 
	os.system('setterm -foreground green')
	print ("")
	print ("		▁ ▂ ▄ ▅ ▆ ▇ █ Hᴇʀʀᴀᴍɪᴇɴᴛᴀꜱ ᴅɪꜱᴘᴏɴɪʙʟᴇꜱ █ ▇ ▆ ▅ ▄ ▂ ▁ ")
	print ("")
	print ("")
	os.system('setterm -half-bright on;setterm -foreground yellow')
	print ("\t1 - ░▒▓█►─═ ＤｒｏｗＳｈｉｎｇ: Hᴇʀʀᴀᴍɪᴇɴᴛᴀ ᴘʜɪꜱʜɪɴɢ +77 ꜱɪᴛɪᴏꜱ ═─►█▓▒░")
	print ("	")
	print ("\t2 - ░▒▓█►─═ ＵＲＬＫｉｄ： Aᴄᴏʀᴛᴀᴅᴏʀ URL ═─►█▓▒░")
	print ("")
	os.system('setterm -foreground cyan')
	print ("\t3 - ░▒▓█►─═ Ｂａｎｎｅｒ－ＤｒｏｗＫ: Gᴇɴᴇʀᴀᴅᴏʀ ᴅᴇ Bᴀɴɴᴇʀꜱ ═─►█▓▒░")
	print ("")
	print ("\t4 - ░▒▓█►─═ ＤｒｏｗＤＮＳ:  Dᴇᴛᴀʟʟᴇꜱ ʏ ʜᴇʀʀᴀᴍɪᴇɴᴛᴀꜱ ᴅᴇ ᴄᴏɴᴇxɪóɴ  ═─►█▓▒░")
	print ("")
	os.system('setterm -half-bright on;setterm -foreground green')
	print ("\t5 - ░▒▓█►─═ ＤｒｏｗＳＭＳ: Eɴᴠíᴀ ꜱᴍꜱ ꜱɪɴ ɴᴜᴍᴇʀᴏ ʀᴇᴍɪᴛᴇɴᴛᴇ ═─►█▓▒░")
	print ("")
	print ("\t6 - ░▒▓█►─═ ＤｒｏｗＳＯ: Iɴꜱᴛᴀʟᴀʀ ꜱᴏ ᴄᴏᴍᴏ UBUNTU Y KALI LINUX ═─►█▓▒░")
	print ("")
	os.system('setterm -foreground white;setterm -half-bright on')
	print ("\t7 - ░▒▓█►─═ ＱＲＬｉｎｋ： Generador de QR (en imagen) apartir de un link═─►█▓▒░")
	print ("")
	print ("\t8 - ░▒▓█►─═ ＣＣＧＥＮ: ɢᴇɴᴇʀᴀᴅᴏʀ ᴅᴇ ᴛᴀʀᴊᴇᴛᴀs ᴅᴇ ᴄʀᴇᴅɪᴛᴏ ═─►█▓▒░")
	print ("")
	os.system('setterm -half-bright on;setterm -foreground red')
	print ("")
	print ("")
	print ("")
	print ("")
	print ("\tx - Salir del script")
	os.system('setterm -half-bright on;setterm -foreground magenta')
	"""
	"""
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	print ("")
	opcionMenu = input("¿Qué herramienta quieres utilizar? Envía el número de opción >> ")
 
	if opcionMenu=="1":
		os.system('python3 .dshing')
		print ("")
		input("Presiona enter para regresar a DrowScript o CTRL+C para salir")
	elif opcionMenu=="2":
		os.system('cd .tools; bash .urlkid')
		print ("")
		input("Presiona enter para regresar a DrowScript o CTRL+C para salir")
	elif opcionMenu=="3":
		os.system('cd .tools;python2 .bann')
		print ("")
		input("Presiona enter para regresar a DrowScript o CTRL+C para salir")
	elif opcionMenu=="4":
		os.system('cd .tools;python2 drowdns')
		print ("")
		input("Presiona enter para regresar a DrowScript o CTRL+C para salir")
	elif opcionMenu=="5":
		os.system('cd .tools;bash drowsms.sh')
		print ("")
		input("Presiona enter para regresar a DrowScript o CTRL+C para salir")
	elif opcionMenu=="6":
		os.system('cd .so;python2 .drowk.py')
		print ("")
		input("Presiona enter para regresar a DrowScript o CTRL+C para salir")
	elif opcionMenu=="7":
		os.system('python3 .qr.py')
		print ("")
		input("Presiona enter para regresar a DrowScript o CTRL+C para salir")
	elif opcionMenu=="8":
		os.system('cd .ccgen;python2 ccgen')
		print ("")
	elif opcionMenu=="x":
		break
	else:
		print ("")
		input("Opción incorrecta..\n")
