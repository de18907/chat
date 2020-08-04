import os
from os import remove
import re
import pandas as pd
lista_archivos_chat,textos,palabras,posicion,palabra1 = [],[],[],[],[] #lista de achivos del chat
mensaje,mensaje2,mensaje3 = [],[],[]
palabra_real = []
celular, correo, ciudad = [],[],[]
data = {'Celular': [],'Correo': [],'Ciudad': []}#tabla

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
    if palabras[desde] == 'm.' and palabras[desde +1] == '-':#desde
        posicion.append(desde+1)
for jsjs in range(len(posicion)):
    if jsjs != 0:
        mensaje.append(palabras[posicion[jsjs-1]:posicion[jsjs]])
#mensajes de personas que buscan
for ver1 in range(len(mensaje)): #cuantidad de mensajes
    for ver in range(len(mensaje[ver1])): #cantidad de palabras en un mensaje
        if re.findall('busc', mensaje[ver1][ver]):
            mensaje2.append(ver1)
for mm in range(len(mensaje2)-1):
    if mensaje2[mm] != mensaje2[mm+1]:
        mensaje3.append(mensaje[mensaje2[mm+1]])
for iii in range(len(mensaje3)):
    for iiii in range(len(mensaje3[iii])):
        palabra1.append(iiii)
for papa in range(len(palabra1)):
    if palabra1[papa] == 0:
        palabra_real.append(palabra1[papa-1])#cantidad de palabras
#Palabras claves celular
nume_c = 0
for es in range(len(mensaje3)):#filtro
    nume_c += 1
    for filtrar in range(len(mensaje3[es])):
        if mensaje3[es][filtrar] == '+1':#celular
            celular.append(mensaje3[es][filtrar]+mensaje3[es][filtrar+1]+mensaje3[es][filtrar+2])
    if len(celular) != nume_c:
        celular.append(celular[len(celular)-1])
#Palabras claves correo
nume_co,num_otro,eses = 0,0, [9999999]
for es in range(len(mensaje3)):#filtro
    num_otro +=1
    for filtrar in range(len(mensaje3[es])):
        if re.findall('@',mensaje3[es][filtrar]): #corre
            eses.append(es)
            if es == eses[nume_co]:
                correo[es].append(mensaje3[es][filtrar])#agregando en el mismo mensaje
            else:
                correo.append([mensaje3[es][filtrar]])
            nume_co +=1
    if len(correo) != num_otro:
        correo.append('')
