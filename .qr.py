#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os
 
def menu():
	"""
	"""
	os.system('clear')
	os.system('cd .tools;bash .b') 
	os.system('setterm -foreground green')
	print ("")
	print ("")
	print ("		 	▁ ▂ ▄ ▅ ▆ ▇ █ ɢᴜíᴀ ᴅᴇ ᴜsᴏ █ ▇ ▆ ▅ ▄ ▂ ▁")
	print ("")
	print ("")
	print (" 	░▒▓█►─═ ＱＲＬｉｎｋ： ɢᴇɴᴇʀᴀᴅᴏʀ ᴅᴇ ǫʀ (ᴇɴ ɪᴍɢ) ᴀᴘᴀʀᴛɪʀ ᴅᴇ ᴜɴ ᴇɴʟᴀᴄᴇ ═─►█▓▒░")
	print ("	")
	os.system('setterm -foreground white;setterm -half-bright on')
	print ("")
	print ("")
	print (" 		ᴀʟ ᴀʙʀɪʀ ʟᴀ ʜᴇʀʀᴀᴍɪᴇɴᴛᴀ, ᴇꜱᴄʀɪʙᴇ ᴇʟ <ʟɪɴᴋ> ʏ ᴅᴇꜱᴘᴜᴇꜱ <ᴘᴀᴛʜ>; ")
	print ("")
	print ("		ᴇꜱ ᴅᴇᴄɪʀ; https://drowkid.bswc.net  /ꜱᴛᴏʀᴀɢᴇ/ᴅᴏᴡɴʟᴏᴀᴅꜱ/")
	print ("				<link>			 <path>")
	print ("")
	os.system('setterm -half-bright on;setterm -foreground green')
	print ("")
	print ("		 Después, escribe el nombre con el que deseas guardar el qr")
	print ("")
	print (" 		 Ejemplo: drowkidqr.png")
	print ("")
	print ("")
	os.system('setterm -foreground yellow')
	print ("")
	print ("		▌│█║▌║▌║ ¿ʏᴀ ᴇɴᴛᴇɴᴅɪsᴛᴇ ᴄᴏᴍᴏ ᴜsᴀʀ ǫʀʟɪɴᴋ? ║▌║▌║█│▌ ")
	print ("")
	print ("")
	print ("")
	os.system('setterm -foreground cyan')
	print ("\tA - Ir a QRLink")
	print ("")
	print ("")
	print ("\tB - Salir")
	os.system('setterm -half-bright on;setterm -foreground cyan')
	"""
	"""
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	print ("")
	opcionMenu = input("Envía el número de opción >> ")
 
	if opcionMenu=="A":
		os.system('bash .qrlink.sh')
		print ("")
		input("Presiona enter para regresar a DrowScript o CTRL+C para salir")
	elif opcionMenu=="a":
		os.system('bash .qrlink.sh')
	elif opcionMenu=="b":
		break
	elif opcionMenu=="B":
		break
	else:
		print ("")
		input("Opción incorrecta..\n")
