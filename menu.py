import sys
import csv


print """ menu
-----------------
1)Leer
2)Insertar
3)Exit"""
opcion=int(input("Que queiere realizar? "))    
if opcion == 1:
    with open('data.csv','r')as file:
              data = csv.reader(file, delimiter=',')
              for line in data:
                  print line
        
if opcion == 2:
      nombre = raw_input("Ingresa nombre:")
      email = raw_input("Ingresa email: ")
      with open('data.csv','a')as file:
       data = csv.writer(file, delimiter=',')
       data.writerow([nombre, email])
if opcion == 3:
       sys.exit(0)
       
