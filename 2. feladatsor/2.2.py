# Az alábbi függvényt arra szeretnénk használni, hogy eldöntsük, hogy a megadott pozitív
# egész szám prím-e.
# Helyes-e az alábbi megoldás?
# Milyen tesztesetekkel ellenőriznénk a helyességét?

def primteszt(n):

    for i in range(2, n):
        if n % i == 0:
            return "nem prim"
    return "prim"

if __name__ == "__main__":
    print(primteszt(1))

# Helyes
# Teszt elemek: prímszám, nem prímszám, 1, 0