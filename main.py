"""
    Para la prueba el primer paso es crear un entorno virtual.

    Active el entorno virtual e instale las dependencias.

    Para correr todas la pruebas coloque en la consola a nivel del proyecto: pytest

    La prueba tiene 4 partes:
        1 - Un conversor de Celcius a Farenheit y de Farenheit a Celcius
        2 - Un buscador de numeros primos
        3 - Una suma recursiva
        4 - Un contador de propiedades
        5 - Un reto de Clases

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
def temp_conversor() -> float:
    pass

# pytest -k temp_conversor

###################################################################
###################################################################
###################################################################

# RETO 2

"""
    El siguiente reto se basa en obtener todos los numeros primos segun un rango dado
    y  retornar una lista con los numeros primos encontrados.

    Ya te damos los numeros iniciales con los que vas a trabajar.
    Para esto omitimos el 0 y el 1 por facilidad y empezamos con el 2 y el 3.

    No es obligatorio, pero implenta un contador y cuenta la cantidad de llamas que se hacen a la funcion.
    Intenta que la misma sea lo mas eficiente posible.
"""

def prime_numbers(number: int) -> list:
    primes = [2, 3]
    counter = 0
    
    pass

# pytest -k prime_numbers

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
    pass

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
    pass

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
    pass
    
class Car:
    pass

class Boat:
    pass

class Airplane:
    pass
    
# pytest -k test_class


###################################################################
###################################################################
###################################################################
