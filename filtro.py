import os
from os import remove
import re
import pandas as pd
from tkinter import *
from mensaje import mensajes
def filtrarr(root):
    mensaje3 = mensajes.mensaje3
    fecha,celular,correo, ciudad, sector, lugar, av, tipo, cualitativos,bano, habitaciones, monto = [],[],[],[],[],[],[],[],[],[],[],[]
    data = {'Fecha': [],'Nombre y Celular': [],'Correo': [],'Ciudad': [],'Sector': [],'Lugar': [],'Av. Principal (Sto. Dgo.)': [],'Tipo de inmueble': [],'Cualitativos': [],'Baño': [],'Habitaciones': [],'Monto': [],'Descripcion': []}#tabla
    na_sect,na_ci,na_monto,na_tipo,na_habitacion,na_bano,na_cuali,na_av,hab,ciud,ban,mon,cuali,tip,avv,sect=[],[],[],[],[],[],[],[],[9999999999],[9999999999],[9999999999],[9999999999],[9999999999],[9999999999],[9999999999],[9999999999]
    #Palabras claves celular y correo
    nume_c = 1
    for es in range(len(mensaje3)):#filtro
        na_co = es
        for filtrar in range(len(mensaje3[es])):
            if mensaje3[es][filtrar] == 'm.' and mensaje3[es][filtrar+1] == '-':
                #fecha
                if re.findall('/', mensaje3[es][filtrar-3]):
                    fecha.append(mensaje3[es][filtrar-3])
                #celular
                if mensaje3[es][filtrar+2] == '+1':
                    celular.append(f'{mensaje3[es][filtrar+2]}-{mensaje3[es][filtrar+3]}-{mensaje3[es][filtrar+4]}')
                elif mensaje3[es][filtrar+2] == '+34':
                    celular.append(f'{mensaje3[es][filtrar+2]}-({mensaje3[es][filtrar+3]})-{mensaje3[es][filtrar+4]}-{mensaje3[es][filtrar+5]}-{mensaje3[es][filtrar+6]}')
                elif mensaje3[es][filtrar+2] != '+1' and mensaje3[es][filtrar+2] != '+34': #
                    if re.findall(':',mensaje3[es][filtrar+2]):
                        celular.append(mensaje3[es][filtrar+2])
                    elif re.findall(':',mensaje3[es][filtrar+3]):
                        celular.append(f'{mensaje3[es][filtrar+2]} {mensaje3[es][filtrar+3]}')
                    elif re.findall(':',mensaje3[es][filtrar+4]):
                        celular.append(f'{mensaje3[es][filtrar+2]} {mensaje3[es][filtrar+3]} {mensaje3[es][filtrar+4]}')
                    elif re.findall(':',mensaje3[es][filtrar+5]):
                        celular.append(f'{mensaje3[es][filtrar+2]} {mensaje3[es][filtrar+3]} {mensaje3[es][filtrar+4]} {mensaje3[es][filtrar+5]}')
                    else:
                        celular.append(f'{mensaje3[es][filtrar+2]} {mensaje3[es][filtrar+3]} {mensaje3[es][filtrar+4]} {mensaje3[es][filtrar+5]}')
            #corre
            if re.findall('@',mensaje3[es][filtrar]):
                if es == na_co: 
                    correo.append([mensaje3[es][filtrar]])
                    na_co +=1
                else: 
                    correo[nume_c-1].append(mensaje3[es][filtrar])   
            #tipo de inmueble 
            if re.findall('town',mensaje3[es][filtrar]) and re.findall('house',mensaje3[es][filtrar+1]):
                tip.append(es)
                na_tipo.append(es)
                if es == tip[len(na_tipo)-1]:
                    tipo[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
                else:
                    tipo.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
            elif re.findall('apartamento',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('casa',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('solar',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('edificio',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('local',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('villa',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('finca',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('cabaña',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('condominio',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]): 
                tip.append(es)
                na_tipo.append(es)
                if es == tip[len(na_tipo)-1]:
                    tipo[es].append(mensaje3[es][filtrar])
                else:
                    tipo.append([mensaje3[es][filtrar]])
            #habitacion    
            if re.findall('hab',mensaje3[es][filtrar]) and re.findall('1',mensaje3[es][filtrar-1]) or re.findall('hab',mensaje3[es][filtrar]) and re.findall('2',mensaje3[es][filtrar-1]) or re.findall('hab',mensaje3[es][filtrar]) and re.findall('3',mensaje3[es][filtrar-1]) or re.findall('hab',mensaje3[es][filtrar]) and re.findall('4',mensaje3[es][filtrar-1]) or re.findall('hab',mensaje3[es][filtrar]) and re.findall('5',mensaje3[es][filtrar-1]) or re.findall('hab',mensaje3[es][filtrar]) and re.findall('6',mensaje3[es][filtrar-1]) or re.findall('hab',mensaje3[es][filtrar]) and re.findall('uno',mensaje3[es][filtrar-1]) or re.findall('hab',mensaje3[es][filtrar]) and re.findall('dos',mensaje3[es][filtrar-1]) or re.findall('hab',mensaje3[es][filtrar]) and re.findall('tres',mensaje3[es][filtrar-1]) or re.findall('hab',mensaje3[es][filtrar]) and re.findall('cuatro',mensaje3[es][filtrar-1]) or re.findall('hab',mensaje3[es][filtrar]) and re.findall('cinco',mensaje3[es][filtrar-1]) or re.findall('hab',mensaje3[es][filtrar]) and re.findall('seis',mensaje3[es][filtrar-1]):
                hab.append(es)
                na_habitacion.append(es)
                if es == hab[len(na_habitacion)-1]:
                    habitaciones[es].append(mensaje3[es][filtrar-1])
                else:
                    habitaciones.append([mensaje3[es][filtrar-1]])    
            #bano        
            if re.findall('baño',mensaje3[es][filtrar]) and re.findall('1',mensaje3[es][filtrar-1]) or re.findall('bano',mensaje3[es][filtrar]) and re.findall('1',mensaje3[es][filtrar-1]) or re.findall('baño',mensaje3[es][filtrar]) and re.findall('2',mensaje3[es][filtrar-1]) or re.findall('bano',mensaje3[es][filtrar]) and re.findall('2',mensaje3[es][filtrar-1]) or re.findall('baño',mensaje3[es][filtrar]) and re.findall('3',mensaje3[es][filtrar-1]) or re.findall('bano',mensaje3[es][filtrar]) and re.findall('3',mensaje3[es][filtrar-1]) or re.findall('baño',mensaje3[es][filtrar]) and re.findall('4',mensaje3[es][filtrar-1]) or re.findall('bano',mensaje3[es][filtrar]) and re.findall('4',mensaje3[es][filtrar-1]):
                ban.append(es)
                na_bano.append(es)
                if es == ban[len(na_bano)-1]:
                    bano[es].append(mensaje3[es][filtrar-1])
                else:
                    bano.append([mensaje3[es][filtrar-1]])  
            #monto
            if re.findall(',',mensaje3[es][filtrar]) and re.findall('0',mensaje3[es][filtrar]):
                mon.append(es)
                na_monto.append(es)
                if es == mon[len(na_monto)-1]:
                    monto[es].append(mensaje3[es][filtrar])
                else:
                    monto.append([mensaje3[es][filtrar]])   
            #cualitativos
            elif re.findall('aire',mensaje3[es][filtrar]):#aire
                cuali.append(es)
                na_cuali.append(es)
                if es == cuali[len(na_cuali)-1]:
                    cualitativos[es].append(mensaje3[es][filtrar])
                else:
                    cualitativos.append([mensaje3[es][filtrar]])
            elif re.findall('aire',mensaje3[es][filtrar]) and re.findall('1',mensaje3[es][filtrar-1]) or re.findall('aire',mensaje3[es][filtrar]) and re.findall('2',mensaje3[es][filtrar-1]) or re.findall('aire',mensaje3[es][filtrar]) and re.findall('3',mensaje3[es][filtrar-1]) or re.findall('aire',mensaje3[es][filtrar]) and re.findall('4',mensaje3[es][filtrar-1]):
                cuali.append(es)
                na_cuali.append(es)
                if es == cuali[len(na_cuali)-1]:
                    cualitativos[es].append(f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}')
                else:
                    cualitativos.append([f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}'])
            if re.findall('piscina',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('picina',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]):#piscina
                cuali.append(es)
                na_cuali.append(es)
                if es == cuali[len(na_cuali)-1]:
                    cualitativos[es].append('piscina')
                else:
                    cualitativos.append(['piscina'])
            elif re.findall('jacuzzi',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]):#jacuzzi
                cuali.append(es)
                na_cuali.append(es)
                if es == cuali[len(na_cuali)-1]:
                    cualitativos[es].append('Jacuzzi')
                else:
                    cualitativos.append(['Jacuzzi'])
            elif re.findall('family',mensaje3[es][filtrar]) and re.findall('room',mensaje3[es][filtrar]) or re.findall('linea',mensaje3[es][filtrar]) and re.findall('blanca',mensaje3[es][filtrar]):
                cuali.append(es)
                na_cuali.append(es)
                if es == cuali[len(na_cuali)-1]:
                    cualitativos[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
                else:
                    cualitativos.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
            elif re.findall('amueblado',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('marmol',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('vacío',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('vacio',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or  re.findall('estudio',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('gym',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('terraza',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('balcón',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or re.findall('balcon',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]):
                cuali.append(es)
                na_cuali.append(es)
                if es == cuali[len(na_cuali)-1]:
                    cualitativos[es].append(mensaje3[es][filtrar])
                else:
                    cualitativos.append([mensaje3[es][filtrar]]) 
            elif re.findall('penthouse',mensaje3[es][filtrar]) and not re.findall('@',mensaje3[es][filtrar]) or mensaje3[es][filtrar] == 'ph' and not re.findall('@',mensaje3[es][filtrar]):
                cuali.append(es)
                na_cuali.append(es)
                if es == cuali[len(na_cuali)-1]:
                    cualitativos[es].append('penthouse')
                else:
                    cualitativos.append(['penthouse'])  
            #av
            if re.findall('27',mensaje3[es][filtrar]) and re.findall('de',mensaje3[es][filtrar]) and re.findall('febrero',mensaje3[es][filtrar]):
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
            #Sector
            if re.findall('la',mensaje3[es][filtrar-1]) and re.findall('esperilla',mensaje3[es][filtrar]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}')
                else:
                    sector.append([f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}'])    
            elif re.findall('zona',mensaje3[es][filtrar-1]) and re.findall('universitaria',mensaje3[es][filtrar]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}')
                else:
                    sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
            elif re.findall('el',mensaje3[es][filtrar-1]) and re.findall('vergel',mensaje3[es][filtrar]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}')
                else:
                    sector.append([f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}'])
            elif re.findall('arroyo',mensaje3[es][filtrar]) and re.findall('hondo',mensaje3[es][filtrar+1]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
                else:
                    sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
            elif re.findall('evaristo',mensaje3[es][filtrar-1]) and re.findall('morales',mensaje3[es][filtrar]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}')
                else:
                    sector.append([f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}'])
            elif re.findall('la',mensaje3[es][filtrar-1]) and re.findall('julia',mensaje3[es][filtrar]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}')
                else:
                    sector.append([f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}'])
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
            elif re.findall('el',mensaje3[es][filtrar-1]) and re.findall('millón',mensaje3[es][filtrar]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}')
                else:
                    sector.append([f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}'])
            elif re.findall('el',mensaje3[es][filtrar-1]) and re.findall('millon',mensaje3[es][filtrar]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}')
                else:
                    sector.append([f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}'])
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
            elif re.findall('los',mensaje3[es][filtrar]) and re.findall('cacicazgos',mensaje3[es][filtrar+1]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
                else:
                    sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
            elif re.findall('el',mensaje3[es][filtrar-1]) and re.findall('cacique',mensaje3[es][filtrar]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}')
                else:
                    sector.append([f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}'])
            elif re.findall('las',mensaje3[es][filtrar]) and re.findall('praderas',mensaje3[es][filtrar+1]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}')
                else:
                    sector.append([f'{mensaje3[es][filtrar]} {mensaje3[es][filtrar+1]}'])
            elif re.findall('mirador',mensaje3[es][filtrar-1]) and re.findall('norte',mensaje3[es][filtrar]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}')
                else:
                    sector.append([f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}'])
            elif re.findall('mirador',mensaje3[es][filtrar-1]) and re.findall('sur',mensaje3[es][filtrar]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}')
                else:
                    sector.append([f'{mensaje3[es][filtrar-1]} {mensaje3[es][filtrar]}'])
            elif re.findall('gazcue',mensaje3[es][filtrar]) or re.findall('naco',mensaje3[es][filtrar]) or re.findall('piantini',mensaje3[es][filtrar]) or re.findall('Paraíso',mensaje3[es][filtrar]) or re.findall('Paraiso',mensaje3[es][filtrar]) or re.findall('serrallés',mensaje3[es][filtrar]) or re.findall('serralles',mensaje3[es][filtrar]) or re.findall('quisqueya',mensaje3[es][filtrar]) or re.findall('julieta',mensaje3[es][filtrar]) or re.findall('renacimiento',mensaje3[es][filtrar]) or re.findall('miradores',mensaje3[es][filtrar]):
                sect.append(es)
                na_sect.append(es)
                if es == sect[len(na_sect)-1]:
                    sector[es].append(mensaje3[es][filtrar])
                else:
                    sector.append([mensaje3[es][filtrar]])
            #Ciudad
            if re.findall('santo',mensaje3[es][filtrar-1]) and re.findall('domingo',mensaje3[es][filtrar]) or re.findall('sto',mensaje3[es][filtrar-1]) and re.findall('dgo',mensaje3[es][filtrar]):            
                ciud.append(es)
                na_ci.append(es)
                if es == ciud[len(na_ci)-1]:
                    ciudad[es].append('Santo Domingo')
                else:
                    ciudad.append(['Santo Domingo'])
            elif re.findall('distrito',mensaje3[es][filtrar]) and re.findall('nacional',mensaje3[es][filtrar+1]):
                ciud.append(es)
                na_ci.append(es)
                if es == ciud[len(na_ci)-1]:
                    ciudad[es].append('Distrito Nacional')
                else:
                    ciudad.append(['Distrito Nacional'])
            elif re.findall('juan',mensaje3[es][filtrar]) and re.findall('dolio',mensaje3[es][filtrar+1]):
                ciud.append(es)
                na_ci.append(es)
                if es == ciud[len(na_ci)-1]:
                    ciudad[es].append('Juan Dolio')
                else:
                    ciudad.append(['Juan Dolio'])
            elif re.findall('la',mensaje3[es][filtrar-1]) and re.findall('romana',mensaje3[es][filtrar]):
                ciud.append(es)
                na_ci.append(es)
                if es == ciud[len(na_ci)-1]:
                    ciudad[es].append('La Romana')
                else:
                    ciudad.append(['La Romana'])
            elif re.findall('punta',mensaje3[es][filtrar]) and re.findall('cana',mensaje3[es][filtrar+1]):
                ciud.append(es)
                na_ci.append(es)
                if es == ciud[len(na_ci)-1]:
                    ciudad[es].append('Punta Cana')
                else:
                    ciudad.append(['Punta Cana'])
            elif re.findall('cap',mensaje3[es][filtrar]) and re.findall('cana',mensaje3[es][filtrar+1]):
                ciud.append(es)
                na_ci.append(es)
                if es == ciud[len(na_ci)-1]:
                    ciudad[es].append('Cap Cana')
                else:
                    ciudad.append(['Cap Cana'])
            elif re.findall('las',mensaje3[es][filtrar]) and re.findall('terrenas',mensaje3[es][filtrar+1]):
                ciud.append(es)
                na_ci.append(es)
                if es == ciud[len(na_ci)-1]:
                    ciudad[es].append('Las Terrenas')
                else:
                    ciudad.append(['Las Terrenas'])
            elif re.findall('puerto',mensaje3[es][filtrar]) and re.findall('plata',mensaje3[es][filtrar+1]):
                ciud.append(es)
                na_ci.append(es)
                if es == ciud[len(na_ci)-1]:
                    ciudad[es].append('Puerto Plata')
                else:
                    ciudad.append(['Puerto Plata'])
            elif re.findall('san',mensaje3[es][filtrar-1]) and re.findall('isidro',mensaje3[es][filtrar]):
                ciud.append(es)
                na_ci.append(es)
                if es == ciud[len(na_ci)-1]:
                    ciudad[es].append('San Isidro')
                else:
                    ciudad.append(['San Isidro'])
            elif re.findall('bayahibe',mensaje3[es][filtrar]):
                ciud.append(es)
                na_ci.append(es)
                if es == ciud[len(na_ci)-1]:
                    ciudad[es].append('Bayahibe')
                else:
                    ciudad.append(['Bayahibe'])
            elif re.findall('bavaro',mensaje3[es][filtrar]) or re.findall('bávaro',mensaje3[es][filtrar]):
                ciud.append(es)
                na_ci.append(es)
                if es == ciud[len(na_ci)-1]:
                    ciudad[es].append('Bávaro')
                else:
                    ciudad.append(['Bávaro'])
        if len(correo) != nume_c:
            correo.append('')
        if len(habitaciones) != nume_c:
            habitaciones.append('')
        if len(bano) != nume_c:
            bano.append('')
        if len(tipo) != nume_c:
            tipo.append('')
        if len(monto) != nume_c:
            monto.append('')
        if len(av) != nume_c:
            av.append('')
        if len(sector) != nume_c:
            sector.append('')
        if len(cualitativos) != nume_c:
            cualitativos.append('')
        if len(ciudad) != nume_c:
            ciudad.append('')
        nume_c += 1 
    """
    #lugar
            if re.findall('metro',mensaje3[es][filtrar]) and re.findall('country',mensaje3[es][filtrar]) and re.findall('club',mensaje3[es][filtrar]):
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

        if len(lugar) != nume_c:
            lugar.append('')
    """
    #para subir los datos al excel
    for h in range(len(mensaje3)): 
        data['Fecha'].append(fecha[h])
        data['Nombre y Celular'].append(celular[h])
        data['Correo'].append(' ; '.join(correo[h]))
        data['Ciudad'].append(' ; '.join(ciudad[h]))
        data['Sector'].append(' ; '.join(sector[h]))
        data['Av. Principal (Sto. Dgo.)'].append(' ; '.join(av[h]))
        data['Tipo de inmueble'].append(' ; '.join(tipo[h]))
        data['Cualitativos'].append(' ; '.join(cualitativos[h]))
        data['Baño'].append(' ; '.join(bano[h]))
        data['Habitaciones'].append(' ; '.join(habitaciones[h]))
        data['Monto'].append(' ; '.join(monto[h]))
        data['Descripcion'].append(' '.join(mensaje3[h]))
    #    data['Lugar'].append(' ; '.join(lugar[h]))
    df = pd.DataFrame(data, columns = ['Fecha','Nombre y Celular','Correo','Av. Principal (Sto. Dgo.)','Ciudad','Sector','Tipo de inmueble','Cualitativos','Baño','Habitaciones','Monto','Descripcion'])
    df.to_excel('tabla.xlsx', sheet_name='Datos_de_Whatsapp')
    #hacer la app web
    #metodo de analisis de estos datos
    #arreglar av
    root.destroy()

root = Tk()
#tama;o
root.geometry("250x120")
root.resizable(1,1)
root.title("App Whatsapp")
Button(root, text="Filtrar datos", command=lambda root=root:filtrarr(root)).pack(padx=15,pady=20,ipadx=5,ipady=40,fill=X)
root.mainloop()
#ventana
root.mainloop()