#Posiciones con puntos del WDC actual
ver = 224.5
ham = 221.5
bot = 123
nor = 114
per = 108
lec = 92
sai = 89.5
gas = 66
ric = 56
alo = 46
oco = 44
vet = 35
tsu = 18
strl = 18
rus = 13
lat = 7
rai = 2
gio = 1
msc = 0
maz = 0
# Función para calcular puntos de pilotos 
def puntos_pilotos(puntos, piloto):
    return puntos + piloto

#Función para calcular puntos de los equipo
def puntos_equipo(piloto1, piloto2):
    return piloto1 + piloto2

#Estructura If para calcular puntos de Hamilton en base a su posición
posicion = int(input("¿En que posición quedó Hamilton?"))
if(posicion == 1):
    ham_total = puntos_pilotos(25, ham)

elif(posicion == 2):
    ham_total = puntos_pilotos(18, ham)

elif(posicion == 3):
    ham_total = puntos_pilotos(15, ham)

elif(posicion == 4):
    ham_total = puntos_pilotos(12, ham)
    
elif(posicion == 5):
    ham_total = puntos_pilotos(10, ham)
    
elif(posicion == 6):
    ham_total = puntos_pilotos(8, ham)
    
elif(posicion == 7):
    ham_total = puntos_pilotos(6, ham)
    
elif(posicion == 8):
    ham_total = puntos_pilotos(4, ham)
    
elif(posicion == 9):
    ham_total = puntos_pilotos(2, ham)
    
elif(posicion == 10):
    ham_total = puntos_pilotos(1, ham)
    
else:
    ham_total = puntos_pilotos(0, ham)  
#Para calcular puntos de verstappen
posicion = int(input("¿En que posición quedó Verstappen?"))
if(posicion == 1):
    ver_total = puntos_pilotos(25, ver)

elif(posicion == 2):
    ver_total = puntos_pilotos(18, ver)

elif(posicion == 3):
    ver_total = puntos_pilotos(15, ver)

elif(posicion == 4):
    ver_total = puntos_pilotos(12, ver)
    
elif(posicion == 5):
    ver_total = puntos_pilotos(10, ver)
    
elif(posicion == 6):
    ver_total = puntos_pilotos(8, ver)
    
elif(posicion == 7):
    ver_total = puntos_pilotos(6, ver)
    
elif(posicion == 8):
    ver_total = puntos_pilotos(4, ver)
    
elif(posicion == 9):
    ver_total = puntos_pilotos(2, ver)
    
elif(posicion == 10):
    ver_total = puntos_pilotos(1, ver)
    
else:
    ver_total = puntos_pilotos(0, ver)
#Calcular puntos norris
posicion = int(input("¿En que posición quedó Norris?"))
if(posicion == 1):
    nor_total = puntos_pilotos(25, nor)

elif(posicion == 2):
    nor_total = puntos_pilotos(18, nor)

elif(posicion == 3):
    nor_total = puntos_pilotos(15, nor)

elif(posicion == 4):
    nor_total = puntos_pilotos(12, nor)
    
elif(posicion == 5):
    nor_total = puntos_pilotos(10, nor)
    
elif(posicion == 6):
    nor_total = puntos_pilotos(8, nor)
    
elif(posicion == 7):
    nor_total = puntos_pilotos(6, nor)
    
elif(posicion == 8):
    nor_total = puntos_pilotos(4, nor)
    
elif(posicion == 9):
    nor_total = puntos_pilotos(2, nor)
    
elif(posicion == 10):
    nor_total = puntos_pilotos(1, nor)
    
else:
    nor_total = puntos_pilotos(0, nor)
#Para calcular puntos de bottas
posicion = int(input("¿En que posición quedó Bottas?"))
if(posicion == 1):
    bot_total = puntos_pilotos(25, bot)

elif(posicion == 2):
    bot_total = puntos_pilotos(18, bot)

elif(posicion == 3):
    bot_total = puntos_pilotos(15, bot)

elif(posicion == 4):
    bot_total = puntos_pilotos(12, bot)
    
elif(posicion == 5):
    bot_total = puntos_pilotos(10, bot)
    
elif(posicion == 6):
    bot_total = puntos_pilotos(8, bot)
    
elif(posicion == 7):
    bot_total = puntos_pilotos(6, bot)
    
