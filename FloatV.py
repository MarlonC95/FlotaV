import os
import re

def Com_placa(placa):
    patron = r'^[A-Z]{3}-[0-9]{4}$'
    return re.match(patron, placa)

def Com_Fecha(fecha):
    patron = r'^\d{2}-\d{2}-\d{4}$'
    return re.match(patron, fecha)

class nodo:
    def __init__(self, dato):
        self.dato = dato
        self.sig = None

class Vehiculo:
    def __init__(self, placa, marca, modelo, año, kilometraje, historial_mantenimiento):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__kilometraje = kilometraje
        self.__historial_mantenimiento = historial_mantenimiento

    @property
    def placa(self):
        return self.__placa

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def año(self):
        return self.__año

    @property
    def kilometraje(self):
        return self.__kilometraje

    @property
    def historial_mantenimiento(self):
        return self.__historial_mantenimiento
    
    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @año.setter
    def año(self, año):
        if año < 1900 or año > 2025:
            raise ValueError("El año debe estar entre 1900 y 2025")
        else:
            self.__año = año

    @kilometraje.setter
    def kilometraje(self, kilometraje):
        if kilometraje < 0:
            raise ValueError("El kilometraje no puede ser negativo")
        else:
            self.__kilometraje = kilometraje

    @historial_mantenimiento.setter
    def historial_mantenimiento(self, historial_mantenimiento):
        self.__historial_mantenimiento = historial_mantenimiento

    def agregar_historial_mantenimiento(self, mantenimiento):
        self.__historial_mantenimiento.agregar_mantenimiento(mantenimiento)

    def mostrar_historial_mantenimiento(self):
        self.__historial_mantenimiento.mostrar_mantenimiento()
    
    def costo_Tmantenimiento(self):
        costo_total = 0
        actual = self.__historial_mantenimiento.primero
        while actual is not None:
            costo_total += actual.dato.costo
            actual = actual.sig
        return costo_total
    
class mantenimiento:
    def __init__(self, fecha, descripcion, costo):
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__costo = costo

    @property
    def fecha(self):
        return self.__fecha

    @property
    def descripcion(self):
        return self.__descripcion

    @property
    def costo(self):
        return self.__costo
    
    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion

    @costo.setter
    def costo(self, costo):
        self.__costo = costo

    def __str__(self):
        return f"Fecha: {self.__fecha}, Descripción: {self.__descripcion}, Costo: {self.__costo}"

class Lista_mantenimientos:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_mantenimiento(self, mantenimiento):
        if self.primero is None:
            self.primero = nodo(mantenimiento)
            self.ultimo = self.primero
        else:
            nuevo_nodo = nodo(mantenimiento)
            self.ultimo.sig = nuevo_nodo
            self.ultimo = nuevo_nodo

    def mostrar_mantenimiento(self):
        actual = self.primero
        while actual is not None:
            print(actual.dato)
            actual = actual.sig
        print()

    def eliminar_mantenimiento(self, mantenimiento):
        actual = self.primero
        anterior = None
        while actual is not None and actual.dato != mantenimiento:
            anterior = actual
            actual = actual.sig
        if actual is not None:
            if anterior is None:
                self.primero = actual.sig
            else:
                anterior.sig = actual.sig
            return True
        return False


class FlotaV:
    def __init__(self):
        self.__vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.__vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        for vehiculo in self.__vehiculos:
            print(f"Placa: {vehiculo.placa}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.año}, Kilometraje: {vehiculo.kilometraje}")

    def eliminar_vehiculo(self, placa):
        for vehiculo in self.__vehiculos:
            if vehiculo.placa == placa:
                self.__vehiculos.remove(vehiculo)
                return True
        return False

    def buscar_vehiculo(self, placa):
        for vehiculo in self.__vehiculos:
            if vehiculo.placa == placa:
                return vehiculo
        return None
    

def Agregar_vehiculo():
    print("Agregando un nuevo vehiculo")
    print("------------------------------")
    print("Ingreso de datos de la placa [AAA-0000]")
    placa = input("Ingrese la placa del vehiculo: ")
    if not Com_placa(placa):
        print("Placa invalida")
        return
    marca = input("Ingrese la marca del vehiculo: ")
    modelo = input("Ingrese el modelo del vehiculo: ")
    año = int(input("Ingrese el año del vehiculo: "))
    kilometraje = int(input("Ingrese el kilometraje del vehiculo: "))
    mantenimientos = Lista_mantenimientos()
    vehiculo = Vehiculo(placa, marca, modelo, año, kilometraje, mantenimientos)
    flota.agregar_vehiculo(vehiculo)
    print("Vehiculo agregado correctamente")

def Buscar_vehiculo():
    placa = input("Ingrese la placa del vehiculo que desea buscar: ")
    vehiculo = flota.buscar_vehiculo(placa)
    if vehiculo is None:
        print("Vehiculo no encontrado")
    else:
        print(f"Placa: {vehiculo.placa}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.año}, Kilometraje: {vehiculo.kilometraje}")

