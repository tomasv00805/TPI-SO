from procesos import *

def crear_archivos():
    archivo = open("procesos.txt", "a")
    archivo.close()
    
def guardar_proceso(proceso):
    archivo = open("procesos.txt", "a")
    archivo.write(proceso.Nombre + "," + str(proceso.Rafaga) + "," + str(proceso.TdeEntrada)+"\n")
    archivo.close()
    
def leer_procesos():
    archivo = open("procesos.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
    lista_procesos=[]
    for linea in lineas:
        lista_procesos.append(linea)
    return lista_procesos