# Írjon egy Python függvényt, amely a bekért évszámról eldönti, hogy az adott év szökőév-e!

# minden néggyel osztható év, kivéve a százzal is oszthatókat, viszont szökőévek a 400-zal osztható évek is

def szokoev():

    try:
        n = int(input("Adj meg egy évszámot: "))

        if n % 400 == 0:
            return "Szökőév"
        elif n % 4 == 0 and n % 100 != 0:
            return "Szökőév"
        else:
            return "Nem szökőév"

    except ValueError:
        return "Nem évszámot adtál meg"

if __name__ == "__main__":
    print(szokoev())

# Teszt elemek: 100-al osztható évszám, 400-al osztható évszám, 4-el osztható évszám