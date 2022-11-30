
import logging
logging.basicConfig(format='%(message)s', level=logging.INFO)



while True:
    operation = (input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    if operation.isnumeric() == False:    
        check = input("To nie jest liczba. Czy chcesz spróbować jeszcze raz? Wpisz 'T' jeśli tak lub dowolny inny znak jeśli chcesz zakończyć: ")
        if check == "T":
            continue
        print("Do zobaczenia!")
        break
    else:
        operation_float = float(operation)
        value1 = float(input("Podaj składnik 1.: "))
        value2 = float(input("Podaj składnik 2.: "))
        
        if operation_float == 3 or operation_float == 4:
            value3 = float(input("Podaj składnik 3.: "))

        if operation_float == 4 and (value2 == 0 or value3 == 0):         
            check2 = input("Nie dziel przez 0. Czy chcesz spróbować jeszcze raz? Wpisz 'T' jeśli tak lub dowolny inny znak jeśli chcesz zakończyć: ")
            if check2 == "T":
                continue
            print("Do zobaczenia!")
            break           
        else: 
            if operation_float == 1:
                logging.info(f"Dodaję {value1} i {value2}")
                print(f"Twój wynik to {value1 + value2}")
            if operation_float == 2:
                logging.info(f"Odejmuję {value1} i {value2}")
                print(f"Twój wynik to {value1 - value2}")
            if operation_float == 3:
                logging.info(f"Mnożę {value1} i {value2} i {value3}")
                print(f"Twój wynik to {value1 * value2 * value3}")
            if operation_float == 4:
                logging.info(f"Dzielę {value1} i {value2} i {value3}")
                print(f"Twój wynik to {value1 / value2 / value3}")
        
            check3 = input("Czy chcesz jeszcze coś policzyć? Wpisz 'T' jeśli tak lub dowolny inny znak jeśli chcesz zakończyć: ")
            if check3 == "T":
                continue
            print("Do zobaczenia!")
            break  