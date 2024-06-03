# import pytest
from intro import *

def test_temp_conversor():
    assert temp_conversor(True, 95) == 203 , "TEST 1.1 -El valor para los grados en Fahrenheit no es correcto"
    assert temp_conversor(False, 95) == 35, "TEST 1.2 -El valor para los grados en Celcius no es correcto"
    assert temp_conversor(True, 37) == 98.6, "TEST 1.3 -El valor para los grados en Fahrenheit no es correcto"
    assert temp_conversor(False, 37) == 2.78, "TEST 1.4 -El valor para los grados en Celcius no es correcto"



def test_suma_recursiva():
    assert suma_recursiva([1, 2, 3, 4, 5]) == 15, "TEST 2.1 - resultado incorrecto"
    assert suma_recursiva([1, 2, 3, 4, 5, 6.5, [1,2,3,4, [5]]]) == 30, "TEST 2.2 - resultado incorrecto"
    assert suma_recursiva([37, 42, {}, "5", [1,2,3,4,5, [3]]]) == 97, "TEST 2.3 - resultado incorrecto"
    assert suma_recursiva(["3", 3.14, 5, [9, 7, [45, 8.9], [5], 8]]) == 79, "TEST 2.3 - resultado incorrecto"


def test_property_counter():
    response = {'stephen.marquard@uct.ac.za': 4, 'louis@media.berkeley.edu': 6, 'zqian@umich.edu': 8, 'rjlowe@iupui.edu': 4, 'cwen@iupui.edu': 10, 'gsilver@umich.edu': 6, 'wagnermr@iupui.edu': 2, 'antranig@caret.cam.ac.uk': 2, 'gopal.ramasammycook@gmail.com': 2, 'david.horwitz@uct.ac.za': 8, 'ray@media.berkeley.edu': 2}

    result = property_counter()
    assert isinstance(result, dict) == True, "No es un diccionario"
    assert response == result, "Los diccionarios no son iguales"



def test_class():
    avion = Ariplain("Boeing", 400, 5000.36, "air")
    assert isinstance(avion, Vehicle), "No hereda de 'Vehicle'"
    assert isinstance(avion, Ariplain), "El nombre de la Clase Airplane debe ser 'Ariplain'"
    assert avion.engine == False, "El 'engine' debe empezar en False."
    assert avion.start_engine() == f"{avion.name} engine started", "Las cadenas no son iguales"
    assert avion.engine == True
    assert avion.medium == "air"
    assert avion.is_flying() == "Boeing is flying at 400 kmh", "Las cadenas no son iguales"

    carro = Car("Mustang", 300, 5555, "land")
    assert isinstance(carro, Vehicle), "No hereda de 'Vehicle'"
    assert isinstance(carro, Car), "El nombre de la Clase Car debe ser 'Car'"
    assert carro.engine == False, "El 'engine' debe empezar en False."
    assert carro.start_engine() == f"{carro.name} engine started", "Las cadenas no son iguales"
    assert carro.engine == True
    assert carro.medium == "land"
    assert carro.is_running() == "Mustang is running at 300 kmh", "Las cadenas no son iguales"

    barco = Boat("Barquito", 20, 300, "Water")
    assert isinstance(barco, Vehicle), "No hereda de 'Vehicle'"
    assert isinstance(barco, Boat), "El nombre de la Clase Boat debe ser 'Boat'"
    assert barco.engine == False, "El 'engine' debe empezar en False."
    assert barco.start_engine() == f"{barco.name} engine started", "Las cadenas no son iguales"
    assert barco.engine == True
    assert barco.medium == "Water"
    assert barco.is_navigating() == "Barquito is navigating at 20 nocks", "Las cadenas no son iguales"