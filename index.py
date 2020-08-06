import os
from os import remove
import re
import pandas as pd
lista_archivos_chat,textos,palabras,posicion = [],[],[],[] #lista de achivos del chat
mensaje,mensaje2,mensaje3 = [],[],[]
celular, correo, ciudad, sector, lugar, av, tipo, cualitativos = [],[],[],[],[],[],[],[]
data = {'Celular': [],'Correo': [],'Ciudad': [],'Sector': [],'Lugar': [],'Av. Principal (Sto. Dgo.)': [],'Tipo de inmueble': [],'Cualitativos': []}#tabla
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
    mensaje.append(palabras[posicion[jsjs-1]:posicion[jsjs]])
for ver1 in range(len(mensaje)): #cuantidad de mensajes
    for ver in range(len(mensaje[ver1])): #cantidad de palabras en un mensaje
        if re.findall('busc', mensaje[ver1][ver]):
            mensaje2.append(ver1)
for mm in range(len(mensaje2)-1):
    if mensaje2[mm] != mensaje2[mm+1]:
        mensaje3.append(mensaje[mensaje2[mm+1]])
#Palabras claves celular y correo
nume_c,nume_co,na,na_sect,na_lug,na_av,na_tipo,na_cuali,eses,cuidd,sect,lug,avv,tip,cuali = 0,0,[],[],[],[],[],[],[9999999],[9999999],[9999999],[9999999],[9999999],[9999999],[9999999]
for es in range(len(mensaje3)):#filtro
    nume_c += 1
    for filtrar in range(len(mensaje3[es])):
        #celular
        if mensaje3[es][filtrar] == '+1':
            celular.append(mensaje3[es][filtrar]+mensaje3[es][filtrar+1]+mensaje3[es][filtrar+2])
        #corre
        if re.findall('@',mensaje3[es][filtrar]): 
            eses.append(es)
            if es == eses[nume_co]:
                correo[es].append(mensaje3[es][filtrar])#agregando en el mismo mensaje
            else:
                correo.append([mensaje3[es][filtrar]])
            nume_co +=1
        #Ciudad
        if re.findall('santo',mensaje3[es][filtrar]) and re.findall('domingo',mensaje3[es][filtrar+1]):
            cuidd.append(es)
            na.append(es)
            if es == cuidd[len(na)-1]:
                ciudad[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                ciudad.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('distrito',mensaje3[es][filtrar]) and re.findall('nacional',mensaje3[es][filtrar+1]):
            cuidd.append(es)
            na.append(es)
            if es == cuidd[len(na)-1]:
                ciudad[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                ciudad.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('sto',mensaje3[es][filtrar]) and re.findall('dgo',mensaje3[es][filtrar+1]):
            cuidd.append(es)
            na.append(es)
            if es == cuidd[len(na)-1]:
                ciudad[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                ciudad.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('juan',mensaje3[es][filtrar]) and re.findall('dolio',mensaje3[es][filtrar+1]):
            cuidd.append(es)
            na.append(es)
            if es == cuidd[len(na)-1]:
                ciudad[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                ciudad.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('la',mensaje3[es][filtrar]) and re.findall('romana',mensaje3[es][filtrar+1]):
            cuidd.append(es)
            na.append(es)
            if es == cuidd[len(na)-1]:
                ciudad[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                ciudad.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('punta',mensaje3[es][filtrar]) and re.findall('cana',mensaje3[es][filtrar+1]):
            cuidd.append(es)
            na.append(es)
            if es == cuidd[len(na)-1]:
                ciudad[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                ciudad.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('cap',mensaje3[es][filtrar]) and re.findall('cana',mensaje3[es][filtrar+1]):
            cuidd.append(es)
            na.append(es)
            if es == cuidd[len(na)-1]:
                ciudad[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                ciudad.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('las',mensaje3[es][filtrar]) and re.findall('terrenas',mensaje3[es][filtrar+1]):
            cuidd.append(es)
            na.append(es)
            if es == cuidd[len(na)-1]:
                ciudad[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                ciudad.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('puerto',mensaje3[es][filtrar]) and re.findall('plata',mensaje3[es][filtrar+1]):
            cuidd.append(es)
            na.append(es)
            if es == cuidd[len(na)-1]:
                ciudad[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                ciudad.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('san',mensaje3[es][filtrar]) and re.findall('isidro',mensaje3[es][filtrar+1]):
            cuidd.append(es)
            na.append(es)
            if es == cuidd[len(na)-1]:
                ciudad[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                ciudad.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('bayahibe',mensaje3[es][filtrar]) or re.findall('bavaro',mensaje3[es][filtrar]) or re.findall('bávaro',mensaje3[es][filtrar]):
            cuidd.append(es)
            na.append(es)
            if es == cuidd[len(na)-1]:
                ciudad[es].append(mensaje3[es][filtrar])
            else:
                ciudad.append([mensaje3[es][filtrar]])
        #Sector
        elif re.findall('zona',mensaje3[es][filtrar]) and re.findall('universitaria',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('la',mensaje3[es][filtrar]) and re.findall('esperilla',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('el',mensaje3[es][filtrar]) and re.findall('vergel',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('arroyo',mensaje3[es][filtrar]) and re.findall('hondo',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('evaristo',mensaje3[es][filtrar]) and re.findall('morales',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('la',mensaje3[es][filtrar]) and re.findall('julia',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('bella',mensaje3[es][filtrar]) and re.findall('vista',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('los',mensaje3[es][filtrar]) and re.findall('prados',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('el',mensaje3[es][filtrar]) and re.findall('millón',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('el',mensaje3[es][filtrar]) and re.findall('millon',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('urbanización',mensaje3[es][filtrar]) and re.findall('fernandez',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('urbanizacion',mensaje3[es][filtrar]) and re.findall('fernandez',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('urbanización',mensaje3[es][filtrar]) and re.findall('real',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('urbanizacion',mensaje3[es][filtrar]) and re.findall('real',mensaje3[es][filtrar+1]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('los',mensaje3[es][filtrar]) and re.findall('cacicazgos',mensaje3[es][filtrar]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('el',mensaje3[es][filtrar]) and re.findall('cacique',mensaje3[es][filtrar]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('las',mensaje3[es][filtrar]) and re.findall('praderas',mensaje3[es][filtrar]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('mirador',mensaje3[es][filtrar]) and re.findall('norte',mensaje3[es][filtrar]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('mirador',mensaje3[es][filtrar]) and re.findall('sur',mensaje3[es][filtrar]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('gazcue',mensaje3[es][filtrar]) or re.findall('naco',mensaje3[es][filtrar]) or re.findall('piantini',mensaje3[es][filtrar]) or re.findall('Paraíso',mensaje3[es][filtrar]) or re.findall('Paraiso',mensaje3[es][filtrar]) or re.findall('serrallés',mensaje3[es][filtrar]) or re.findall('serralles',mensaje3[es][filtrar]) or re.findall('quisqueya',mensaje3[es][filtrar]) or re.findall('julieta',mensaje3[es][filtrar]) or re.findall('renacimiento',mensaje3[es][filtrar]) or re.findall('miradores',mensaje3[es][filtrar]):
            sect.append(es)
            na_sect.append(es)
            if es == sect[len(na_sect)-1]:
                sector[es].append(mensaje3[es][filtrar])
            else:
                sector.append([mensaje3[es][filtrar]])
        #lugar
        elif re.findall('metro',mensaje3[es][filtrar]) and re.findall('country',mensaje3[es][filtrar]) and re.findall('club',mensaje3[es][filtrar]):
            lug.append(es)
            na_lug.append(es)
            if es == lug[len(na_lug)-1]:
                lugar[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}')
            else:
                lugar.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}'])
        elif re.findall('casa',mensaje3[es][filtrar]) and re.findall('de',mensaje3[es][filtrar]) and re.findall('campo',mensaje3[es][filtrar]):
            lug.append(es)
            na_lug.append(es)
            if es == lug[len(na_lug)-1]:
                lugar[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}')
            else:
                lugar.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}'])
        elif re.findall('guavaberry',mensaje3[es][filtrar]) or re.findall('hemingway',mensaje3[es][filtrar]):
            lug.append(es)
            na_lug.append(es)
            if es == lug[len(na_lug)-1]:
                lugar[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                lugar.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        #av
        elif re.findall('27',mensaje3[es][filtrar]) and re.findall('de',mensaje3[es][filtrar]) and re.findall('febrero',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}'])
        elif re.findall('john',mensaje3[es][filtrar]) and re.findall('f.',mensaje3[es][filtrar]) and re.findall('kennedy',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}'])
        elif re.findall('republica',mensaje3[es][filtrar]) and re.findall('de',mensaje3[es][filtrar]) and re.findall('colombia',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}'])
        elif re.findall('lope',mensaje3[es][filtrar]) and re.findall('de',mensaje3[es][filtrar]) and re.findall('vega',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}'])
        elif re.findall('nuñez',mensaje3[es][filtrar]) and re.findall('de',mensaje3[es][filtrar]) and re.findall('cáceres',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}'])
        elif re.findall('nuñez',mensaje3[es][filtrar]) and re.findall('de',mensaje3[es][filtrar]) and re.findall('caceres',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]} {mensaje3[es][filtrar+2]}'])
        elif re.findall('maximo',mensaje3[es][filtrar]) and re.findall('gomez',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('abraham',mensaje3[es][filtrar]) and re.findall('lincoln',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('winston',mensaje3[es][filtrar]) and re.findall('churchill',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('george',mensaje3[es][filtrar]) and re.findall('washington',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('autopista',mensaje3[es][filtrar]) and re.findall('duarte',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('carretera',mensaje3[es][filtrar]) and re.findall('mella',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('av.',mensaje3[es][filtrar]) and re.findall('circunvalación',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('av.',mensaje3[es][filtrar]) and re.findall('circunvalacion',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                av.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('tiradentes',mensaje3[es][filtrar]) or re.findall('bolivar',mensaje3[es][filtrar]) or re.findall('privada',mensaje3[es][filtrar]) or re.findall('ecológica',mensaje3[es][filtrar]) or re.findall('ecologica',mensaje3[es][filtrar]) or re.findall('anacaona',mensaje3[es][filtrar]):
            avv.append(es)
            na_av.append(es)
            if es == avv[len(na_av)-1]:
                av[es].append(mensaje3[es][filtrar])
            else:
                av.append([mensaje3[es][filtrar]])
        #tipo de inmueble 
        elif re.findall('town',mensaje3[es][filtrar]) and re.findall('house',mensaje3[es][filtrar]):
            tip.append(es)
            na_tipo.append(es)
            if es == tip[len(na_tipo)-1]:
                tipo[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                tipo.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('apartamento',mensaje3[es][filtrar]) or re.findall('casa',mensaje3[es][filtrar]) or re.findall('solar',mensaje3[es][filtrar]) or re.findall('edificio',mensaje3[es][filtrar]) or re.findall('local',mensaje3[es][filtrar]) or re.findall('villa',mensaje3[es][filtrar]) or re.findall('finca',mensaje3[es][filtrar]) or re.findall('cabaña',mensaje3[es][filtrar]) or re.findall('condominio',mensaje3[es][filtrar]): 
            tip.append(es)
            na_tipo.append(es)
            if es == tip[len(na_tipo)-1]:
                tipo[es].append(mensaje3[es][filtrar])
            else:
                tipo.append([mensaje3[es][filtrar]])
        #cualitativos
        elif re.findall('family',mensaje3[es][filtrar]) and re.findall('room',mensaje3[es][filtrar]):
            cuali.append(es)
            na_cuali.append(es)
            if es == cuali[len(na_cuali)-1]:
                cualitativos[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                cualitativos.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('linea',mensaje3[es][filtrar]) and re.findall('blanca',mensaje3[es][filtrar]):
            cuali.append(es)
            na_cuali.append(es)
            if es == cuali[len(na_cuali)-1]:
                cualitativos[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
            else:
                cualitativos.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
        elif re.findall('terraza',mensaje3[es][filtrar]) or re.findall('penthouse',mensaje3[es][filtrar]) or re.findall('ph',mensaje3[es][filtrar]) or re.findall('estudio',mensaje3[es][filtrar]) or re.findall('balcón',mensaje3[es][filtrar]) or re.findall('balcon',mensaje3[es][filtrar]) or re.findall('piscina',mensaje3[es][filtrar]) or re.findall('jacuzzi',mensaje3[es][filtrar]) or re.findall('aire',mensaje3[es][filtrar]) or re.findall('amueblado',mensaje3[es][filtrar]) or re.findall('marmol',mensaje3[es][filtrar]) or re.findall('vacío',mensaje3[es][filtrar]) or re.findall('vacio',mensaje3[es][filtrar]):
            cuali.append(es)
            na_cuali.append(es)
            if es == cuali[len(na_cuali)-1]:
                cualitativos[es].append(mensaje3[es][filtrar])
            else:
                cualitativos.append([mensaje3[es][filtrar]])
    if len(celular) != nume_c:
        celular.append(celular[len(celular)-1])
    if len(correo) != nume_c:
        correo.append('')
    if len(ciudad) != nume_c:
        ciudad.append('')
    if len(sector) != nume_c:
        sector.append('')
    if len(lugar) != nume_c:
        lugar.append('')
    if len(av) != nume_c:
        av.append('')
    if len(tipo) != nume_c:
        tipo.append('')
    if len(cualitativos) != nume_c:
        cualitativos.append('')
#para subir los datos al excel
for h in range(len(celular)): 
    data['Celular'].append(celular[h])
    data['Correo'].append(correo[h])
    data['Ciudad'].append(ciudad[h])
    data['Sector'].append(sector[h])
    data['Lugar'].append(lugar[h])
    data['Av. Principal (Sto. Dgo.)'].append(av[h])
    data['Tipo de inmueble'].append(tipo[h])
    data['Cualitativos'].append(cualitativos[h])
df = pd.DataFrame(data, columns = ['Celular','Correo','Ciudad','Sector','Lugar','Av. Principal (Sto. Dgo.)','Tipo de inmueble','Cualitativos'])
df.to_excel('tabla.xlsx', sheet_name='Datos_de_Whatsapp')

print(mensaje3[2900])