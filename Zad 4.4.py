
import logging
logging.basicConfig(format='%(message)s', level=logging.INFO)

operations = ['1', '2', '3', '4']

def exit_check():    
    return input("Czy chcesz spróbować jeszcze raz? Wpisz 'T' jeśli tak lub dowolny inny znak jeśli chcesz zakończyć: ")


while True:
    operation = (input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))   
    if operation not in operations:
        print("Błędna wartość.")
        if exit_check() == "T":
            continue
        print("Do zobaczenia!")
        break
    else:
        value1 = input("Podaj składnik 1.: ")
        if not value1.isnumeric():
            print("To nie jest liczba.")
            if exit_check() == "T":
                continue
            print("Do zobaczenia!")
            break
        value1 = float(value1)
        value2 = input("Podaj składnik 2.: ")
        if not value2.isnumeric():
            print("To nie jest liczba.")
            if exit_check() == "T":
                continue
            print("Do zobaczenia!")
            break
        value2 = float(value2)
        if operation == '1' or operation == '3':
            value3 = input("Podaj składnik 3.: ")
            if not value3.isnumeric():
                print("To nie jest liczba.")
                if exit_check() == "T":
                    continue
                print("Do zobaczenia!")
                break
            value3 = float(value3)
        if operation == '4' and value2 == 0:         
            print("Nie dziel przez 0.")
            if exit_check() == "T":
                continue
            print("Do zobaczenia!")
            break           
        else: 
            if operation == '1':
                logging.info(f"Dodaję {value1} i {value2} i {value3}")
                print(f"Twój wynik to {value1 + value2 + value3}")
            if operation == '2':
                logging.info(f"Odejmuję {value1} i {value2}")
                print(f"Twój wynik to {value1 - value2}")
            if operation == '3':
                logging.info(f"Mnożę {value1} i {value2} i {value3}")
                print(f"Twój wynik to {value1 * value2 * value3}")
            if operation == '4':
                logging.info(f"Dzielę {value1} i {value2}")
                print(f"Twój wynik to {value1 / value2}")
        
            print("Czy chcesz jeszcze coś policzyć?") 
            if exit_check() == "T":
                continue
            print("Do zobaczenia!")
            break  