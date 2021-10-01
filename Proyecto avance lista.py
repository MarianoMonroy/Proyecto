#Posiciones con puntos del WDC actual
pilotos = ["Verstappen", "Hamilton", "Bottas", "Norris", "Perez", "Leclerc",
           "Sainz", "GAsly", "Ricciardo", "Alonso", "Ocon", "Vettel",
           "Tsunoda", "Stroll", "Russel", "Latifi", "Raikkonnen",
           "Giovinazzi","Schumacher", "Mazepin"]
puntos = [224.5, 221.5, 123, 114, 108, 92, 89.5, 66, 56, 46, 44, 35, 18,
          18, 13, 7, 2, 1, 0, 0]
print(pilotos[15])
# Función para calcular puntos de pilotos 
def puntos_pilotos(puntos, piloto):
    return puntos + piloto

#Función para calcular puntos de los equipo
def puntos_equipo(piloto1, piloto2):
    return piloto1 + piloto2
#Funcion para saber quien es el líder del campeonato
def lider_campeonato(piloto1, piloto2):
    if piloto1 > piloto2:
        return "Verstappen con ",piloto1, "puntos"
    elif piloto2 > piloto1:
        return "Hamilton con",piloto2, "puntos"
#Función para calcular la diferencia de puntos entre líder y pilotos
def diferencia_puntos_a_lider(piloto):
    if ver_total >= ham_total:
        i = piloto
        acum = ver_total
        while ver_total > piloto:
            acum = acum - i
            i = i - 1
            return acum
    elif ver_total <= ham_total:
        i = piloto
        acum = ham_total
        while piloto < ham_total:
            acum = acum - i
            i = i - 1
            return acum
    else:
        return "Tienen los mismos puntos"
#Estructura If para calcular puntos de Hamilton en base a su posición
posicion = int(input("¿En que posición quedó Hamilton?"))
if(posicion == 1):
    ham_total = puntos_pilotos(25, puntos[0])

elif(posicion == 2):
    ham_total = puntos_pilotos(18, puntos[0])

elif(posicion == 3):
    ham_total = puntos_pilotos(15, puntos[0])

elif(posicion == 4):
    ham_total = puntos_pilotos(12, puntos[0])
    
elif(posicion == 5):
    ham_total = puntos_pilotos(10, puntos[0])
    
elif(posicion == 6):
    ham_total = puntos_pilotos(8, puntos[0])
    
elif(posicion == 7):
    ham_total = puntos_pilotos(6, puntos[0])
    
elif(posicion == 8):
    ham_total = puntos_pilotos(4, puntos[0])
    
elif(posicion == 9):
    ham_total = puntos_pilotos(2, puntos[0])
    
elif(posicion == 10):
    ham_total = puntos_pilotos(1, puntos[0])
    
else:
    ham_total = puntos_pilotos(0, puntos[0])

#Para calcular puntos de verstappen
posicion = int(input("¿En que posición quedó Verstappen?"))
if(posicion == 1):
    ver_total = puntos_pilotos(25, puntos[1])

elif(posicion == 2):
    ver_total = puntos_pilotos(18, puntos[1])

elif(posicion == 3):
    ver_total = puntos_pilotos(15, puntos[1])

elif(posicion == 4):
    ver_total = puntos_pilotos(12, puntos[1])
    
elif(posicion == 5):
    ver_total = puntos_pilotos(10, puntos[1])
    
elif(posicion == 6):
    ver_total = puntos_pilotos(8, puntos[1])
    
elif(posicion == 7):
    ver_total = puntos_pilotos(6, puntos[1])
    
elif(posicion == 8):
    ver_total = puntos_pilotos(4, puntos[1])
    
elif(posicion == 9):
    ver_total = puntos_pilotos(2, puntos[1])
    
elif(posicion == 10):
    ver_total = puntos_pilotos(1, puntos[1])
    
else:
    ver_total = puntos_pilotos(0, puntos[1])
