


import logging
logging.basicConfig(level=logging.INFO)

def is_number(string):
    try:
        x = float(string)
        return x
    except ValueError:
        print (string, " nie jest liczbą")
        raise


wybor  = int(input ('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:  '))
z = 0

if wybor == 1:
    a0 = input('podaj pierwsza liczbę:  ')
    a = is_number(a0)
    b0 = input('podaj drugą liczbę:  ')
    b = is_number(b0)
    c0 = input('podaj trzecią liczbę:  ')
    c = is_number(c0)

    logging.info ("Dodawanie %s i %s i %s",str(a), str(b),str(c))
    z = a+b+c
    print("Wynik:", z)

elif wybor == 2:
    a0 = input('podaj pierwsza liczbę:  ')
    a = is_number(a0)
    b0 = input('podaj drugą liczbę:  ')
    b = is_number(b0)

    logging.info("Odejmowanie %s od %s", str(a), str(b))
    z = a-b
    print("Wynik:", z)
elif wybor == 3:
    a0 = input('podaj pierwsza liczbę:  ')
    a = is_number(a0)
    b0 = input('podaj drugą liczbę:  ')
    b = is_number(b0)

    logging.info("Mnożenie %s i %s", str(a), str(b))
    z = a*b
    print("Wynik:", z)
elif wybor == 4:
    a0 = input('podaj pierwsza liczbę:  ')
    a = is_number(a0)
    b0 = input('podaj drugą liczbę:  ')
    b = is_number(b0)

    logging.info("Dzielenie %s i %s", str(a), str(b))
    print("Dzielenie", a, "przez", b)
    z = a/b
    print("Wynik:", z)

else:
    print ('podano błędny numer wyboru działania')


print ("")



