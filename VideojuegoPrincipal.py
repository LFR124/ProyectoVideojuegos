'''Administra las listas de consolas y juegos y rentas registradas.
o Para fines de administración del negocio, cuenta con las funciones necesarias para generar los siguientes
reportes:
§ Ganancias por consola (cada renta tiene una consola la cual tiene costo por hora).
§ Ganancias totales.
o Para cerrar una renta, se deberá mostrar en pantalla la lista de rentas activas y el usuario seleccionará la
renta a cerrar.
o Ofrece un menú con las siguientes funciones:
§ Registrar Consola
§ Buscar Consola
§ Ver consolas
§ Registrar Juego
§ Buscar Juego
§ Rentar
§ Terminar renta
§ Ver rentas activas
§ Ver rentas inactivas
§ Generar reporte:
• Ganancias por consola.
• Ganancias totales'''
import Contratos as j
import Renta as r
class Principal:

    def __init__(self):
        self.obj_contrato=j.Contratos()
     
    
    def menu(self):
        self.obj_contrato=j.Contratos()
        print("\n-------------------| Bienvenido |------------------")
        self.ciclo=True
        #i1=True
        #i2=True
        i3=True
        i4=True
        i5=True
        while (self.ciclo==True):
            i3=True
            i4=True
            print("\n1) Registrar consola")
            print("2) Buscar consola")
            print("3) Ver consolas")
            print("4) Registrar juego")
            print("5) Rentar")
            print("6) Terminar renta")#status inactivo
            print("7) Ver rentas activas")
            print("8) Ver rentas inactivas")
            print("9) Generar reporte")
            print("10) Salir\n")
            self.opcion=int(input("*Ingresa una opcion: "))
            if(self.opcion==1):
                print("Registar Consola")
                self.obj_contrato.registrar_consola()
                print("________________________________")
               
            elif(self.opcion==2):
                print("Buscar Consola")
                self.busqueda=input("Nombre de la consola: ")
                for i in range(0, len(self.obj_contrato.funciones)):
                    self.resultado=self.obj_contrato.funciones[i].consultar(self.busqueda)
                    if(self.resultado!=None):
                        print("\n"+self.resultado)
                print("________________________________")

            elif(self.opcion==3):
                print("Ver Consolas")
                for i in range(0, len(self.obj_contrato.funciones)):
                    self.resultado=self.obj_contrato.funciones[i].consulta()
                    if(self.resultado!=None):
                        print("\n"+self.resultado)
                print("________________________________")

            elif(self.opcion==4):
                print("Registar Juego")
                '''while i2==True:
                    for i in range(0, len(self.obj_contrato.dulces)):
                       self.resultado=self.obj_contrato.funciones[i].inventario()
                    if(self.resultado!=None):
                       print("\n"+self.resultado)
                    print("1)Salir")
                    clave=input("Selecciona una consola: ")
                    
                       for i in range(0, len(self.obj_contrato.rentas)):
                       self.resultado=self.obj_contrato.rentas[i].comprar(clave,cantidad)
                       if(self.resultado!=None):
                        print("\n"+self.resultado)  
                      i5=False
                    el

               
                
                print("________________________________")'''
            
            elif(self.opcion==5):
                self.obj_contrato.registrar_renta()

                print("________________________________")
            elif(self.opcion==6):


                print("________________________________")
            elif(self.opcion==7):
                
                print("________________________________")
               
            elif(self.opcion==9):
                print("Generar reporte")
                while i5==True:
                
                    print("\n1) Ganancias por consola")
                    print("2) Imprimir inventario")
                    print("3) Buscar Producto")
                    self.op=int(input("Ingresa una opcion: "))
                    if self.op==1:
                        print("Ganancias por consola")
                        self.obj_contrato.ganancias_por_consola()
                        print("________________________________")
                    
                    elif self.op==2:
                        print("Ganancias Totales")

                        print("________________________________")
                    else:
                        i4=False

            else:
                self.ciclo=False
                print("-----------------------------------| Adiós |-------------------------------")

p=Principal()
p.menu()