#Calcular puntos norris
posicion = int(input("¿En que posición quedó Norris?"))
if(posicion == 1):
    nor_total = puntos_pilotos(25, puntos[2])

elif(posicion == 2):
    nor_total = puntos_pilotos(18, puntos[2])

elif(posicion == 3):
    nor_total = puntos_pilotos(15, puntos[2])

elif(posicion == 4):
    nor_total = puntos_pilotos(12, puntos[2])
    
elif(posicion == 5):
    nor_total = puntos_pilotos(10, puntos[2])
    
elif(posicion == 6):
    nor_total = puntos_pilotos(8, puntos[2])
    
elif(posicion == 7):
    nor_total = puntos_pilotos(6, puntos[2])
    
elif(posicion == 8):
    nor_total = puntos_pilotos(4, puntos[2])
    
elif(posicion == 9):
    nor_total = puntos_pilotos(2, puntos[2])
    
elif(posicion == 10):
    nor_total = puntos_pilotos(1, puntos[2])
    
else:
    nor_total = puntos_pilotos(0, puntos[2])
#Para calcular puntos de bottas
posicion = int(input("¿En que posición quedó Bottas?"))
if(posicion == 1):
    bot_total = puntos_pilotos(25, puntos[3])

elif(posicion == 2):
    bot_total = puntos_pilotos(18, puntos[3])

elif(posicion == 3):
    bot_total = puntos_pilotos(15, puntos[3])

elif(posicion == 4):
    bot_total = puntos_pilotos(12, puntos[3])
    
elif(posicion == 5):
    bot_total = puntos_pilotos(10, puntos[3])
    
elif(posicion == 6):
    bot_total = puntos_pilotos(8, puntos[3])
    
elif(posicion == 7):
    bot_total = puntos_pilotos(6, puntos[3])
    
elif(posicion == 8):
    bot_total = puntos_pilotos(4, puntos[3])
    
elif(posicion == 9):
    bot_total = puntos_pilotos(2, puntos[3])
    
elif(posicion == 10):
    bot_total = puntos_pilotos(1, puntos[3])
    
else:
    bot_total = puntos_pilotos(0, puntos[3])
#Puntos de Peréz
posicion = int(input("¿En que posición quedó Peréz?"))
if(posicion == 1):
    per_total = puntos_pilotos(25, puntos[4])

elif(posicion == 2):
    per_total = puntos_pilotos(18, puntos[4])

elif(posicion == 3):
    per_total = puntos_pilotos(15, puntos[4])

elif(posicion == 4):
    per_total = puntos_pilotos(12, puntos[4])
    
elif(posicion == 5):
    per_total = puntos_pilotos(10, puntos[4])
    
elif(posicion == 6):
    per_total = puntos_pilotos(8, puntos[4])
    
elif(posicion == 7):
    per_total = puntos_pilotos(6, puntos[4])
    
elif(posicion == 8):
    per_total = puntos_pilotos(4, puntos[4])
    
elif(posicion == 9):
    per_total = puntos_pilotos(2, puntos[4])
    
elif(posicion == 10):
    per_total = puntos_pilotos(1, puntos[4])
    
else:
    per_total = puntos_pilotos(0, puntos[4])
#Puntos de Sainz
posicion = int(input("¿En que posición quedó Saínz?"))
if(posicion == 1):
    sai_total = puntos_pilotos(25, puntos[5])

elif(posicion == 2):
    sai_total = puntos_pilotos(18, puntos[5])

elif(posicion == 3):
    sai_total = puntos_pilotos(15, puntos[5])

elif(posicion == 4):
    sai_total = puntos_pilotos(12, puntos[5])
    
elif(posicion == 5):
    sai_total = puntos_pilotos(10, puntos[5])
    
elif(posicion == 6):
    sai_total = puntos_pilotos(8, puntos[5])
    
elif(posicion == 7):
    sai_total = puntos_pilotos(6, puntos[5])
    
elif(posicion == 8):
    sai_total = puntos_pilotos(4, puntos[5])
    
elif(posicion == 9):
    sai_total = puntos_pilotos(2, puntos[5])
    
