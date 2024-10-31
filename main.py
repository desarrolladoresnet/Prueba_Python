"""
    Para la prueba el primer paso es crear un entorno virtual.

    Active el entorno virtual e instale las dependencias.

    Para correr todas la pruebas coloque en la consola a nivel del proyecto: pytest

    La prueba tiene 4 partes:
        1 - Un conversos de Celcius a Farenheit y de Farenheit a Celcius
        2 - Una suma recursiva
        3 - Un contador de propiedades
        4 - Un reto de Clases

    No debe cambiar los nombres de las funciones.
    Debajo de cada funcion hay un camndo para ejecutar las pruebas de esa funcion unicamente.

    CONSEJO: Todos los retos fueron probados y tienen solucion, tomese su tiempo para encontrar las soluciones.
    Las pruebas te daran pistas importantes de como resolver los retos planteados.

    IMPORTANTE: No hacer uso de IAs, digase ChatGPT, Gemini, Copilot etc..., nos interesa conocer tu manejo de
    logica, ademas de que la sintaxis la puedes buscar en la documetacion o en StackOverflow.
"""


### NOTA:  En todas las funciones es importante retornar el valor esperado.

### NOTA2: Bajo ningun concepto manipule el archivo de test_main.py

###################################################################
###################################################################
###################################################################

#  RETO 1

"""
Esta es un conversor de Celcius a Farenheit y de Farenheit a Celcius,
debe recibir dos parametros, el primero de tipo Boolean, el segundo 
puede ser un numero Entero o un numero Flotante

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


def prime_numbers(number: int) -> list:
    primes = [2, 3]
    counter = 0
    n = 5
    
    while n < number:
        is_prime = True

        for i in primes:
            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(n)
            
        n += 2
        counter += 1
        
    return primes



###################################################################
###################################################################
###################################################################

# RETO 2

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

# RETO 3

"""
En este ejercicio primero debe abrir el archivo 'mails.txt'. (Te dimos echa esa parte)

Buscar las lineas que empiecen por 'From' y tomar el email que ahi aparece.

Luego debe insertarlo en un diccionario e ir contando la cantidad de veces que aparece ese email.

Por ejemplo: {unemail@email.com: 1, otroemail@email: 5}
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

    Debe crear la primera clase 'Vehicle', debe recibir y poseer una serie de parametros:
        name
        max_speed
        km

        Debe tener el metodo start_engine():
            Si el engine esta en on debe enviar el siguiente msj: "Engine alredy on"
                
            Si esta en off envia el siguiente msj: <nombre> engine started"
            Ademas debe cambiar el estado del engine a true

    Luego debe crear las siguientes clases que heredan 'Vehicle' y suman un parametro 'medium' (este parametro solo lo poseen las clases que heredan):
        
    1- 'Car' que debe tener un metodo llamado 'is_running' y devueleve un string con:
        '<nombre> is running at <maxima_velocidad> kmh'

    2- 'Airplane' que debe tener un metodo llamado 'is_flying' y devueleve un string con:
        '<nombre> is flying at <maxima_velocidad> kmh'

    3- 'Boat' que debe tener un metodo llamado 'is_navigating' y devueleve un string con:
        '<nombre> is navigating at <maxima_velocidad> kmh'
"""

class Vehicle:
    def __init__(self, name, max_speed, km) -> None:
        self.name = name
        self.max_speed = max_speed
        self.km = km
        self.engine = False

    def start_engine(self):
        if self.engine: 
            return "Engine alredy on"
            
        self.engine = True
        return f"{self.name} engine started"
    
    def start_stop(self):
        if not self.engine: 
            return "Engine alredy off"
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