elif(posicion == 8):
    bot_total = puntos_pilotos(4, bot)
    
elif(posicion == 9):
    bot_total = puntos_pilotos(2, bot)
    
elif(posicion == 10):
    bot_total = puntos_pilotos(1, bot)
    
else:
    bot_total = puntos_pilotos(0, bot)
#Puntos de Peréz
posicion = int(input("¿En que posición quedó Peréz?"))
if(posicion == 1):
    per_total = puntos_pilotos(25, per)

elif(posicion == 2):
    per_total = puntos_pilotos(18, per)

elif(posicion == 3):
    per_total = puntos_pilotos(15, per)

elif(posicion == 4):
    per_total = puntos_pilotos(12, per)
    
elif(posicion == 5):
    per_total = puntos_pilotos(10, per)
    
elif(posicion == 6):
    per_total = puntos_pilotos(8, per)
    
elif(posicion == 7):
    per_total = puntos_pilotos(6, per)
    
elif(posicion == 8):
    per_total = puntos_pilotos(4, per)
    
elif(posicion == 9):
    per_total = puntos_pilotos(2, per)
    
elif(posicion == 10):
    per_total = puntos_pilotos(1, per)
    
else:
    per_total = puntos_pilotos(0, per)
#Puntos de Sainz
posicion = int(input("¿En que posición quedó Saínz?"))
if(posicion == 1):
    sai_total = puntos_pilotos(25, sai)

elif(posicion == 2):
    sai_total = puntos_pilotos(18, sai)

elif(posicion == 3):
    sai_total = puntos_pilotos(15, sai)

elif(posicion == 4):
    sai_total = puntos_pilotos(12, sai)
    
elif(posicion == 5):
    sai_total = puntos_pilotos(10, sai)
    
elif(posicion == 6):
    sai_total = puntos_pilotos(8, sai)
    
elif(posicion == 7):
    sai_total = puntos_pilotos(6, sai)
    
elif(posicion == 8):
    sai_total = puntos_pilotos(4, sai)
    
elif(posicion == 9):
    sai_total = puntos_pilotos(2, sai)
    
elif(posicion == 10):
    sai_total = puntos_pilotos(1, sai)
    
else:
    sai_total = puntos_pilotos(0, sai)
#Puntos leclerc
posicion = int(input("¿En que posición quedó Leclerc?"))
if(posicion == 1):
    lec_total = puntos_pilotos(25, lec)

elif(posicion == 2):
    lec_total = puntos_pilotos(18, lec)

elif(posicion == 3):
    lec_total = puntos_pilotos(15, lec)

elif(posicion == 4):
    lec_total = puntos_pilotos(12, lec)
    
elif(posicion == 5):
    lec_total = puntos_pilotos(10, lec)
    
elif(posicion == 6):
    lec_total = puntos_pilotos(8, lec)
    
elif(posicion == 7):
    lec_total = puntos_pilotos(6, lec)
    
elif(posicion == 8):
    lec_total = puntos_pilotos(4, lec)
    
elif(posicion == 9):
    lec_total = puntos_pilotos(2, lec)
    
elif(posicion == 10):
    lec_total = puntos_pilotos(1, lec)
    
else:
    lec_total = puntos_pilotos(0, lec)
#Puntos GAsly
posicion = int(input("¿En que posición quedó Gasly?"))
if(posicion == 1):
    gas_total = puntos_pilotos(25, gas)

elif(posicion == 2):
    gas_total = puntos_pilotos(18, gas)

elif(posicion == 3):
    gas_total = puntos_pilotos(15, gas)

elif(posicion == 4):
    gas_total = puntos_pilotos(12, gas)
    
elif(posicion == 5):
    gas_total = puntos_pilotos(10, gas)
    
elif(posicion == 6):
    gas_total = puntos_pilotos(8, gas)
    
elif(posicion == 7):
    gas_total = puntos_pilotos(6, gas)
    
elif(posicion == 8):
    gas_total = puntos_pilotos(4, gas)
    
elif(posicion == 9):
    gas_total = puntos_pilotos(2, gas)
    
elif(posicion == 10):
    gas_total = puntos_pilotos(1, gas)
    
else:
    gas_total = puntos_pilotos(0, gas)
#Puntos ricciardo
posicion = int(input("¿En que posición quedó Ricciardo?"))
if(posicion == 1):
    ric_total = puntos_pilotos(25, ric)