elif(posicion == 10):
    sai_total = puntos_pilotos(1, puntos[5])
    
else:
    sai_total = puntos_pilotos(0, puntos[5])
#Puntos leclerc
posicion = int(input("¿En que posición quedó Leclerc?"))
if(posicion == 1):
    lec_total = puntos_pilotos(25, puntos[6])

elif(posicion == 2):
    lec_total = puntos_pilotos(18, puntos[6])

elif(posicion == 3):
    lec_total = puntos_pilotos(15, puntos[6])

elif(posicion == 4):
    lec_total = puntos_pilotos(12, puntos[6])
    
elif(posicion == 5):
    lec_total = puntos_pilotos(10, puntos[6])
    
elif(posicion == 6):
    lec_total = puntos_pilotos(8, puntos[6])
    
elif(posicion == 7):
    lec_total = puntos_pilotos(6, puntos[6])
    
elif(posicion == 8):
    lec_total = puntos_pilotos(4, puntos[6])
    
elif(posicion == 9):
    lec_total = puntos_pilotos(2, puntos[6])
    
elif(posicion == 10):
    lec_total = puntos_pilotos(1, puntos[6])
    
else:
    lec_total = puntos_pilotos(0, puntos[6])
#Puntos GAsly
posicion = int(input("¿En que posición quedó Gasly?"))
if(posicion == 1):
    gas_total = puntos_pilotos(25, puntos[7])

elif(posicion == 2):
    gas_total = puntos_pilotos(18, puntos[7])

elif(posicion == 3):
    gas_total = puntos_pilotos(15, puntos[7])

elif(posicion == 4):
    gas_total = puntos_pilotos(12, puntos[7])
    
elif(posicion == 5):
    gas_total = puntos_pilotos(10, puntos[7])
    
elif(posicion == 6):
    gas_total = puntos_pilotos(8, puntos[7])
    
elif(posicion == 7):
    gas_total = puntos_pilotos(6, puntos[7])
    
elif(posicion == 8):
    gas_total = puntos_pilotos(4, puntos[7])
    
elif(posicion == 9):
    gas_total = puntos_pilotos(2, puntos[7])
    
elif(posicion == 10):
    gas_total = puntos_pilotos(1, puntos[7])
    
else:
    gas_total = puntos_pilotos(0, puntos[7])
#Puntos ricciardo
posicion = int(input("¿En que posición quedó Ricciardo?"))
if(posicion == 1):
    ric_total = puntos_pilotos(25, puntos[8])

elif(posicion == 2):
    ric_total = puntos_pilotos(18, puntos[8])

elif(posicion == 3):
    ric_total = puntos_pilotos(15, puntos[8])

elif(posicion == 4):
    ric_total = puntos_pilotos(12, puntos[8])
    
elif(posicion == 5):
    ric_total = puntos_pilotos(10, puntos[8])
    
elif(posicion == 6):
    ric_total = puntos_pilotos(8, puntos[8])
    
elif(posicion == 7):
    ric_total = puntos_pilotos(6, puntos[8])
    
elif(posicion == 8):
    ric_total = puntos_pilotos(4, puntos[8])
    
elif(posicion == 9):
    ric_total = puntos_pilotos(2, puntos[8])
    
elif(posicion == 10):
    ric_total = puntos_pilotos(1, puntos[8])
    
else:
    ric_total = puntos_pilotos(0, puntos[8])
#Puntos ocon
posicion = int(input("¿En que posición quedó Ocon?"))
if(posicion == 1):
    oco_total = puntos_pilotos(25, puntos[9])

elif(posicion == 2):
    oco_total = puntos_pilotos(18, puntos[9])

elif(posicion == 3):
    oco_total = puntos_pilotos(15, puntos[9])

elif(posicion == 4):
    oco_total = puntos_pilotos(12, puntos[9])
    
elif(posicion == 5):
    oco_total = puntos_pilotos(10, puntos[9])
    
