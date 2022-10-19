"""Pregunta 8: Una clase que administre una agenda.
Se debe almacenar en un diccionario dentro de
una lista para cada contacto: el nombre, el teléfono
y el mail. Debe tener los siguientes métodos:
    - Añadir contacto
    - Mostrar contacto
    - Buscar contacto
"""

"""
contacto = {}

def mostrarcontactos():
    print("Nombre\t\tDatos")
    for key in contacto:
        print("{}\t\t{}".format(key, contacto.get(key)))

while True:
    opcion = int(input(" 1. Añadir\n 2. Buscar \n 3. Mostrar\n Ingrese su opción: "))
    if opcion == 1:
        nombre = input("Ingrese el nombre del contacto: ")
        telefono = input("Ingrese el teléfono del contacto: ")
        email = input("Ingrese el email del contacto: ")
        contacto[nombre] = telefono, email
    elif opcion == 2:
        busqueda = input("Ingrese el nombre del contacto que quiere buscar: ")
        if busqueda in contacto:
            print("Los datos del contacto", busqueda, "son:", contacto[busqueda])
        else:
            print("No se encuentra ese nombre en la agenda.")
    elif opcion == 3:
        if not contacto:
            print("Agenda vacía")
        else:
            mostrarcontactos()
    else:
        break

"""


class Agenda:

    def anadir(self):
        self.nombre = input("Ingrese nombre del contacto: ")
        self.telefono = input("Ingrese teléfono del contacto: ")
        self.email = input("Ingrese email del contacto: ")

        self.contacto = {}
        self.contacto[self.nombre] = {"telefono": self.telefono, "email": self.email}
        print("Se ha agregado el contacto", self.nombre,"a la agenda.")
        self.directorio = []
        self.directorio.append(self.contacto))


    def mostrarcontacto(self):
        for key in self.contacto:
            print("Nombre:{}. Datos: {}".format(key, self.contacto.get(key)))

    def buscar(self):
        #self.busqueda = input("Ingrese el contacto que desea buscar: ")
      #  self.contacto for self.contacto in self.directorio:
        #if self.contacto[self.nombre] == self.busqueda:
        #if self.busqueda in self.directorio[self.nombre]:
            print("Los datos del contacto", self.busqueda, "son:", self.contacto[self.busqueda])
        #else:
            print("No se encuentra ese nombre en la agenda.")



  #  def listar(self):
       #if not contacto:
        #    print("Agenda vacía")
       #else:
        #    mostrarcontactos(self)



persona1 = Agenda()
persona1.anadir()
persona1.mostrarcontacto()
#persona1.buscar()

persona2 = Agenda()
persona2.anadir()
persona2.mostrarcontacto()
#persona2.buscar()

#self.directorio = {}
#self.directorio.append([self.contacto])


