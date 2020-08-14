import os
import re
from archivo import archivos
class mensajes:
    posicion = []#lista de achivos del chat
    mensaje1,mensaje2,mensaje3 = [],[],[]
    for texto in archivos.lista_archivos_chat:
        mirar = open(texto).read()
        if mirar != "" or mirar != " ":
            palabras = mirar.lower().split()
            for desde in range(len(palabras)):
                if palabras[desde] == 'm.' and palabras[desde +1] == '-':
                    posicion.append(desde-3)
    for jsjs in range(len(posicion)):
        if palabras[posicion[jsjs-1]:posicion[jsjs]] != []:
            mensaje1.append(palabras[posicion[jsjs-1]:posicion[jsjs]])#aqui se agrega el mensaje por fechas
    aqui = -1
    for ver1 in range(len(mensaje1)):#si el mensaje anterior es de la misma persona entonces este agregamelo al anterior de lo contrario creame un array con el mensaje nuevo
        for ver2 in range(len(mensaje1[ver1])):
            if mensaje1[ver1][ver2] == 'm.' and mensaje1[ver1][ver2+1] == '-':
                if mensaje1[ver1][ver2+2] == '+1' and mensaje1[ver1][ver2+3] == mensaje1[ver1-1][ver2+3] and mensaje1[ver1][ver2+4] == mensaje1[ver1-1][ver2+4]:
                    mensaje2[aqui].append(' '.join(mensaje1[ver1]))
                elif mensaje1[ver1][ver2+2] == '+34' and mensaje1[ver1][ver2+3] == mensaje1[ver1-1][ver2+3] and mensaje1[ver1][ver2+4] == mensaje1[ver1-1][ver2+4] and mensaje1[ver1][ver2+5] == mensaje1[ver1-1][ver2+5]:
                    mensaje2[aqui].append(' '.join(mensaje1[ver1]))
                elif mensaje1[ver1][ver2+2] != '+1' and mensaje1[ver1][ver2+2] != '+34' and mensaje1[ver1][ver2+2] == mensaje1[ver1-1][ver2+2] and mensaje1[ver1][ver2+3] == mensaje1[ver1-1][ver2+3]:
                    mensaje2[aqui].append(' '.join(mensaje1[ver1]))
                else:
                    mensaje2.append([' '.join(mensaje1[ver1])])
                    aqui += 1
    for na in range(len(mensaje2)):#agrega los que dicen busco
        q = na
        for an in range(len(mensaje2[na][0].split())):
            if re.findall('busc', mensaje2[na][0].split()[an]):
                if na == q:
                    mensaje3.append(mensaje2[na][0].split())
                    q = na + 1 