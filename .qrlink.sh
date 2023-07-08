#!/bin/bash
#
# QRLink: Open Source
# Licencia: General Public License
# Sistema: GNU/linux
# Fecha: 06-05-2022
# 
#
# ==============================================
#                   Variables
# ==============================================
operatingSystem=$(uname -o)
deviceArchitecture=$(uname -m)
showPath=$(pwd)
link=$1
save=$2
# ==============================================
#                  Light colors
# ==============================================
black="\e[1;30m"
blue="\e[1;34m"
green="\e[1;32m"
cyan="\e[1;36m"
red="\e[1;31m"
purple="\e[1;35m"
yellow="\e[1;33m"
white="\e[1;37m"
# ==============================================
#                  Dark colors
# ==============================================
blackDark="\e[0;30m"
blueDark="\e[0;34m"
greenDark="\e[0;32m"
cyanDark="\e[0;36m"
redDark="\e[0;31m"
purpleDark="\e[0;35m"
yellowDark="\e[0;33m"
whiteDark="\e[0;37m"
# ==============================================
#               Background colors
# ==============================================
blackBack=$(setterm -background black)
blueBack=$(setterm -background blue)
greenBack=$(setterm -background green)
cyanBack=$(setterm -background cyan)
redBack=$(setterm -background red)
yellowBack=$(setterm -background yellow)
whiteBack=$(setterm -background white)
# ==============================================
#             Installing dependencies
# ==============================================
function dependencies() {
    if [[ "${operatingSystem}" == "Android" ]]; then
	apt="pkg"
	python="python"
    else
	apt="apt"
	python="python3"
    fi
    python3=$(command -v python3)
    if [[ "${python3}" == "" ]]; then
	echo -e ${red}"
[${green}*${red}] ${green}Installing dependencies..."${white}
	${apt} update && ${apt} upgrade -y
	${apt} install ${python} -y
	python3 -m pip install --upgrade pip
	python3 -m pip install -r .requirements.txt
    fi
}
# ==============================================
#                Banner QRLink
# ==============================================
function qrlink() {
    sleep 0.5
    clear
    echo -e ${green}"
 ▄▄▄▄▄▄▄  ▄ ▄▄ ▄▄▄▄▄▄▄
 █ ▄▄▄ █ ██ ▀▄ █ ▄▄▄ █   ${blackDark}${whiteBack}  ______  ______   ${blackBack}${green}
 █ ███ █ ▄▀ ▀▄ █ ███ █   ${blackDark}${whiteBack}  ██████╗ ██████╗  ${blackBack}${green} ██╗     ██╗███╗   ██╗██╗  ██╗
 █▄▄▄▄▄█ █ ▄▀█ █▄▄▄▄▄█   ${blackDark}${whiteBack} ██╔═══██╗██╔══██╗ ${blackBack}${green} ██║     ██║████╗  ██║██║ ██╔╝
 ▄▄ ▄  ▄▄▀██▀▀ ▄▄▄ ▄▄    ${blackDark}${whiteBack} ██║   ██║██████╔╝ ${blackBack}${green} ██║     ██║██╔██╗ ██║█████╔╝
 ▄██ ▀ ▄ █▄▀ ▄ ▄█▀▀  ▄   ${blackDark}${whiteBack} ██║▄▄ ██║██╔══██╗ ${blackBack}${green} ██║     ██║██║╚██╗██║██╔═██╗
 █▀█▄▄█▄ ▀▀▄▀▄▄▀ ▀▀▄ █   ${blackDark}${whiteBack} ╚██████╔╝██║  ██║ ${blackBack}${green} ███████╗██║██║ ╚████║██║  ██╗
 ▄▄▄▄▄▄▄ █ ▄▀  ▄█▄▄██    ${blackDark}${whiteBack}  ╚══▀▀═╝ ╚═╝  ╚═╝ ${blackBack}${green} ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
 █ ▄▄▄ █  ▄▄█▀█▄ ▀ ▄▄ 
 █ ███ █ ▀▀█▀▄  ██ ▀▀█   .:.:. ${white}QR Generator Tool coded by: @drowkid01 ${green}.:.:.
 █▄▄▄▄▄█ █▀ ▄▄▀▀ █▄ ▄               ${green}${redBack}.:.:. ${white}@drowkid01 ${green}.:.:.${blackBack}
"${white}
}
# ==============================================
#                   Arguments
# ==============================================
function arguments() {
    qrlink
    cp .qrlink.py backup.py
    sed -i "s!TEXT!${link}!g" .qrlink.py
    sed -i "s!PATH!${save}!g" .qrlink.py
    python3 .qrlink.py
    rm .qrlink.py
    mv backup.py .qrlink.py
    echo -e ${green}"
[${white}√${green}] QR code image saved:${white} ${save}
"
}
# ==============================================
#                  Interactive
# ==============================================
function interactive() {
    qrlink
    echo -e -n ${green}"
[${white}*${green}] Escribe el link: "${white}
    read -r link
    sleep 0.5
    echo -e -n ${green}"
[${white}*${green}] Escribe el nombre de la imagen qr (sin .png): "${white}
    read -r save
    sleep 0.5
    cp .qrlink.py backup.py
    sed -i "s!TEXT!${link}!g" .qrlink.py
    sed -i "s!PATH!${save}!g" .qrlink.py
    python3 .qrlink.py
    rm .qrlink.py
    mv backup.py .qrlink.py
    echo -e ${green}"
[${white}√${green}] QR code guardado:${white} ${save}
"
}
# ==============================================
#              Declaring functions
# ==============================================
dependencies
if [[ "${link}" == "" ]]; then
    interactive
else
    arguments
fi
echo -e ${red} "CTRL+C PARA SALIR"
# ==============================================
#    Creado por: @DrowKid01 - DrowKid ©2022
# ==============================================
