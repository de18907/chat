import os
from os import remove
import re
lista_archivos_chat,textos,palabras,posicion,palabra1 = [],[],[],[],[] #lista de achivos del chat
mensaje,mensaje2,mensaje3 = [],[],[]
local,local_real,palabra_real = [],[],[]
tabla_no, tabla = [],[]#Buscar palabras claves
dirs1 = os.listdir("chat/")#achivos del chat
for file_chat in dirs1:
    lista_archivos_chat.append(f"chat/{file_chat}")   
#leer el texto y add como palabras
for texto in lista_archivos_chat:
    f_obj = open(texto)
    mirar = f_obj.read()
    if mirar != "" or mirar != " ":
        limpio = mirar.lower()
        textos.append(limpio.split())
for textos1 in textos:
    for textos0 in textos1:
        palabras.append(textos0)
for desde in range(len(palabras)):
    if palabras[desde] == 'p.' and palabras[desde +1] == 'm.':#desde
        posicion.append(desde+2)
for jsjs in range(len(posicion)):
    if jsjs != 0:
        mensaje.append(palabras[posicion[jsjs-1]:posicion[jsjs]])
#mensajes de personas que buscan
for ver1 in range(len(mensaje)): #cuantidad de mensajes
    for ver in range(len(mensaje[ver1])): #cantidad de palabras en un mensaje
        if re.findall('busc', mensaje[ver1][ver]):
            mensaje2.append(ver1)
locales=-1
for mm in range(len(mensaje2)-1):
    if mensaje2[mm] != mensaje2[mm+1]:
        mensaje3.append(mensaje[mensaje2[mm+1]])
        locales+=1
        local.append(locales)
local_real.append(len(local))#cantidad de mensajes que buscan
for iii in range(len(mensaje3)):
    for iiii in range(len(mensaje3[iii])):
        palabra1.append(iiii)
for papa in range(len(palabra1)):
    if palabra1[papa] == 0:
        palabra_real.append(palabra1[papa-1])#cantidad de palabras




#tabla = []
#for tce in range(len(celular)-1):
#    tabla.append([celular[tce]])
#for tco in range(len(correo)-1):
#    tabla[tco].append(correo[tco])



#Palabras claves celular,ciudad, zona
for es in range(local_real[0]):#filtro
    for filtrar in range(len(mensaje3[es])):
        if mensaje3[es][filtrar] == '+1':#celular
            tabla_no.append(mensaje3[es][filtrar]+mensaje3[es][filtrar+1]+mensaje3[es][filtrar+2])
        elif re.findall('@',mensaje3[es][filtrar]): #corre
            tabla_no.append(mensaje3[es][filtrar])   

#for dentro in range(len(tabla_no)):
    #if re.findall('+1',tabla_no[dentro]):
    #    print(tabla_no[dentro])

#eliminar archivo final
#dirs2 = os.listdir("resultado/")
#for file_final in dirs2:
#    remove(f"resultado/{file_final}")
#Escribir en el archivo
#file = open("resultado/final.txt", "w")
#for inininin in limpio:
#    file.write(str(mensaje) + os.linesep)
#file.close()

import openpyxl
wb = openpyxl.Workbook()
hoja = wb.active
hoja.append(['Celular', 'Correo'])# Crea la fila del encabezado con los títulos

#bb = 0
#for tc in celular:
#    tabla[bb].append([tc])
#    bb += 1
#for producto in tabla:
    #producto es una tupla con los valores de un producto 
#    hoja.append(producto)

wb.save('tabla.xlsx')