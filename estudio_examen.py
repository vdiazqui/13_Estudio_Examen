class Ciencia:
    
    def __init__(self,nombre,rama):
        self.nombre= nombre
        self.rama= rama
    def mostrar_info(self):
        dificultad = (1,2,3,4,5)
        if self.rama == "salud":
            print(self.nombre, "eso es para debiles, la dificultad es nivel", dificultad [0])
        elif self.rama == "mates" or "ingenieria":
            print(self.nombre, "así me gusta, la dificultad es nivel", dificultad [4])
        else:
            print("Nada, eso no tiene ni dificultad")

def main():
    tonto= Ciencia(input('Introduzca su nombre: '),input("Introduzca su rama de la ciencia: "))
    tonto.mostrar_info()
    
if __name__=="__main__":
    main()