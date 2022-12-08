# Írjon egy Python függvényt, amely a két bekért két természetes szám legnagyobb közös osztóját
# adja meg!

def lnko():

    a = int(input("Adjon meg egy természetes számot: "))
    b = int(input("Adjon meg még egy természetes számot: "))

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

if __name__ == "__main__":
    print(lnko())