elif(posicion == 2):
    ric_total = puntos_pilotos(18, ric)

elif(posicion == 3):
    ric_total = puntos_pilotos(15, ric)

elif(posicion == 4):
    ric_total = puntos_pilotos(12, ric)
    
elif(posicion == 5):
    ric_total = puntos_pilotos(10, ric)
    
elif(posicion == 6):
    ric_total = puntos_pilotos(8, ric)
    
elif(posicion == 7):
    ric_total = puntos_pilotos(6, ric)
    
elif(posicion == 8):
    ric_total = puntos_pilotos(4, ric)
    
elif(posicion == 9):
    ric_total = puntos_pilotos(2, ric)
    
elif(posicion == 10):
    ric_total = puntos_pilotos(1, ric)
    
else:
    ric_total = puntos_pilotos(0, ric)
#Puntos ocon
posicion = int(input("¿En que posición quedó Ocon?"))
if(posicion == 1):
    oco_total = puntos_pilotos(25, oco)

elif(posicion == 2):
    oco_total = puntos_pilotos(18, oco)

elif(posicion == 3):
    oco_total = puntos_pilotos(15, oco)

elif(posicion == 4):
    oco_total = puntos_pilotos(12, oco)
    
elif(posicion == 5):
    oco_total = puntos_pilotos(10, oco)
    
elif(posicion == 6):
    oco_total = puntos_pilotos(8, oco)
    
elif(posicion == 7):
    oco_total = puntos_pilotos(6, oco)
    
elif(posicion == 8):
    oco_total = puntos_pilotos(4, oco)
    
elif(posicion == 9):
    oco_total = puntos_pilotos(2, oco)
    
elif(posicion == 10):
    oco_total = puntos_pilotos(1, oco)
    
else:
    oco_total = puntos_pilotos(0, oco)
#Puntos alonso
posicion = int(input("¿En que posición quedó Alonso?"))
if(posicion == 1):
    alo_total = puntos_pilotos(25, alo)

elif(posicion == 2):
    alo_total = puntos_pilotos(18, alo)

elif(posicion == 3):
    alo_total = puntos_pilotos(15, alo)

elif(posicion == 4):
    alo_total = puntos_pilotos(12, alo)
    
elif(posicion == 5):
    alo_total = puntos_pilotos(10, alo)
    
elif(posicion == 6):
    alo_total = puntos_pilotos(8, alo)
    
elif(posicion == 7):
    alo_total = puntos_pilotos(6, alo)
    
elif(posicion == 8):
    alo_total = puntos_pilotos(4, alo)
    
elif(posicion == 9):
    alo_total = puntos_pilotos(2, alo)
    
elif(posicion == 10):
    alo_total = puntos_pilotos(1, alo)
    
else:
    alo_total = puntos_pilotos(0, alo)
#Puntos de vettel
posicion = int(input("¿En que posición quedó Vettel?"))
if(posicion == 1):
    vet_total = puntos_pilotos(25, vet)

elif(posicion == 2):
    vet_total = puntos_pilotos(18, vet)

elif(posicion == 3):
    vet_total = puntos_pilotos(15, vet)

elif(posicion == 4):
    vet_total = puntos_pilotos(12, vet)

elif(posicion == 5):
    vet_total = puntos_pilotos(10, vet) 

elif(posicion == 6):
    vet_total = puntos_pilotos(8, vet)   

elif(posicion == 7):
    vet_total = puntos_pilotos(6, vet)   

elif(posicion == 8):
    vet_total = puntos_pilotos(4, vet)    

elif(posicion == 9):
    vet_total = puntos_pilotos(2, vet)    

elif(posicion == 10):
    vet_total = puntos_pilotos(1, vet)    
else:
    vet_total = puntos_pilotos(0, vet)
#Puntos Tsunoda
posicion = int(input("¿En que posición quedó Tsunoda?"))
if(posicion == 1):
    tsu_total = puntos_pilotos(25, tsu)

elif(posicion == 2):
    tsu_total = puntos_pilotos(18, tsu)

elif(posicion == 3):
    tsu_total = puntos_pilotos(15, tsu)

elif(posicion == 4):
    tsu_total = puntos_pilotos(12, tsu)
    
elif(posicion == 5):
    tsu_total = puntos_pilotos(10, tsu)
    
