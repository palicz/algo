# Írjon egy Python függvényt, amely a bekér három szám közül a legnagyobb/legkisebb értéket adja
# meg!

def legnagyobb(a,b,c):

    return max(a,b,c)

def legkisebb(a,b,c):

    return min(a,b,c)

def valasztas():

    n1 = input("Adja meg az első számot: ")
    n2 = input("Adja meg a második számot: ")
    n3 = input("Adja meg a harmadik számot: ")

    valasztas = int(input(f"--- Válasz, melyik függvény fusson le: ---\n[1] Legnagyobb szám / [2] Legkisebb szám\n"))

    if valasztas == 1:
        print(legnagyobb(n1, n2, n3))
    elif valasztas == 2:
        print(legkisebb(n1, n2, n3))
    else:
        print("Nem választottad egyik lehetőséget sem.")

if __name__ == "__main__":
    valasztas()