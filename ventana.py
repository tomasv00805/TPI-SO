from tkinter import *
from tkinter import ttk
from procesos import *
from archivo import *
from algoritmos import *

procesos=[]    
def cargardatos():
        for lineas in leer_procesos():
            datos = lineas.split(",")
            proceso1 = proceso(datos[0],datos[1],datos[2])
            procesos.append(proceso1)

def estadotextos(self,estado):
    self.txtNombreProceso.config(state=estado)
    self.txtRafaga.config(state=estado)
    self.txtTdeEntrada.config(state=estado)

def btframe2(self,estado):
    self.btnGuardar.config(state=estado)
    self.btnCancelar.config(state=estado)
     
def btframe1(self,estado):
    self.btnNuevo.config(state=estado)
    self.btnModificar.config(state=estado)
    self.btnEliminar.config(state=estado)

def borrartextos(self):
    self.txtNombreProceso.delete(0,END)
    self.txtRafaga.delete(0,END)
    self.txtTdeEntrada.delete(0,END)
    
def encontrarultimo1(matris):
    #encontrar ultimo 1 de cada fila
    matris1=copy.copy(matris)
    ultimos=[]
    for fila in matris1:
        ultimos.append(len(fila)-1-fila[::-1].index(1))
    return ultimos

def tiempodeservisio(prosesos):
    #encontrar el tiempo de servisio de cada proceso
    prosesos1=copy.copy(prosesos)
    tiemposervisio=[]
    for i in prosesos1:
        tiemposervisio.append(i.Rafaga)
    return tiemposervisio

def encontrarelprimero1(matris):
    #encontrar el primero 1 de cada fila
    matris1=copy.copy(matris)
    primers=[]
    for fila in matris1:
        primers.append(fila.index(1))
    return primers

def tiempollegada(prosesos):
    #encontrar el tiempo de llegada de cada proceso
    prosesos1=copy.copy(prosesos)
    tiemposllegada=[]
    for i in prosesos1:
        tiemposllegada.append(i.TdeEntrada)
    return tiemposllegada

def testancia(primers,ultimos):
    #encontrar la distancia entre el primero y el ultimo 1 de cada fila
    primers1=copy.copy(primers)
    ultimos1=copy.copy(ultimos)
    distancias=[]
    for i in range(len(primers)):
        distancias.append(ultimos1[i]-primers1[i])
    return distancias

def trts(tiempoestancia,tiemposervisio):
    #encontrar el tiempo de respuesta de cada proceso
    tiempoestancia1=copy.copy(tiempoestancia)
    tiemposervisio1=copy.copy(tiemposervisio)
    trts=[]
    for i in range(len(tiempoestancia)):
        trts.append(tiempoestancia1[i]/tiemposervisio1[i])
    return trts

def nombreprocesos(procesos):
    #encontrar el nombre de cada proceso
    procesos1=copy.copy(procesos)
    nombres=[]
    for i in procesos1:
        nombres.append(i.Nombre)
    return nombres


    

