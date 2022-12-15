
import logging
logging.basicConfig(format='%(message)s', level=logging.INFO)

import math

def operation():
    operation_number = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie, 5 Potęgowanie, 6 Pierwiastkowanie: ")
    return operation_check(operation_number)

def operation_check(answer):
    operations = ['1', '2', '3', '4', '5', '6']
    if answer not in operations:
        print("Błędna wartość.")
        exit_check()
    else:
        return get_value(answer)

def exit_check():    
    check = input("Czy chcesz spróbować jeszcze raz? Wpisz 'T' jeśli tak lub dowolny inny znak jeśli chcesz zakończyć: ")
    if check == "T":
        operation()
    else:
        print("Do zobaczenia!")
        exit(0)  

def get_value(operation_number):
    values = (input("Podaj rozdzielone przecinkiem wartości do obliczeń: ")).split(",")
    for i in values:
        if not i.lstrip('-').isnumeric():
            print("Nieprawidłowy format danych.")
            exit_check()
    else:
        values = [float(i) for i in values]
    return calculations(operation_number, values)

def calculations(operation_number, values): 
    if operation_number == "1":
        logging.info(f"Dodaję: {values}")
        print(f"Twój wynik to: {add(values)}")
        exit_check()
    elif operation_number == "2":
        logging.info(f"Odejmuję: {values}")
        print(f"Twój wynik to {subtract(values)}")
        exit_check()
    elif operation_number == "3":
        logging.info(f"Mnożę: {values}")
        print(f"Twój wynik to: {multiply(values)}")
        exit_check()
    elif operation_number == "4":
        if not all(values[1:]):
            print("Nie dziel przez 0!")
            exit_check()
        else:
            logging.info(f"Dzielę: {values}")
            print(division(values))
            exit_check()
    elif operation_number == "5":
        logging.info(f"Potęguję: {values[:2]}")
        print(f"Twój wynik to: {power(values)}")
        exit_check()
    elif operation_number == "6":
        if values[0] < 0:
            print("Wartość musi być >= 0.")
            exit_check()
        else:
            logging.info(f"Wyciągam pierwiastek kwadratowy z: {values[0]}")
            print(f"Twój wynik to: {square_root(values[0])}")
            exit_check()

def add(values):
    return sum(values)
def subtract(values):        
    result = values[0]
    for i in values[1:]:
        result = result - i    
    return result
def multiply(values):
    result = values[0]
    for i in values[1:]:
        result = result * i
    return result
def division(values):
    result = values[0]
    for i in values[1:]:
        result = result / i
    return result
def power(values):
    return pow(values[0], values[1])
def square_root(values):
    return math.sqrt(values)

operation()