elif(posicion == 6):
    oco_total = puntos_pilotos(8, puntos[9])
    
elif(posicion == 7):
    oco_total = puntos_pilotos(6, puntos[9])
    
elif(posicion == 8):
    oco_total = puntos_pilotos(4, puntos[9])
    
elif(posicion == 9):
    oco_total = puntos_pilotos(2, puntos[9])
    
elif(posicion == 10):
    oco_total = puntos_pilotos(1, puntos[9])
    
else:
    oco_total = puntos_pilotos(0, puntos[9])
#Puntos alonso
posicion = int(input("¿En que posición quedó Alonso?"))
if(posicion == 1):
    alo_total = puntos_pilotos(25, puntos[10])

elif(posicion == 2):
    alo_total = puntos_pilotos(18,puntos[10])

elif(posicion == 3):
    alo_total = puntos_pilotos(15, puntos[10])

elif(posicion == 4):
    alo_total = puntos_pilotos(12, puntos[10])
    
elif(posicion == 5):
    alo_total = puntos_pilotos(10, puntos[10])
    
elif(posicion == 6):
    alo_total = puntos_pilotos(8, puntos[10])
    
elif(posicion == 7):
    alo_total = puntos_pilotos(6, puntos[10])
    
elif(posicion == 8):
    alo_total = puntos_pilotos(4, puntos[10])
    
elif(posicion == 9):
    alo_total = puntos_pilotos(2, puntos[10])
    
elif(posicion == 10):
    alo_total = puntos_pilotos(1, puntos[10])
    
else:
    alo_total = puntos_pilotos(0, puntos[10])
#Puntos de vettel
posicion = int(input("¿En que posición quedó Vettel?"))
if(posicion == 1):
    vet_total = puntos_pilotos(25, puntos[11])

elif(posicion == 2):
    vet_total = puntos_pilotos(18, puntos[11])

elif(posicion == 3):
    vet_total = puntos_pilotos(15, puntos[11])

elif(posicion == 4):
    vet_total = puntos_pilotos(12, puntos[11])

elif(posicion == 5):
    vet_total = puntos_pilotos(10, puntos[11]) 

elif(posicion == 6):
    vet_total = puntos_pilotos(8, puntos[11])   

elif(posicion == 7):
    vet_total = puntos_pilotos(6, puntos[11])   

elif(posicion == 8):
    vet_total = puntos_pilotos(4, puntos[11])    

elif(posicion == 9):
    vet_total = puntos_pilotos(2, puntos[11])    

elif(posicion == 10):
    vet_total = puntos_pilotos(1, puntos[11])    
else:
    vet_total = puntos_pilotos(0, puntos[11])
#Puntos Tsunoda
posicion = int(input("¿En que posición quedó Tsunoda?"))
if(posicion == 1):
    tsu_total = puntos_pilotos(25, puntos[12])

elif(posicion == 2):
    tsu_total = puntos_pilotos(18, puntos[12])

elif(posicion == 3):
    tsu_total = puntos_pilotos(15, puntos[12])

elif(posicion == 4):
    tsu_total = puntos_pilotos(12, puntos[12])
    
elif(posicion == 5):
    tsu_total = puntos_pilotos(10, puntos[12])
    
elif(posicion == 6):
    tsu_total = puntos_pilotos(8, puntos[12])
    
elif(posicion == 7):
    tsu_total = puntos_pilotos(6, puntos[12])
    
elif(posicion == 8):
    tsu_total = puntos_pilotos(4, puntos[12])
    
elif(posicion == 9):
    tsu_total = puntos_pilotos(2, puntos[12])
    
elif(posicion == 10):
    tsu_total = puntos_pilotos(1, puntos[12])
    
else:
    tsu_total = puntos_pilotos(0, puntos[12])

#Puntos stroll
posicion = int(input("¿En que posición quedó Stroll?"))
if(posicion == 1):
    strl_total = puntos_pilotos(25, puntos[13])

elif(posicion == 2):
    strl_total = puntos_pilotos(18, puntos[13])

