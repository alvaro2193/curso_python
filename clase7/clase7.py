d = {}
nombre = []
nota = []
opcion = int(input(print ("Que desea hacer? \n 1. Ingresar alumno \n 2. No ingresar mas alumnos")))

while True:
    if opcion ==1 :
        nom = input("Introduzca el nombre del alumno: ")
        nombre.append (nom)
        nt = int(input("Introduce su nota: "))
        nota.append (nt)
        
        opcion2 = int(input (print ("Desea ingresar mas alumnos 1. Si o 2. No)")))
        
        if opcion2 == 1 : 
            True
        if opcion2 == 2 :
            break
    if opcion ==2:
        print (nombre , '\n', nota )
        