def Agregar_mantenimiento_vehiculo():
    print("Agregando un nuevo mantenimiento")
    print("------------------------------")
    placa = input("Ingrese la placa del vehiculo: ")
    vehiculo = flota.buscar_vehiculo(placa)
    if vehiculo is None:
        print("Vehiculo no encontrado")
        return
    print("Ingreso de datos de la fecha [DD-MM-AAAA]")
    fecha = input("Ingrese la fecha del mantenimiento: ")
    if not Com_Fecha(fecha):
        print("Fecha invalida")
        return    
    descripcion = input("Ingrese la descripcion del mantenimiento: ")
    costo = float(input("Ingrese el costo del mantenimiento: "))
    mantenimiento_obj = mantenimiento(fecha, descripcion, costo)
    vehiculo.agregar_historial_mantenimiento(mantenimiento_obj)
    print("Mantenimiento agregado correctamente")
    
def Editar_Vehiculo():
    placa = input("Ingrese la placa del vehiculo que desea editar: ")
    vehiculo = flota.buscar_vehiculo(placa)
    if vehiculo is None:
        print("Vehiculo no encontrado")
        return
    marca = input("Ingrese la marca del vehiculo: ")
    modelo = input("Ingrese el modelo del vehiculo: ")
    año = int(input("Ingrese el año del vehiculo: "))
    kilometraje = int(input("Ingrese el kilometraje del vehiculo: "))
    vehiculo.marca = marca
    vehiculo.modelo = modelo
    vehiculo.año = año
    vehiculo.kilometraje = kilometraje
    print("Vehiculo editado correctamente")

def Eliminar_vehiculo():
    placa = input("Ingrese la placa del vehiculo que desea eliminar: ")
    if flota.eliminar_vehiculo(placa):
        print("Vehiculo eliminado correctamente")
    else:
        print("Vehiculo no encontrado")
    
def eliminar_mantenimiento():
    placa = input("Ingrese la placa del vehiculo: ")
    vehiculo = flota.buscar_vehiculo(placa)
    if vehiculo is None:
        print("Vehiculo no encontrado")
        return
    fecha = input("Ingrese la fecha del mantenimiento que desea eliminar: ")
    mantenimiento_obj = mantenimiento(fecha, "", 0)
    if vehiculo.historial_mantenimiento.eliminar_mantenimiento(mantenimiento_obj):
        print("Mantenimiento eliminado correctamente")
    else:
        print("Mantenimiento no encontrado")

def Mostrar_vehiculos():
    flota.mostrar_vehiculos()

def Mostrar_mantenimientos():
    placa = input("Ingrese la placa del vehiculo: ")
    vehiculo = flota.buscar_vehiculo(placa)
    if vehiculo is None:
        print("Vehiculo no encontrado")
        return
    vehiculo.mostrar_historial_mantenimiento()

def Mostrar_costo_mantenimientos():
    placa = input("Ingrese la placa del vehiculo: ")
    vehiculo = flota.buscar_vehiculo(placa)
    if vehiculo is None:
        print("Vehiculo no encontrado")
        return
    print("Costo total de mantenimientos: ", vehiculo.costo_Tmantenimiento())

flota = FlotaV()

def menu():
    while True:
        os.system("cls")
        print("|=========================================|")
        print("|                    Menu:                |")
        print("|=========================================|")
        print("|1. Agregar vehiculo                      |")
        print("|2. Buscar vehiculo                       |")
        print("|3. Agregar mantenimiento                 |")
        print("|4. Editar vehiculo                       |")
        print("|5. Eliminar vehiculo                     |")
        print("|6. Eliminar mantenimiento                |")
        print("|7. Mostrar vehiculos                     |")
        print("|8. Mostrar mantenimientos                |")
        print("|9. Mostrar costo de mantenimientos       |")
        print("|0. Salir                                 |")
        print("|=========================================|")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            os.system("cls")
            print("Agregar vehiculo")
            print("================")
            Agregar_vehiculo()
        elif opcion == "2":
            os.system("cls")
            print("Buscar vehiculo")
            print("===============")
            Buscar_vehiculo()
        elif opcion == "3":
            os.system("cls")
            print("Agregar mantenimiento")
            print("====================")
            Agregar_mantenimiento_vehiculo()
        elif opcion == "4":
            os.system("cls")
            print("Editar vehiculo")
            print("===============")
            Editar_Vehiculo()
        elif opcion == "5":
            os.system("cls")
            print("Eliminar vehiculo")
            print("================")
            Eliminar_vehiculo()
        elif opcion == "6":
            os.system("cls")
            print("Eliminar mantenimiento")
            print("=====================")
            eliminar_mantenimiento()
        elif opcion == "7":
            os.system("cls")
            print("Mostrar vehiculos")
            print("================")
            Mostrar_vehiculos()
        elif opcion == "8":
            os.system("cls")
            print("Mostrar mantenimientos")
            print("=====================")
            Mostrar_mantenimientos()        
        elif opcion == "9":
            os.system("cls")
            print("Mostrar costo de mantenimientos")
            print("================================")
            Mostrar_costo_mantenimientos()
        elif opcion == "0":
            os.system("cls")
            print("Gracias por usar el programa de la flota de vehiculos :D")
            print("========================================================")
            print("Hasta luego :D")
            break
        else:
            print("Opcion invalida")
        input("Presione una tecla para continuar")

menu()