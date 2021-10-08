#Posiciones con puntos del WDC actual
pilotos = ["Verstappen", "Hamilton", "Bottas", "Norris", "Perez", "Leclerc",
           "Sainz", "Gasly", "Ricciardo", "Alonso", "Ocon", "Vettel",
           "Tsunoda", "Stroll", "Russel", "Latifi", "Raikkonnen",
           "Giovinazzi","Schumacher", "Mazepin"]
puntos = [224.5, 221.5, 123, 114, 108, 92, 89.5, 66, 56, 46, 44, 35, 18,
          18, 13, 7, 2, 1, 0, 0]
total = []

# Función para calcular puntos de pilotos 
def puntos_pilotos(puntos, piloto):
    return puntos + piloto

#Función para calcular puntos de los equipo
def puntos_equipo(piloto1, piloto2):
    return piloto1 + piloto2

#Funcion para saber quien es el líder del campeonato
def lider_campeonato(piloto1, piloto2):
    if piloto1 > piloto2:
        return "Verstappen con " , piloto1, "puntos"
    elif piloto2 > piloto1:
        return "Hamilton con" , piloto2 , "puntos"
    
#Función para calcular la diferencia de puntos entre líder y pilotos
def diferencia_puntos_a_lider(piloto):
    if total[0] >= total[1]:
        i = piloto
        acum = total[0]
        while total[0] > piloto:
            acum = acum - i
            i = i - 1
            return acum
    elif total[0] <= total[1]:
        i = piloto
        acum = total[1]
        while piloto < total[1]:
            acum = acum - i
            i = i - 1
            return acum
    else:
        return "Tienen los mismos puntos"
    
#Función para imprimir campeonato de pilotos final 
def imprimir_info():
    i = 0
    while i < 20:
        j = 0
        while j < 20:
            if (i==j):
                print(pilotos[i],"tiene", total[j],"puntos")
                j = j +1
            i = i +1
    return ("")

#función que imprime la diferencia al líder del campeonato
def imprime_diferencia():
    i =0
    while i < 19:
        j = 0
        while j < 20:
            if i == j:
                print("La diferencia de ", pilotos[i]," al líder es de", \
                      diferencia_puntos_a_lider(total[j]),"puntos")
                j = j +1
            i = i+1
    return("")
#Función para agregar las posiciones y pilotos a una lista en base a sus indices
def posicion_puntos( ):
    i = 0
    while i < 19:
        posicion = int(input("En que posición quedó el piloto?"))
        x = int(input("Inserte el indice del piloto respecto a la lista"))
        
        if posicion == 1 :
            totalp = puntos_pilotos(25, puntos[x])
            total.insert(x, totalp)
            i = i +1
        elif posicion == 2:
            totalp = puntos_pilotos(18, puntos[x])
            total.insert(x, totalp)
            i = i +1
        elif posicion == 3:
            totalp = puntos_pilotos(15, puntos[x])
            total.insert(x, totalp)
            i = i +1
        elif posicion == 4:
            totalp = puntos_pilotos(12, puntos[x])
            total.insert(x, totalp)
            i = i +1
        elif posicion == 5:
            totalp = puntos_pilotos(10, puntos[x])
            total.insert(x, totalp)
            i = i +1
        elif posicion == 6:
            totalp = puntos_pilotos(8, puntos[x])
            total.insert(x, totalp)
        elif posicion == 7:    
            totalp = puntos_pilotos(6, puntos[x])
            total.insert(x, totalp)
            i = i +1
        elif posicion == 8:
            totalp = puntos_pilotos(4, puntos[x])
            total.insert(x, totalp)
            i = i +1
        elif posicion == 9:
            totalp = puntos_pilotos(2, puntos[x])
            total.insert(x, totalp)
            i = i +1
        elif posicion == 10:
            totalp = puntos_pilotos(1, puntos[x])
            total.insert(x, totalp)
            i = i +1
        else:
            totalp = puntos_pilotos(0, puntos[x])
            total.insert(x, totalp)
            i = i +1
    return total
print(posicion_puntos())

#Puntos por piloto
posiciones = [pilotos, total]
print("\n Campeonato de Pilotos")
print(imprimir_info())

#Puntos por equipo
print("Campeonato de Constructores")
print("Mercedes Benz tiene ", puntos_equipo(total[1], total[3]),"puntos")
print("Red Bull tiene ", puntos_equipo(total[0], total[4])," puntos")
print("Mclaren tiene ", puntos_equipo(total[2], total[8])," puntos")
print("Ferrari tiene ", puntos_equipo(total[5], total[6])," puntos")
print("Aston Martin tiene ", puntos_equipo(total[11], total[13])," puntos")
print("Alpha Tauri tiene ", puntos_equipo(total[7], total[12])," puntos")
print("Alpine tiene ", puntos_equipo(total[9], total[10]), "puntos")
print("Alfa Romeo tiene ",puntos_equipo(total[16], total[17])," puntos")
print("Williams tiene ", puntos_equipo(total[15], total[14]), " puntos")
print("Haas tiene ", puntos_equipo(total[18], total[19]), "puntos")
#Para saber quien es el lider
print("\n El lider del campeonato es ",lider_campeonato(total[0], total[1]))
#Diferencia de puntos entre pilotos
("\n Diferencia de puntos respecto al líder")
print(imprime_diferencia())