elif(posicion == 3):
    strl_total = puntos_pilotos(15, puntos[13])

elif(posicion == 4):
    strl_total = puntos_pilotos(12, puntos[13])
    
elif(posicion == 5):
    strl_total = puntos_pilotos(10, puntos[13])
    
elif(posicion == 6):
    strl_total = puntos_pilotos(8, puntos[13])
    
elif(posicion == 7):
    strl_total = puntos_pilotos(6, puntos[13])
    
elif(posicion == 8):
    strl_total = puntos_pilotos(4, puntos[13])
    
elif(posicion == 9):
    strl_total = puntos_pilotos(2, puntos[13])
    
elif(posicion == 10):
    strl_total = puntos_pilotos(1, puntos[13])
    
else:
    strl_total = puntos_pilotos(0, puntos[13])
#Puntos Latifi
posicion = int(input("¿En que posición quedó Latifi?"))
if(posicion == 1):
    lat_total = puntos_pilotos(25, puntos[14])

elif(posicion == 2):
    lat_total = puntos_pilotos(18, puntos[14])

elif(posicion == 3):
    lat_total = puntos_pilotos(15, puntos[14])

elif(posicion == 4):
    lat_total = puntos_pilotos(12, puntos[14])
    
elif(posicion == 5):
    lat_total = puntos_pilotos(10, puntos[14])
    
elif(posicion == 6):
    lat_total = puntos_pilotos(8, puntos[14])
    
elif(posicion == 7):
    lat_total = puntos_pilotos(6, puntos[14])
    
elif(posicion == 8):
    lat_total = puntos_pilotos(4, puntos[14])
    
elif(posicion == 9):
    lat_total = puntos_pilotos(2, puntos[14])
    
elif(posicion == 10):
    lat_total = puntos_pilotos(1, puntos[14])
    
else:
    lat_total = puntos_pilotos(0, puntos[14])
#Puntos Russel
posicion = int(input("¿En que posición quedó Russel?"))
if(posicion == 1):
    rus_total = puntos_pilotos(25, puntos[15])

elif(posicion == 2):
    rus_total = puntos_pilotos(18, puntos[15])

elif(posicion == 3):
    rus_total = puntos_pilotos(15, puntos[15])

elif(posicion == 4):
    rus_total = puntos_pilotos(12, puntos[15])
    
elif(posicion == 5):
    rus_total = puntos_pilotos(10, puntos[15])
    
elif(posicion == 6):
    rus_total = puntos_pilotos(8, puntos[15])
    
elif(posicion == 7):
    rus_total = puntos_pilotos(6, puntos[15])
    
elif(posicion == 8):
    rus_total = puntos_pilotos(4, puntos[15])
    
elif(posicion == 9):
    rus_total = puntos_pilotos(2, puntos[15])
    
elif(posicion == 10):
    rus_total = puntos_pilotos(1, puntos[15])
    
else:
    rus_total = puntos_pilotos(0, puntos[15])

#Puntos kimi
posicion = int(input("¿En que posición quedó Raikkonnen?"))
if(posicion == 1):
    rai_total = puntos_pilotos(25, puntos[16])

elif(posicion == 2):
    rai_total = puntos_pilotos(18, puntos[16])

elif(posicion == 3):
    rai_total = puntos_pilotos(15, puntos[16])

elif(posicion == 4):
    rai_total = puntos_pilotos(12, puntos[16])
    
elif(posicion == 5):
    rai_total = puntos_pilotos(10, puntos[16])
    
elif(posicion == 6):
    rai_total = puntos_pilotos(8, puntos[16])
    
elif(posicion == 7):
    rai_total = puntos_pilotos(6, puntos[16])
    
elif(posicion == 8):
    rai_total = puntos_pilotos(4, puntos[16])
    
elif(posicion == 9):
    rai_total = puntos_pilotos(2, puntos[16])
    
elif(posicion == 10):
    rai_total = puntos_pilotos(1, puntos[16])
    
else:
    rai_total = puntos_pilotos(0, puntos[16])
