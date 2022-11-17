import copy
from procesos import *

def ordenarTllegada(procesos):
    procesos.sort(key=lambda x: x.TdeEntrada)
    
def ordenarRafaga(procesos):
    procesos.sort(key=lambda x: x.Rafaga)

def largomatris(procesos):
    ordenarTllegada(procesos)
    largo = 0
    for proceso in procesos:
        largo= largo + proceso.Rafaga
    largo= largo + procesos[0].TdeEntrada
    return largo

def anchomatris(procesos):
    ancho = 0
    ancho= len(procesos)
    return ancho

def crearmatris(procesos):
    ordenarTllegada(procesos)
    largo= largomatris(procesos)
    ancho= anchomatris(procesos)
    matris= [[0 for x in range(largo)] for y in range(ancho)]
    return matris


def fifo(procesos):
    matris= crearmatris(procesos)
    Posicion=0
    ordenarTllegada(procesos)
    for proceso in procesos:
        if(Posicion<proceso.TdeEntrada):
            Posicion= proceso.TdeEntrada
        for i in range(proceso.Rafaga):
            matris[procesos.index(proceso)][Posicion]= 1
            Posicion= Posicion + 1
    return matris

def procesosen0(procesos):
    hay0=0
    for proceso in procesos:
        if(proceso.Rafaga>0):
            hay0= hay0 + 1
    if(hay0 == 0):
        return 1
    else:
        return 0

def Rowrobin(procesos,q):
    procesoscopia= copy.deepcopy(procesos)
    matris= crearmatris(procesoscopia)
    Posicion=0
    quantum= q
    quantumayuda=0
    ordenarTllegada(procesoscopia)
    while(procesosen0(procesoscopia)==0):
        for proceso in procesoscopia:
            if(Posicion<proceso.TdeEntrada):
                Posicion= proceso.TdeEntrada
            if(proceso.Rafaga>0):
                for quantumayuda in range(quantum):
                    matris[procesoscopia.index(proceso)][Posicion]= 1
                    Posicion= Posicion + 1
                    quantumayuda= quantumayuda + 1
                    proceso.Rafaga= proceso.Rafaga - 1
                    if(proceso.Rafaga<=0):
                        break
        
    return matris


# def spn(procesos):
#     matris= crearmatris(procesos)
#     Posicion=0
#     ordenarTllegada(procesos)
#     for proceso in procesos:
#         if(Posicion<proceso.TdeEntrada):
#             Posicion= proceso.TdeEntrada
#         for i in range(proceso.Rafaga):
#             matris[procesos.index(proceso)][Posicion]= 1
#             Posicion= Posicion + 1
            
#     return matris 
    
#short process next
def spn(procesos):
    matris= crearmatris(procesos)
    Posicion=0
    ordenarTllegada(procesos)
    llego= []
    posicion= procesos[0].TdeEntrada
    llego.append(copy.copy(procesos[0]))
    procesos[0].Rafaga= 0
    while(procesosen0(llego)==0):
        for proceso in procesos:
            if(proceso.Rafaga > 0):
                if(proceso.TdeEntrada>posicion):
                    llego.append(copy.copy(procesos[0]))
                    proceso.Rafaga= 0
        ordenarRafaga(llego)
        for i in range(llego[0].Rafaga):
            matris[procesos.index(llego[0])][Posicion]= 1
            Posicion= Posicion + 1
        llego[0].Rafaga=0
        posicion= posicion + 1
            
    return matris
    
# try:
    # except:
    #    pass    

def str(procesos):
    ##short time remaining
    matris= crearmatris(procesos)
    Posicion=0
    ordenarTllegada(procesos)
    
    return matris