
from tkinter import *
from ventana import *


def main():
    root = Tk()
    root.wm_title("Tabla procesos")
    app = Ventana(root) 
    app.mainloop()



if __name__ == "__main__":
    main()