#puntos Giov
posicion = int(input("¿En que posición quedó Giovinazzi?"))
if(posicion == 1):
    gio_total = puntos_pilotos(25, puntos[17])

elif(posicion == 2):
    gio_total = puntos_pilotos(18, puntos[17])

elif(posicion == 3):
    gio_total = puntos_pilotos(15, puntos[17])

elif(posicion == 4):
    gio_total = puntos_pilotos(12, puntos[17])
    
elif(posicion == 5):
    tsu_total = puntos_pilotos(10, puntos[17])
    
elif(posicion == 6):
    gio_total = puntos_pilotos(8, puntos[17])
    
elif(posicion == 7):
    gio_total = puntos_pilotos(6, puntos[17])
    
elif(posicion == 8):
    gio_total = puntos_pilotos(4, puntos[17])
    
elif(posicion == 9):
    gio_total = puntos_pilotos(2, puntos[17])
    
elif(posicion == 10):
    gio_total = puntos_pilotos(1, puntos[17])
    
else:
    gio_total = puntos_pilotos(0, puntos[17])

#Puntos Schumi
posicion = int(input("¿En que posición quedó Schumacher?"))
if(posicion == 1):
    msc_total = puntos_pilotos(25, puntos[18])

elif(posicion == 2):
    msc_total = puntos_pilotos(18, puntos[18])

elif(posicion == 3):
    msc_total = puntos_pilotos(15, puntos[18])

elif(posicion == 4):
    msc_total = puntos_pilotos(12, puntos[18])
    
elif(posicion == 5):
    msc_total = puntos_pilotos(10, puntos[18])
    
elif(posicion == 6):
    msc_total = puntos_pilotos(8, puntos[18])
    
elif(posicion == 7):
    msc_total = puntos_pilotos(6, puntos[18])
    
elif(posicion == 8):
    msc_total = puntos_pilotos(4, puntos[18])
    
elif(posicion == 9):
    msc_total = puntos_pilotos(2, puntos[18])
    
elif(posicion == 10):
    msc_total = puntos_pilotos(1, puntos[18])
    
else:
    msc_total = puntos_pilotos(0, puntos[18])
#Puntos mazepin
posicion = int(input("¿En que posición quedó Mazepin?"))
if(posicion == 1):
    maz_total = puntos_pilotos(25, puntos[19])

elif(posicion == 2):
    maz_total = puntos_pilotos(18, puntos[19])

elif(posicion == 3):
    maz_total = puntos_pilotos(15, puntos[19])

elif(posicion == 4):
    maz_total = puntos_pilotos(12, puntos[19])
    
elif(posicion == 5):
    maz_total = puntos_pilotos(10, puntos[19])
    
elif(posicion == 6):
    maz_total = puntos_pilotos(8, puntos[19])
    
elif(posicion == 7):
    maz_total = puntos_pilotos(6, puntos[19])
    
elif(posicion == 8):
    maz_total = puntos_pilotos(4, puntos[19])
    
elif(posicion == 9):
    maz_total = puntos_pilotos(2, puntos[19])
    
elif(posicion == 10):
    maz_total = puntos_pilotos(1, puntos[19])
    
else:
    maz_total = puntos_pilotos(0, puntos[19])