elif(posicion == 6):
    tsu_total = puntos_pilotos(8, tsu)
    
elif(posicion == 7):
    tsu_total = puntos_pilotos(6, tsu)
    
elif(posicion == 8):
    tsu_total = puntos_pilotos(4, tsu)
    
elif(posicion == 9):
    tsu_total = puntos_pilotos(2, tsu)
    
elif(posicion == 10):
    tsu_total = puntos_pilotos(1, tsu)
    
else:
    tsu_total = puntos_pilotos(0, tsu)

#Puntos stroll
posicion = int(input("¿En que posición quedó Stroll?"))
if(posicion == 1):
    strl_total = puntos_pilotos(25, strl)

elif(posicion == 2):
    strl_total = puntos_pilotos(18, strl)

elif(posicion == 3):
    strl_total = puntos_pilotos(15, strl)

elif(posicion == 4):
    strl_total = puntos_pilotos(12, strl)
    
elif(posicion == 5):
    strl_total = puntos_pilotos(10, strl)
    
elif(posicion == 6):
    strl_total = puntos_pilotos(8, strl)
    
elif(posicion == 7):
    strl_total = puntos_pilotos(6, strl)
    
elif(posicion == 8):
    strl_total = puntos_pilotos(4, strl)
    
elif(posicion == 9):
    strl_total = puntos_pilotos(2, strl)
    
elif(posicion == 10):
    strl_total = puntos_pilotos(1, strl)
    
else:
    strl_total = puntos_pilotos(0, strl)
#Puntos Latifi
posicion = int(input("¿En que posición quedó Latifi?"))
if(posicion == 1):
    lat_total = puntos_pilotos(25, lat)

elif(posicion == 2):
    lat_total = puntos_pilotos(18, lat)

elif(posicion == 3):
    lat_total = puntos_pilotos(15, lat)

elif(posicion == 4):
    lat_total = puntos_pilotos(12, lat)
    
elif(posicion == 5):
    lat_total = puntos_pilotos(10, lat)
    
elif(posicion == 6):
    lat_total = puntos_pilotos(8, lat)
    
elif(posicion == 7):
    lat_total = puntos_pilotos(6, lat)
    
elif(posicion == 8):
    lat_total = puntos_pilotos(4, lat)
    
elif(posicion == 9):
    lat_total = puntos_pilotos(2, lat)
    
elif(posicion == 10):
    lat_total = puntos_pilotos(1, lat)
    
else:
    lat_total = puntos_pilotos(0, lat)
#Puntos Russel
posicion = int(input("¿En que posición quedó Russel?"))
if(posicion == 1):
    rus_total = puntos_pilotos(25, rus)

elif(posicion == 2):
    rus_total = puntos_pilotos(18, rus)

elif(posicion == 3):
    rus_total = puntos_pilotos(15, rus)

elif(posicion == 4):
    rus_total = puntos_pilotos(12, rus)
    
elif(posicion == 5):
    rus_total = puntos_pilotos(10, rus)
    
elif(posicion == 6):
    rus_total = puntos_pilotos(8, rus)
    
elif(posicion == 7):
    rus_total = puntos_pilotos(6, rus)
    
elif(posicion == 8):
    rus_total = puntos_pilotos(4, rus)
    
elif(posicion == 9):
    rus_total = puntos_pilotos(2, rus)
    
elif(posicion == 10):
    rus_total = puntos_pilotos(1, rus)
    
else:
    rus_total = puntos_pilotos(0, rus)

#Puntos kimi
posicion = int(input("¿En que posición quedó Raikkonnen?"))
if(posicion == 1):
    rai_total = puntos_pilotos(25, rai)

elif(posicion == 2):
    rai_total = puntos_pilotos(18, rai)

elif(posicion == 3):
    rai_total = puntos_pilotos(15, rai)

elif(posicion == 4):
    rai_total = puntos_pilotos(12, rai)
    
elif(posicion == 5):
    rai_total = puntos_pilotos(10, rai)
    
elif(posicion == 6):
    rai_total = puntos_pilotos(8, rai)
    
elif(posicion == 7):
    rai_total = puntos_pilotos(6, rai)
    
elif(posicion == 8):
    rai_total = puntos_pilotos(4, rai)
    
elif(posicion == 9):
    rai_total = puntos_pilotos(2, rai)
    