class Ventana(Frame):
       
    def __init__(self, master=None):
        super().__init__(master,width=700, height=260)
        self.master = master
        self.pack()
        self.create_widgets()
        
       
    def fNuevo(self): 
        borrartextos(self)
        self.txtNombreProceso.focus()
        btframe2(self,NORMAL)
        btframe1(self,DISABLED)
        estadotextos(self,NORMAL)
        self.grid.config(state=DISABLED)        
    
    def fGuardar(self):  
        ##compara los elf.txtNombreProceso.get() con los nombres prosesos
        nombre = self.txtNombreProceso.get()
        rafaga = self.txtRafaga.get()
        tdeentrada = self.txtTdeEntrada.get()
        proceso1 = proceso(nombre,rafaga,tdeentrada)
        procesos.append(proceso1)
        guardar_proceso(proceso1)
        cont=len(procesos)  
        self.grid.insert("", 0, text=cont, values=(proceso1.Nombre, proceso1.Rafaga, proceso1.TdeEntrada))
        borrartextos(self)
        self.txtNombreProceso.focus()
        btframe2(self,DISABLED)
        btframe1(self,NORMAL)
        estadotextos(self,DISABLED)
        self.grid.config(state=NORMAL)         
    
    def fModificar(self):        
        estadotextos(self,NORMAL)
        selected = self.grid.focus()
        #sacar focus de la fila seleccionada
        self.grid.selection_remove(selected)
        values = self.grid.item(selected, "values")
        borrartextos(self)
        self.txtNombreProceso.insert(0, values[0])
        self.txtRafaga.insert(0, values[1])
        self.txtTdeEntrada.insert(0, values[2])
        self.txtNombreProceso.focus()
        btframe2(self,DISABLED)
        btframe1(self,DISABLED)
        self.btnCancelar.config(state=NORMAL)
        self.btnModificar2.config(state=NORMAL)
        self.txtNombreProceso.focus()
    
    def fBTModificar(self):
        selected = self.grid.focus()
        posicion=0
        values = self.grid.item(selected, "values")
        for i in range(len(procesos)):
            if procesos[i].Nombre == values[0] and procesos[i].Rafaga == values[1] and procesos[i].TdeEntrada == values[2]:
                posicion=i
                break
        procesos[posicion].Nombre = self.txtNombreProceso.get()
        procesos[posicion].Rafaga = self.txtRafaga.get()
        procesos[posicion].TdeEntrada = self.txtTdeEntrada.get()
        self.grid.item(selected, text="", values=(procesos[posicion].Nombre, procesos[posicion].Rafaga, procesos[posicion].TdeEntrada))
        borrartextos(self)
        self.txtNombreProceso.focus()
        archivo = open("procesos.txt", "w")
        archivo.close()
        archivo = open("procesos.txt", "a")
        for proseso in procesos:
            archivo.write(proseso.Nombre + "," + proseso.Rafaga + "," + proseso.TdeEntrada)
        archivo.write("\n")
        archivo.close()
        self.btnModificar2.config(state=DISABLED)
        btframe2(self,DISABLED)
        btframe1(self,NORMAL)
        estadotextos(self,DISABLED)
        self.grid.config(state=NORMAL)
            
    def fEliminar(self):
        selected = self.grid.focus()
        values = self.grid.item(selected, "values")
        self.grid.delete(selected)
        for i in range(len(procesos)):
            if procesos[i].Nombre == values[0]:
                del procesos[i]
                break
        archivo = open("procesos.txt", "r")
        lineas = archivo.readlines()
        archivo.close()
        archivo = open("procesos.txt", "w")
        for linea in lineas:
            datos = linea.split(",")
            if datos[0] != values[0]:
                archivo.write(linea)
        archivo.close()
                 
    def fbtnFifo(self):
        procesosFifo= copy.deepcopy(procesos)
        matris=fifo(procesosFifo)
        tllegada= tiempollegada(procesosFifo)
        tfinaliz= encontrarultimo1(matris)
        testancia1= testancia(tllegada,tfinaliz)
        tservicio1= tiempodeservisio(procesosFifo)
        trts1= trts(testancia1,tservicio1)
        nombres=nombreprocesos(procesosFifo)
        ventanaFifo = Toplevel(self)
        ventanaFifo.title("Fifo")
        ventanaFifo.geometry("560x300")
        frame = Frame(ventanaFifo)
        ##grid
        self.gridFifo = ttk.Treeview(frame, columns=("TLlegada", "TServicio", "TFinalizacion", "Testancia", "Tr/Ts"))
        self.grid.column("#0",width=20)
        self.gridFifo.heading("#0", text="Proceso")
        self.gridFifo.column("TLlegada",width=70, anchor=CENTER)
        self.gridFifo.column("TServicio",width=70, anchor=CENTER)
        self.gridFifo.column("TFinalizacion",width=70, anchor=CENTER)
        self.gridFifo.column("Testancia",width=70, anchor=CENTER)
        self.gridFifo.column("Tr/Ts",width=70, anchor=CENTER)
        self.gridFifo.heading("TLlegada", text="TLlegada", anchor=CENTER)
        self.gridFifo.heading("TServicio", text="TServicio", anchor=CENTER)
        self.gridFifo.heading("TFinalizacion", text="TFinalizacion", anchor=CENTER)
        self.gridFifo.heading("Testancia", text="Testancia", anchor=CENTER)
        self.gridFifo.heading("Tr/Ts", text="Tr/Ts", anchor=CENTER)
        self.gridFifo.grid(row=0, column=0, columnspan=2)
        frame.grid(row=0, column=0)
        for i in range(len(matris)):
            self.gridFifo.insert("", 0, text=nombres[i], values=(tllegada[i], testancia1[i], tfinaliz[i], testancia1[i], trts1[i]))
        self.gridFifo.config(state=DISABLED)
        

    def fbtnRR(self):
        procesosFifo= copy.deepcopy(procesos)
        q= int(self.txtRR.get())
        matris=Rowrobin(procesosFifo,q)
        tllegada= tiempollegada(procesosFifo)
        tfinaliz= encontrarultimo1(matris)
        testancia1= testancia(tllegada,tfinaliz)
        tservicio1= tiempodeservisio(procesosFifo)
        trts1= trts(testancia1,tservicio1)
        nombres=nombreprocesos(procesosFifo)
        ventanaFifo = Toplevel(self)
        ventanaFifo.title("RR")
        ventanaFifo.geometry("560x300")
        frame = Frame(ventanaFifo)
        ##grid
        self.gridFifo = ttk.Treeview(frame, columns=("TLlegada", "TServicio", "TFinalizacion", "Testancia", "Tr/Ts"))
        self.grid.column("#0",width=20)
        self.gridFifo.heading("#0", text="Proceso")
        self.gridFifo.column("TLlegada",width=70, anchor=CENTER)
        self.gridFifo.column("TServicio",width=70, anchor=CENTER)
        self.gridFifo.column("TFinalizacion",width=70, anchor=CENTER)
        self.gridFifo.column("Testancia",width=70, anchor=CENTER)
        self.gridFifo.column("Tr/Ts",width=70, anchor=CENTER)
        self.gridFifo.heading("TLlegada", text="TLlegada", anchor=CENTER)
        self.gridFifo.heading("TServicio", text="TServicio", anchor=CENTER)
        self.gridFifo.heading("TFinalizacion", text="TFinalizacion", anchor=CENTER)
        self.gridFifo.heading("Testancia", text="Testancia", anchor=CENTER)
        self.gridFifo.heading("Tr/Ts", text="Tr/Ts", anchor=CENTER)
        self.gridFifo.grid(row=0, column=0, columnspan=2)
        frame.grid(row=0, column=0)
        for i in range(len(matris)):
            self.gridFifo.insert("", 0, text=nombres[i], values=(tllegada[i], testancia1[i], tfinaliz[i], testancia1[i], trts1[i]))
        self.gridFifo.config(state=DISABLED)

    def fbtnSPN(self):
        pass
    
    def fbtnSTR(self):
        pass
    
    def fCancelar(self):
        borrartextos(self)
        self.txtNombreProceso.focus()
        btframe2(self,DISABLED)
        btframe1(self,NORMAL)
        estadotextos(self,DISABLED)
        self.btnModificar2.config(state=DISABLED)
        self.grid.config(state=NORMAL)

    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=93, height=259)        
        self.btnNuevo=Button(frame1,text="Nuevo", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5,y=50,width=80, height=30 )        
        self.btnModificar=Button(frame1,text="Modificar", command=self.fModificar, bg="blue", fg="white")
        self.btnModificar.place(x=5,y=90,width=80, height=30)                
        self.btnEliminar=Button(frame1,text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5,y=130,width=80, height=30)        
        
        frame2 = Frame(self,bg="#d3dde3" )
        frame2.place(x=95,y=0,width=150, height=259)                        
        lbl1 = Label(frame2,text="Nombre Proceso: ")
        lbl1.place(x=3,y=5)        
        self.txtNombreProceso=Entry(frame2)
        self.txtNombreProceso.place(x=3,y=25,width=150, height=20)                
        lbl2 = Label(frame2,text="Rafaga: ")
        lbl2.place(x=3,y=55)        
        self.txtRafaga=Entry(frame2)
        self.txtRafaga.place(x=3,y=75,width=20, height=20)        
        lbl3 = Label(frame2,text="Teimpo de Entrada: ")
        lbl3.place(x=3,y=105)        
        self.txtTdeEntrada=Entry(frame2)
        self.txtTdeEntrada.place(x=3,y=125,width=20, height=20)            
        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="green", fg="white",state=DISABLED)
        self.btnGuardar.place(x=10,y=165,width=60, height=30)
        self.btnModificar2=Button(frame2,text="Modificar", command=self.fBTModificar, bg="green", fg="white",state=DISABLED)
        self.btnModificar2.place(x=80,y=165,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="red", fg="white",state=DISABLED)
        self.btnCancelar.place(x=50,y=210,width=60, height=30)        
        
        
        frame3 = Frame(self,bg="#d3dde3" )
        frame3.place(x=247,y=0,width=420, height=260)
        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3"))    
        self.grid.column("#0",width=30)
        self.grid.column("col1",width=170, anchor=CENTER)
        self.grid.column("col2",width=50, anchor=CENTER)
        self.grid.column("col3",width=50, anchor=CENTER)       
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre Proceso", anchor=CENTER)
        self.grid.heading("col2", text="Rafaga", anchor=CENTER)
        self.grid.heading("col3", text="T de entrada", anchor=CENTER)
        self.grid.pack(side=LEFT, fill= Y)
        sb= Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        
        frame4 = Frame(self, bg="#bfdaff")
        frame4.place(x=550,y=0,width=93, height=280)        
        self.btnFifo=Button(frame4,text="FIFO", command=self.fbtnFifo, bg="blue", fg="white")
        self.btnFifo.place(x=5,y=20,width=80, height=30 )        
        self.btnRR=Button(frame4,text="RR", command=self.fbtnRR, bg="blue", fg="white")
        self.btnRR.place(x=5,y=60,width=80, height=30)     
        self.txtRR=Entry(frame4)
        self.txtRR.place(x=3,y=130,width=150, height=20)  
        lblrr = Label(frame4,text="Quantim: ")
        lblrr.place(x=3,y=100)          
        self.btnSPN=Button(frame4,text="SPN", command=self.fbtnSPN, bg="blue", fg="white")
        self.btnSPN.place(x=5,y=160,width=80, height=30)  
        self.btnSTR=Button(frame4,text="SRT", command=self.fbtnSTR, bg="blue", fg="white")
        self.btnSTR.place(x=5,y=200,width=80, height=30) 
        
        estadotextos(self,DISABLED)
        crear_archivos()
        cargardatos()
        procesos2= copy.deepcopy(procesos)
        #martis= fifo(procesos2)
        #matris2=Rowrobin(procesos2,3)
        #matris3=str(procesos2)
        #print(martis)
        #print(matris2)
        #print(matris3)
        cont=0
        for proceso in procesos:
            cont = cont + 1
            self.grid.insert("", 0, text=cont, values=(proceso.Nombre, proceso.Rafaga, proceso.TdeEntrada))
            
        