"""
Puntos obtenidos por posición
p1 = 25
P2 = 18
P3 = 15
P4 = 12
P5 = 10
P6 = 8
P7 = 6
P8 = 4
P9 = 2
P10 = 1
P11>=0
"""
#Posiciones con puntos del WDC actual
Ham = 195
Ver = 187
Nor = 113
Bot = 108
Per = 104
Sai = 83
Lec = 80
Gas = 50
Ric = 50
Oco = 39
Alo = 38
Vet = 30
Tsu = 18
Str = 18
Lat = 6
Rus = 4
Rai = 2
Gio = 1
Msc = 0
Maz = 0
#Puntos de pilotos
puntos = int(input("¿Cuantos puntos hizo Hamilton?"))
ham_total = (puntos + Ham)
print("Hamilton tiene ", ham_total, "puntos")

puntos = int(input("¿Cuántos puntos hizo Verstappen?"))
ver_total = (puntos + Ver)
print("Verstappen tiene", ver_total, "puntos")

puntos = int(input("¿Cuántos puntos hizo Norris?"))
nor_total = (puntos + Nor)
print("Norris tiene ", nor_total, "puntos")

puntos = int(input("¿Cuántos puntos hizo Bottas?"))
bot_total = (puntos + Bot)
print("Bottas tiene ", bot_total, "puntos")

puntos = int(input("¿Cuántos puntos hizo Pérez?"))
per_total = (puntos + Per)
print("Pérez tiene ",per_total, "puntos")

puntos = int(input("¿Cuántos puntos hizo Saínz?"))
sai_total = (puntos + Sai)
print("Saínz tiene ", sai_total, "puntos")

puntos = int(input("¿Cuántos puntos hizo Leclerc?"))
lec_total = (puntos + Lec)
print("Leclerc tiene ", lec_total, "puntos")

puntos = int(input("¿Cuantos puntos hizo Gasly?"))
gas_total = (puntos + Gas)
print("Gasly tiene ", gas_total, "puntos")

puntos = int(input("¿Cuantos puntos hizo Ricciardo?"))
ric_total = (puntos + Ric)
print("Ricciardo tiene ", ric_total, "puntos")

puntos = int(input("¿Cuantos puntos hizo Ocon?"))
oco_total = (puntos + Oco)
print("Ocon tiene ", oco_total, "puntos")

puntos = int(input("¿Cuantos puntos hizo Alonso?"))
alo_total = (puntos + Alo)
print("Alonso tiene ", alo_total, "puntos")

puntos = int(input("¿Cuantos puntos hizo Vettel?"))
vet_total = (puntos + Vet)
print("Vettel tiene ", vet_total, "puntos")

puntos = int(input("¿Cuantos puntos hizo Tsunoda?"))
tsu_total = (puntos + Tsu)
print("Tsunoda tiene ", tsu_total, "puntos")

puntos = int(input("¿Cuantos puntos hizo Stroll?"))
str_total = (puntos + Str)
print("Stroll tiene ", str_total, "puntos")

puntos = int(input("¿Cuantos puntos hizo Latifi?"))
lat_total = (puntos + Lat)
print("Latifi tiene ", lat_total, "puntos")

puntos = int(input("¿Cuantos puntos hizo Russel?"))
rus_total = (puntos + Rus)
print("Russel tiene ", rus_total, "puntos")

puntos = int(input("¿Cuantos puntos hizo Raikkonen?"))
rai_total = (puntos + Rai)
print("Raikkonen tiene ", rai_total, "puntos")

puntos = int(input("¿Cuantos puntos hizo Giovinazzi?"))
gio_total = (puntos + Gio)
print("Giovinazzi tiene ", gio_total, "puntos")

puntos = int(input("¿Cuantos puntos hizo Schumacher?"))
msc_total = (puntos + Msc)
print("Schumacher tiene", msc_total, " puntos")

puntos = int(input("¿Cuantos puntos hizo Mazepin?"))
maz_total = (puntos + Maz)
print("Mazepin tiene ", maz_total," puntos")

#Puntos por equipo
mercedes = (ham_total + bot_total)
print("Mercedes Benz tiene ", mercedes," puntos")

red_bull = (ver_total + per_total)
print("Red Bull tiene ", red_bull," puntos")

mclaren = (nor_total + ric_total)
print("Mclaren tiene ", mclaren," puntos")

ferrari = (sai_total + lec_total)
print("Ferrari tiene ", ferrari," puntos")

aston = (vet_total + str_total)
print("Aston Martin tiene ", aston," puntos")

at = (gas_total + tsu_total)
print("Alpha Tauri tiene ", at," puntos")

alpine = (oco_total + alo_total)
print("Alpine tiene ", alpine, "puntos")

af = (rai_total + gio_total)
print("Alfa Romeo tiene ", af," puntos")

williams = (rus_total + lat_total)
print("Williams tiene ", williams, " puntos")

haas = (msc_total + maz_total)
print("Haas tiene ", haas, "puntos")





