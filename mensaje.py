import os
import re
from archivo import archivos
class mensajes:
    posicion, posicion2 = [],[] #lista de achivos del chat
    mensaje1,mensaje2,mensaje5,mensaje4,mensaje3 = [],[],[],[[]],[]
    for texto in archivos.lista_archivos_chat:
        mirar = open(texto).read()
        if mirar != "" or mirar != " ":
            palabras = mirar.lower().split()
            for desde in range(len(palabras)):
                if palabras[desde] == 'm.' and palabras[desde +1] == '-':
                    posicion.append(desde-3)
    for jsjs in range(len(posicion)):
        mensaje1.append(palabras[posicion[jsjs-1]:posicion[jsjs]])#aqui se agrega el mensaje por fechas
    for ver1 in range(len(mensaje1)): #cantidad de mensajes
        for ver in range(len(mensaje1[ver1])): #cantidad de palabras en un mensaje
            if re.findall('busc', mensaje1[ver1][ver]):
                mensaje2.append(ver1)
    for mm in range(len(mensaje2)-1):
        if mensaje2[mm] != mensaje2[mm+1]:
            mensaje3.append(mensaje1[mensaje2[mm+1]])
    for tt in range(len(mensaje3)):
        aqui = []
        for jj in range(len(mensaje3[tt])):
            if mensaje3[tt][jj] == 'm.' and mensaje3[tt][jj+1] == '-':
                if mensaje3[tt][jj+2] == '+1' and mensaje3[tt][jj+3] == mensaje3[tt-1][jj+3] and mensaje3[tt][jj+4] == mensaje3[tt-1][jj+4] and mensaje3[tt][jj+5] == mensaje3[tt-1][jj+5]:
                    aqui.append(tt)
                elif mensaje3[tt][jj+2] != '+1' and mensaje3[tt][jj+2] == mensaje3[tt-1][jj+2] and mensaje3[tt][jj+3] == mensaje3[tt-1][jj+3]:
                    aqui.append(tt)
        if len(aqui) == 1:
            posicion2.append(aqui[0])
    agregar = 0
    for hh in range(len(posicion2)):
        if posicion2[hh] == posicion2[hh-1]+1:
            mensaje4[agregar].append(mensaje3[posicion2[hh]])
        else:
            mensaje4.append([mensaje3[posicion2[hh]]])
            agregar += 1
    for md in range(len(mensaje4)):
        if mensaje4[md] != []:
            mensaje5.append(mensaje4[md][0])