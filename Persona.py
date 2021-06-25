class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentation(self):
        print("Hola! Soy {self.nombre} y tengo {self.edad} años")


nombre = "Alberto"
persona_1 = Persona(nombre, 20)
# person.presentation() Es incorrecto
persona_1.presentation()


# EJERCICIO1


class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento, puesto):
        # Invoca a  la clase Persona
        Persona.__init__(self, nombre, edad)
        # Nuevos atributos
        self.departamento = departamento
        self.puesto = puesto


# EJERCICIO2
class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento, puesto):
        # Invoca a  la clase Persona
        Persona.__init__(self, nombre, edad)
        # Nuevos atributos
        self.departamento = departamento
        self.puesto = puesto

    def presentation(self):
        print("Hola! Soy {self.nombre} y tengo {self.edad} años. Trabajo en el departamento {self.departamento} como {self.puesto} ")


trabajador1 = Trabajador("Andrés", "30", "Big Data", "Ingeniero de datos")
trabajador1.presentation()


# EJERCICIO3
# self.nombre es para la definición del valor dentro de la clase
# la variable nombre es un valor para dicho atributo de la clase

# EJERCICIO4-

class Trabajador(Persona):
    # Clase que representa a un trabajador"""
    def __init__(self, nombre, edad, departamento="Data", puesto="Analyst"):
        # Invoca a  la clase Persona
        Persona.__init__(self, nombre, edad)
        # Nuevos atributos
        self.departamento = departamento
        self.puesto = puesto

    def presentation(self):
        print("Hola! Soy {self.nombre} y tengo {self.edad} años. Trabajo en el departamento {self.departamento} como {self.puesto} ")


# EJERCICIO5

my_var_list = ['Andrea', '42', 'Ventas', 'Manager']
trabajador_2 = Trabajador(*my_var_list)
trabajador_2.presentation()

# EJERCICIO6

my_var_dict = {'nombre': 'Andrea', 'edad': '42', 'departamento': 'Ventas', 'puesto': 'Manager'}
trabajador_3 = Trabajador(my_var_dict['nombre'], my_var_dict['edad'], my_var_dict['departamento'],
                          my_var_dict['puesto'])
trabajador_3.presentation()
