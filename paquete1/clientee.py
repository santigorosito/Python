class cliente: 
    def __init__(self, nombre, edad, mail, profesion):
        self.nombre = nombre
        self.edad = edad
        self.mail = mail
        self.profesion = profesion

    def comprar (self, producto, lugar):
        producto = producto
        lugar = lugar
        print(f"El cliente {self.nombre} ha comprado {producto} en {lugar}")
        self.enviar_factura()

    def enviar_factura(self):
        print(f"Se le ha mandado un correo con la factura de su compra a su mail {self.mail}")
    
    def __str__(self):
        return f"Se ha creado el usuario {self.nombre}"