elif(posicion == 10):
    rai_total = puntos_pilotos(1, rai)
    
else:
    rai_total = puntos_pilotos(0, tsu)
#puntos Giov
posicion = int(input("¿En que posición quedó Giovinazzi?"))
if(posicion == 1):
    gio_total = puntos_pilotos(25, gio)

elif(posicion == 2):
    gio_total = puntos_pilotos(18, gio)

elif(posicion == 3):
    gio_total = puntos_pilotos(15, gio)

elif(posicion == 4):
    gio_total = puntos_pilotos(12, gio)
    
elif(posicion == 5):
    tsu_total = puntos_pilotos(10, gio)
    
elif(posicion == 6):
    gio_total = puntos_pilotos(8, gio)
    
elif(posicion == 7):
    gio_total = puntos_pilotos(6, gio)
    
elif(posicion == 8):
    gio_total = puntos_pilotos(4, gio)
    
elif(posicion == 9):
    gio_total = puntos_pilotos(2, gio)
    
elif(posicion == 10):
    gio_total = puntos_pilotos(1, gio)
    
else:
    gio_total = puntos_pilotos(0, gio)

#Puntos Schumi
posicion = int(input("¿En que posición quedó Schumacher?"))
if(posicion == 1):
    msc_total = puntos_pilotos(25, msc)

elif(posicion == 2):
    msc_total = puntos_pilotos(18, msc)

elif(posicion == 3):
    msc_total = puntos_pilotos(15, msc)

elif(posicion == 4):
    msc_total = puntos_pilotos(12, msc)
    
elif(posicion == 5):
    msc_total = puntos_pilotos(10, msc)
    
elif(posicion == 6):
    msc_total = puntos_pilotos(8, msc)
    
elif(posicion == 7):
    msc_total = puntos_pilotos(6, msc)
    
elif(posicion == 8):
    msc_total = puntos_pilotos(4, msc)
    
elif(posicion == 9):
    msc_total = puntos_pilotos(2, msc)
    
elif(posicion == 10):
    msc_total = puntos_pilotos(1, msc)
    
else:
    msc_total = puntos_pilotos(0, msc)
#Puntos mazepin
posicion = int(input("¿En que posición quedó Mazepin?"))
if(posicion == 1):
    maz_total = puntos_pilotos(25, maz)

elif(posicion == 2):
    maz_total = puntos_pilotos(18, maz)

elif(posicion == 3):
    maz_total = puntos_pilotos(15, maz)

elif(posicion == 4):
    maz_total = puntos_pilotos(12, maz)
    
elif(posicion == 5):
    maz_total = puntos_pilotos(10, maz)
    
elif(posicion == 6):
    maz_total = puntos_pilotos(8, maz)
    
elif(posicion == 7):
    maz_total = puntos_pilotos(6, maz)
    
elif(posicion == 8):
    maz_total = puntos_pilotos(4, maz)
    
elif(posicion == 9):
    maz_total = puntos_pilotos(2, maz)
    
elif(posicion == 10):
    maz_total = puntos_pilotos(1, maz)
    
else:
    maz_total = puntos_pilotos(0, maz)

#Puntos por piloto
print("Hamilton tiene ", ham_total, "puntos")
print("Verstappen tiene", ver_total, "puntos")
print("Norris tiene ", nor_total, "puntos")
print("Bottas tiene ", bot_total, "puntos")
print("Pérez tiene ",per_total, "puntos")
print("Saínz tiene ", sai_total, "puntos")
print("Leclerc tiene ", lec_total, "puntos")
print("Gasly tiene ", gas_total, "puntos")
print("Ricciardo tiene ", ric_total, "puntos")
print("Ocon tiene ", oco_total, "puntos")
print("Alonso tiene ", alo_total, "puntos")
print("Vettel tiene ", vet_total, "puntos")
print("Tsunoda tiene ", tsu_total, "puntos")
print("Stroll tiene ", strl_total, "puntos")
print("Latifi tiene ", lat_total, "puntos")
print("Russel tiene ", rus_total, "puntos")
print("Raikkonen tiene ", rai_total, "puntos")
print("Giovinazzi tiene ", gio_total, "puntos")
print("Schumacher tiene", msc_total, " puntos")
print("Mazepin tiene ", maz_total," puntos")

#Puntos por equipo
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