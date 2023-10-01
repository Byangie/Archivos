#Ejercicio
from io import open

def agregar_tarea(*tareas):
    fichero = open('tareas.txt', 'a')

    for tarea in tareas:
        nombre, descripcion = tarea
        fichero.write(f"{nombre} - {descripcion}\n")

def listar_tareas():
    indice = 1
    with open('tareas.txt', 'r') as fichero:
        print("----------TAREAS LISTADAS----------")
        for i in fichero:
            print(f" {indice}.{i.strip()}")
            indice+=1
        print("-----------------------------------")

#completado
    indice = 1
    with open('Tareas_Completadas.txt', 'r') as fichero2:
        print("----------TAREAS COMPLETADAS----------")
        for e in fichero2:
            print(f" {indice}.{e.strip()}")
            indice+=1
        print("--------------------------------------")

        
def completado():
    fichero = open('tareas.txt', 'r+')

    lineas = fichero.readlines()

    tareas = int(input("Ingrese el número de la tarea que completaste: "))

    fichero2 = open('Tareas_Completadas.txt', 'a')

    fichero2.write(lineas[tareas-1])
    del(lineas[tareas-1])

    fichero.seek(0)
    fichero.writelines(lineas)
    
#Bloque principal
numero_tareas = int(input("Ingrese el numero de tareas que agregaras: "))
for i in range(numero_tareas):
    nombre_tarea = input("Agregue el nombre de la tarea: ")
    descripcion_tarea = input("Agregue una descripción para la tarea: ")
    agregar_tarea((nombre_tarea, descripcion_tarea))    

listar_tareas()

completado()

print("\nFinalisaste el proceso de tareas")
