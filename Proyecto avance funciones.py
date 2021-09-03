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
ham = 195
ver = 187
nor = 113
bot = 108
per = 104
sai = 83
lec = 80
gas = 50
ric = 50
oco = 39
alo = 38
vet = 30
tsu = 18
strl = 18
lat = 6
rus = 4
rai = 2
gio = 1
msc = 0
maz = 0
# Calcular Puntos de pilotos con funciones
def puntos_pilotos(puntos, piloto):
    return puntos + piloto
#Calcular puntos de los equipo
def puntos_equipo(piloto1, piloto2):
    return piloto1 + piloto2

puntos = int(input("Cuantos puntos hizo Hamilton"))
ham_total = puntos_pilotos(puntos, ham)

puntos = int(input("¿Cuántos puntos hizo Verstappen?"))
ver_total = puntos_pilotos(puntos, ver)

puntos = int(input("¿Cuántos puntos hizo Norris?"))
nor_total = puntos_pilotos(puntos, nor)

puntos = int(input("¿Cuántos puntos hizo Bottas?"))
bot_total = puntos_pilotos(puntos, bot)

puntos = int(input("¿Cuántos puntos hizo Pérez?"))
per_total = puntos_pilotos(puntos, per)

puntos = int(input("¿Cuántos puntos hizo Saínz?"))
sai_total = puntos_pilotos(puntos, sai)

puntos = int(input("¿Cuántos puntos hizo Leclerc?"))
lec_total = puntos_pilotos(puntos, lec)

puntos = int(input("¿Cuantos puntos hizo Gasly?"))
gas_total = puntos_pilotos(puntos, gas)

puntos = int(input("¿Cuantos puntos hizo Ricciardo?"))
ric_total = puntos_pilotos(puntos, ric)

puntos = int(input("¿Cuantos puntos hizo Ocon?"))
oco_total = puntos_pilotos(puntos, oco)

puntos = int(input("¿Cuantos puntos hizo Alonso?"))
alo_total = puntos_pilotos(puntos, alo)

puntos = int(input("¿Cuantos puntos hizo Vettel?"))
vet_total = puntos_pilotos(puntos, vet)

puntos = int(input("¿Cuantos puntos hizo Tsunoda?"))
tsu_total = puntos_pilotos(puntos, tsu)

puntos = int(input("¿Cuantos puntos hizo Stroll?"))
strl_total = puntos_pilotos(puntos, strl)

puntos = int(input("¿Cuantos puntos hizo Latifi?"))
lat_total = puntos_pilotos(puntos, lat)

puntos = int(input("¿Cuantos puntos hizo Russel?"))
rus_total = puntos_pilotos(puntos, rus)

puntos = int(input("¿Cuantos puntos hizo Raikkonen?"))
rai_total = puntos_pilotos(puntos, rai)

puntos = int(input("¿Cuantos puntos hizo Giovinazzi?"))
gio_total = puntos_pilotos(puntos, gio)

puntos = int(input("¿Cuantos puntos hizo Schumacher?"))
msc_total = puntos_pilotos(puntos, msc)

puntos = int(input("¿Cuantos puntos hizo Mazepin?"))
maz_total = puntos_pilotos(puntos, maz)

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