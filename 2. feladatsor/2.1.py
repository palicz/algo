# Az alábbi függvény visszatérési értéke a három megadott szám közül a legkisebb lenne.
# Helyes-e az alábbi megoldás?
# Milyen tesztesetekkel ellenőriznénk a helyességét?

def legkisebb(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2 < n1 and n2 < n3:
        return n2
    else:
        return n3

if __name__ == "__main__":
    print(legkisebb())

# Nem helyes a megoldás
# a,b,c különböző számok, mindegyik formáció, tehát a legkisebb, b legkisebb, c legkisebb
# a,b egyforma és c különböző
# a,c egyforma és b különböző
# b,c egyforma és a különböző