#Palabras claves ciudad,sector,lugar,av,tipo de inmueble y cualitativos
for ci in range(len(mensaje3)):#aun le falta la limpieza y organizar el codigo
    for ciu in range(len(mensaje3[ci])):
        #Ciudad
        if re.findall('santo',mensaje3[ci][ciu]) and re.findall('domingo',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('distrito',mensaje3[ci][ciu]) and re.findall('nacional',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('sto',mensaje3[ci][ciu]) and re.findall('dgo',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('juan',mensaje3[ci][ciu]) and re.findall('dolio',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('la',mensaje3[ci][ciu]) and re.findall('romana',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('punta',mensaje3[ci][ciu]) and re.findall('cana',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('cap',mensaje3[ci][ciu]) and re.findall('cana',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('las',mensaje3[ci][ciu]) and re.findall('terrenas',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('puerto',mensaje3[ci][ciu]) and re.findall('plata',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('san',mensaje3[ci][ciu]) and re.findall('isidro',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('bayahibe',mensaje3[ci][ciu]) or re.findall('bavaro',mensaje3[ci][ciu]) or re.findall('bávaro',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu])
        #Sector
        elif re.findall('zona',mensaje3[ci][ciu]) and re.findall('universitaria',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('la',mensaje3[ci][ciu]) and re.findall('esperilla',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('el',mensaje3[ci][ciu]) and re.findall('vergel',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('arroyo',mensaje3[ci][ciu]) and re.findall('hondo',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('evaristo',mensaje3[ci][ciu]) and re.findall('morales',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('la',mensaje3[ci][ciu]) and re.findall('julia',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('bella',mensaje3[ci][ciu]) and re.findall('vista',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('los',mensaje3[ci][ciu]) and re.findall('prados',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('el',mensaje3[ci][ciu]) and re.findall('millón',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('el',mensaje3[ci][ciu]) and re.findall('millon',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('urbanización',mensaje3[ci][ciu]) and re.findall('fernandez',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('urbanizacion',mensaje3[ci][ciu]) and re.findall('fernandez',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('urbanización',mensaje3[ci][ciu]) and re.findall('real',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('urbanizacion',mensaje3[ci][ciu]) and re.findall('real',mensaje3[ci][ciu+1]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('los',mensaje3[ci][ciu]) and re.findall('cacicazgos',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('el',mensaje3[ci][ciu]) and re.findall('cacique',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('las',mensaje3[ci][ciu]) and re.findall('praderas',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('mirador',mensaje3[ci][ciu]) and re.findall('norte',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('mirador',mensaje3[ci][ciu]) and re.findall('sur',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('gazcue',mensaje3[ci][ciu]) or re.findall('naco',mensaje3[ci][ciu]) or re.findall('piantini',mensaje3[ci][ciu]) or re.findall('Paraíso',mensaje3[ci][ciu]) or re.findall('Paraiso',mensaje3[ci][ciu]) or re.findall('serrallés',mensaje3[ci][ciu]) or re.findall('serralles',mensaje3[ci][ciu]) or re.findall('quisqueya',mensaje3[ci][ciu]) or re.findall('julieta',mensaje3[ci][ciu]) or re.findall('renacimiento',mensaje3[ci][ciu]) or re.findall('miradores',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        #lugar
        elif re.findall('metro',mensaje3[ci][ciu]) and re.findall('country',mensaje3[ci][ciu]) and re.findall('club',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1]+mensaje3[ci][ciu+2])
        elif re.findall('casa',mensaje3[ci][ciu]) and re.findall('de',mensaje3[ci][ciu]) and re.findall('campo',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('guavaberry',mensaje3[ci][ciu]) or re.findall('hemingway',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        #av
        elif re.findall('27',mensaje3[ci][ciu]) and re.findall('de',mensaje3[ci][ciu]) and re.findall('febrero',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1]+mensaje3[ci][ciu+2])
        elif re.findall('john',mensaje3[ci][ciu]) and re.findall('f.',mensaje3[ci][ciu]) and re.findall('kennedy',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1]+mensaje3[ci][ciu+2])
        elif re.findall('republica',mensaje3[ci][ciu]) and re.findall('de',mensaje3[ci][ciu]) and re.findall('colombia',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1]+mensaje3[ci][ciu+2])
        elif re.findall('lope',mensaje3[ci][ciu]) and re.findall('de',mensaje3[ci][ciu]) and re.findall('vega',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1]+mensaje3[ci][ciu+2])
        elif re.findall('nuñez',mensaje3[ci][ciu]) and re.findall('de',mensaje3[ci][ciu]) and re.findall('cáceres',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1]+mensaje3[ci][ciu+2])
        elif re.findall('nuñez',mensaje3[ci][ciu]) and re.findall('de',mensaje3[ci][ciu]) and re.findall('caceres',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1]+mensaje3[ci][ciu+2])
        elif re.findall('maximo',mensaje3[ci][ciu]) and re.findall('gomez',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('abraham',mensaje3[ci][ciu]) and re.findall('lincoln',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('winston',mensaje3[ci][ciu]) and re.findall('churchill',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('george',mensaje3[ci][ciu]) and re.findall('washington',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('autopista',mensaje3[ci][ciu]) and re.findall('duarte',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('carretera',mensaje3[ci][ciu]) and re.findall('mella',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('av.',mensaje3[ci][ciu]) and re.findall('circunvalación',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('av.',mensaje3[ci][ciu]) and re.findall('circunvalacion',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('tiradentes',mensaje3[ci][ciu]) or re.findall('bolivar',mensaje3[ci][ciu]) or re.findall('privada',mensaje3[ci][ciu]) or re.findall('ecológica',mensaje3[ci][ciu]) or re.findall('ecologica',mensaje3[ci][ciu]) or re.findall('anacaona',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        #tipo de inmueble 
        elif re.findall('town',mensaje3[ci][ciu]) and re.findall('house',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('apartamento',mensaje3[ci][ciu]) or re.findall('casa',mensaje3[ci][ciu]) or re.findall('solar',mensaje3[ci][ciu]) or re.findall('edificio',mensaje3[ci][ciu]) or re.findall('local',mensaje3[ci][ciu]) or re.findall('villa',mensaje3[ci][ciu]) or re.findall('finca',mensaje3[ci][ciu]) or re.findall('cabaña',mensaje3[ci][ciu]) or re.findall('condominio',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu])
        #cualitativos
        elif re.findall('family',mensaje3[ci][ciu]) and re.findall('room',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('linea',mensaje3[ci][ciu]) and re.findall('blanca',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu]+mensaje3[ci][ciu+1])
        elif re.findall('terraza',mensaje3[ci][ciu]) or re.findall('penthouse',mensaje3[ci][ciu]) or re.findall('ph',mensaje3[ci][ciu]) or re.findall('estudio',mensaje3[ci][ciu]) or re.findall('balcón',mensaje3[ci][ciu]) or re.findall('balcon',mensaje3[ci][ciu]) or re.findall('piscina',mensaje3[ci][ciu]) or re.findall('jacuzzi',mensaje3[ci][ciu]) or re.findall('aire',mensaje3[ci][ciu]) or re.findall('amueblado',mensaje3[ci][ciu]) or re.findall('marmol',mensaje3[ci][ciu]) or re.findall('vacío',mensaje3[ci][ciu]) or re.findall('vacio',mensaje3[ci][ciu]):
            ciudad.append(mensaje3[ci][ciu])




        
for h in range(len(celular)): 
    data['Celular'].append(celular[h])
    data['Correo'].append(correo[h])

df = pd.DataFrame(data, columns = ['Celular', 'Correo'])
df.to_excel('tabla.xlsx', sheet_name='Datos_de_Whatsapp')