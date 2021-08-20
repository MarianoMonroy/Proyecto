"""
Algoritmo de proyecto Mariano Monroy
*El programa ya tendrá los puntos de los pilotos antes de la carrera
"""

"""
Este proceso se repite para todos los pilotos
E0 =entero(input( ¿En que posición acabo el piloto1?))
Mientras igual o menor a 10
 si acabó 1
  total puntos + 25 
 si acabó 2
  total puntos + 18  
 si acabó  3
  total puntos + 15
 si acabó 4
  total puntos + 12 
 si acabó 5
  total puntos + 10 
 si acabó 6
  total puntos + 8 
 si acabó 7
  total puntos + 6 
 si acabó 8
  total puntos + 4 
 si acabó 9
  total puntos + 2 
 si acabó 10
   total puntos + 1
sino
 total puntos + 0
 
Mentras igual o menor a 10
input(Hizo vuelta rápida)
 si hizo vuelta rápida
  total puntos + 1
 sino
  total puntos + 0
Ef= imprime el nombre del piloto con sus puntos actualizados y los guarda en una lista
dónde están ordenados de mayor a menor
"""

"""
E0= puntos totales odrenados de mayor a menor
puntos totales= [x,y,z,...]
diferencia de puntos 1 y 2 = y-x
diferencia de puntos 1 y 3 =z-x 
...Continúa restando los puntos de todos los demás pilotos.
EF= imprime las diferencias de puntos de todos los pilotos al primer lugar
"""
