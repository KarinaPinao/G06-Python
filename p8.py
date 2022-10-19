class Usuario:


class Agenda:

    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __init__(self):
        self.contactos = []

    def añadirContacto(self, contacto):
        self.contactos.append(contacto)

    def mostrarContacto(self, contacto):
        for contacto in self.contactos:
            print(contacto)

    def buscarContacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(contacto)




usuario = Agenda()