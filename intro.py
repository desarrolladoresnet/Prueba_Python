### NOTA:  En todas las funciones es importante retornar el valor esperado.


"""
Esta es un conversor de Celcius a Farenheit y de Farenheit a Celcius,
debe recibir dos parametros, el primero de tipo Boolean, el segudo 
puede ser in Entero o un numero Flotante

Si el primer parametro es True
se realiza una conversion de F a C, 
si es False lo opuesto.

El segundo parametro es la temperatura a recibir.

"""
def temp_conversor(farehnt, temp) -> float:
    if farehnt : r = (9/5) * temp + 32
    else: r = (temp - 32) / 1.8

    return round(r, 2)
    pass
# pytest -k temp_conversor


###################################################################
###################################################################
###################################################################

"""
En suma recursiva la funcion recibe una lista con distintos tipos de datos, 
a veces será una lista dentro de otra lista (array en otros lenguajes).

El punto central es sumar todos los numero enteros, pero solo los enteros, sin conversion de tipos.

Debe poder recorrer los distintos posibles niveles de las listas recibidas usando
un solo bucle for o while.

No siempre los elementos son numeros.

La recursion es un elemento importante para este reto.
"""
def suma_recursiva(data: list) -> int:
    def recursion(data):
        sum = 0
        for element in data:
            if isinstance(element, list):
                sum += recursion(element)
            elif  isinstance(element, int):
                sum += element

        return sum
    return recursion(data)

# pytest -k suma_recursiva

###################################################################
###################################################################
###################################################################

"""
En este ejercicio primero debe abrir el archivo 'mails.txt'. (Te dimos echa esa parte)
Buscar las lineas que empiecen por 'From' y tomar el email que ahi aparece.

Luego debe insertarlo en un diccionario e ir contando la cantidad de veces que aparece ese email.

por ejemplo: {unemail@email.com: 1, otroemail@email: 5}
"""
def property_counter() -> dict:
    my_dict = {}
    file = open("mails.txt")
    for line in file:
        if line.startswith("From"):
            line = line.split()
            for word in line:
                if "@" in word:
                    if word in my_dict:
                        my_dict[word] += 1
                    else:
                        my_dict[word] = 1
    return my_dict

# pytest -v -k property_counter()
# pytest -vv -k property_counter()

###################################################################
###################################################################
###################################################################
"""
    Esta prueba se basa en clases.

    Debe crear la primera clase 'Vehicle', debe recibir una serie de parametros:
        name
        max_speed
        km

    Luego debe crear las siguientes clases que heredan 'Vehicle' y suman un parametro 'medium':
        
    1- 'Car' que debe tener un metodo llamado 'is_running' y devueleve un string con:
        '<nombre_de_la_clase> is running at <maxima_velocidad> kmh'

    2- 'Airplane' que debe tener un metodo llamado 'is_flying' y devueleve un string con:
        '<nombre_de_la_clase> is flying at <maxima_velocidad> kmh'

    3- 'Boat' que debe tener un metodo llamado 'is_navigating' y devueleve un string con:
        '<nombre_de_la_clase> is navigating at <maxima_velocidad> kmh'
"""

class Vehicle:
    def __init__(self, name, max_speed, km) -> None:
        self.name = name
        self.max_speed = max_speed
        self.km = km
        self.engine = False

    def start_engine(self):
        if self.engine: 
            "Engine alredy on"
            return
        self.engine = True
        return f"{self.name} engine started"
    
    def start_stop(self):
        if not self.engine: 
            "Engine alredy off"
            return
        self.engine = True
        return f"{self.name} engine stoped"
    
    
class Ariplain(Vehicle):
    def __init__(self, name, max_speed, km, medium) -> None:
        super().__init__(name, max_speed, km)

        self.medium = medium

    def is_flying(self) -> str:
        msj = f"{self.name} is flying at {self.max_speed} kmh"
        return msj

class Car(Vehicle):
    def __init__(self, name, max_speed, km, medium) -> None:
        super().__init__(name, max_speed, km)

        self.medium = medium

    def is_running(self) -> str:
        return f"{self.name} is running at {self.max_speed} kmh"

class Boat(Vehicle):
    def __init__(self, name, max_speed, km, medium) -> None:
        super().__init__(name, max_speed, km)

        self.medium = medium

    def is_navigating(self) -> str:
        return f"{self.name} is navigating at {self.max_speed} nocks"
    
# pytest -k test_class


###################################################################
###################################################################
###################################################################