#Puntos por piloto
print("\n Campeonato de Pilotos")
print(pilotos[0], " tiene ", ver_total, "puntos")
print(pilotos[1], " tiene ", ham_total, "puntos")
print(pilotos[2], " tiene ", bot_total, "puntos")
print(pilotos[3], " tiene ", nor_total, "puntos")
print(pilotos[4], " tiene ",per_total, "puntos")
print(pilotos[5], " tiene ", lec_total, "puntos")
print(pilotos[6], " tiene ", sai_total, "puntos")
print(pilotos[7], " tiene ", gas_total, "puntos")
print(pilotos[8], " tiene ", ric_total, "puntos")
print(pilotos[9], " tiene ", alo_total, "puntos")
print(pilotos[10], " tiene ", oco_total, "puntos")
print(pilotos[11], " tiene ", vet_total, "puntos")
print(pilotos[12], " tiene ", tsu_total, "puntos")
print(pilotos[13], " tiene ", strl_total, "puntos")
print(pilotos[14], " tiene ", lat_total, "puntos")
print(pilotos[15], " tiene ", rus_total, "puntos")
print(pilotos[16], " tiene ", rai_total, "puntos")
print(pilotos[17], " tiene ", gio_total, "puntos")
print(pilotos[18], " tiene", msc_total, " puntos")
print(pilotos[19], " tiene ", maz_total," puntos")
#Puntos por equipo
print("\n Campeonato de Constructores")
print("Mercedes Benz tiene ", puntos_equipo(ham_total, bot_total),"puntos")
print("Red Bull tiene ", puntos_equipo(ver_total, per_total)," puntos")
print("Mclaren tiene ", puntos_equipo(nor_total, ric_total)," puntos")
print("Ferrari tiene ", puntos_equipo(sai_total, lec_total)," puntos")
print("Aston Martin tiene ", puntos_equipo(vet_total, strl_total)," puntos")
print("Alpha Tauri tiene ", puntos_equipo(gas_total, tsu_total)," puntos")
print("Alpine tiene ", puntos_equipo(alo_total, oco_total), "puntos")
print("Alfa Romeo tiene ",puntos_equipo(rai_total, gio_total)," puntos")
print("Williams tiene ", puntos_equipo(lat_total, rus_total), " puntos")
print("Haas tiene ", puntos_equipo(msc_total, maz_total), "puntos")
#Para saber quien es el lider
print("\n El lider del campeonato es ",lider_campeonato(ver_total, ham_total))
#Diferencia de puntos entre pilotos
("\n Diferencia de puntos respecto al líder")
print("La diferencia de Hamilton al líder es de",diferencia_puntos_a_lider(ham_total), "puntos")
print("La diferencia de Verstappen al líder es de",diferencia_puntos_a_lider(ver_total), "puntos")
print("La diferencia de Norris al líder es de",diferencia_puntos_a_lider(nor_total), "puntos")
print("La diferencia de Bottas al líder es de",diferencia_puntos_a_lider(bot_total), "puntos")
print("La diferencia de Pérez al líder es de",diferencia_puntos_a_lider(per_total), "puntos")
print("La diferencia de Saínz al líder es de",diferencia_puntos_a_lider(sai_total), "puntos")
print("La diferencia de Leclerc al líder es de",diferencia_puntos_a_lider(lec_total), "puntos")
print("La diferencia de Gasly al líder es de",diferencia_puntos_a_lider(gas_total), "puntos")
print("La diferencia de Ricciardo al líder es de",diferencia_puntos_a_lider(ric_total), "puntos")
print("La diferencia de Ocon al líder es de",diferencia_puntos_a_lider(oco_total), "puntos")
print("La diferencia de Alonso al líder es de",diferencia_puntos_a_lider(alo_total), "puntos")
print("La diferencia de Vettel al líder es de",diferencia_puntos_a_lider(vet_total), "puntos")
print("La diferencia de Tsunoda al líder es de",diferencia_puntos_a_lider(tsu_total), "puntos")
print("La diferencia de Stroll al líder es de",diferencia_puntos_a_lider(strl_total), "puntos")
print("La diferencia de Latifi al líder es de",diferencia_puntos_a_lider(lat_total), "puntos")
print("La diferencia de Russel al líder es de",diferencia_puntos_a_lider(rus_total), "puntos")
print("La diferencia de Raikonnen al líder es de",diferencia_puntos_a_lider(rai_total), "puntos")
print("La diferencia de Giovinazzi al líder es de",diferencia_puntos_a_lider(gio_total), "puntos")
print("La diferencia de Schumacher al líder es de",diferencia_puntos_a_lider(msc_total), "puntos")
print("La diferencia de Mazepin al líder es de",diferencia_puntos_a_lider(maz_total), "puntos")