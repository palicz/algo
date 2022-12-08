# Írjon egy Python függvényt, amely a bekért egész számról eldönti, hogy páros-e!

def paros():

    try:
        n = int(input("Adj meg egy egész számot: "))

        if n % 2 == 0:
            return "Páros"
        else:
            return "Páratlan"

    except ValueError:
        return "Nem egész számot adtál meg"

if __name__ == "__main__":
    print(paros())

# Teszt elemek: páros egész szám, páratlan egész szám, negatív számok