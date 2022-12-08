# a.) Írassuk ki a Fibonacci sorozat első 20 elemét!

def fibonacci1():

    n1 = 0
    n2 = 1

    szamlalo = 0
    vege = 25

    print("Fibonacci sorozat első 25 eleme:")
    while szamlalo < vege:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        szamlalo += 1

def fibonacci2():

    n1 = 0
    n2 = 1


    print("Fibonacci sorozat elemei 1000-ig:")
    while n1 < 1000:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth

if __name__ == "__main__":
    fibonacci1()
    fibonacci2()
