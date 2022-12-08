# a.) Írassuk ki az első 25 prímszámot!
# b.) Írassuk ki az összes prímszámot 200-ig!
# c.) Írassuk ki a legnagyobb, 500-nál kisebb prímszámot!
# d.) Írassuk ki a legkisebb, 1000-nél nagyobb prímszámot!
# e.) Hogyan oldanánk meg a fenti feladatokat az 2. feladatban módosított prímteszt
# függvény felhasználásával?

# a.)
counter = 0
for n in range(2, 100):
    for i in range(2, n):
        if (n % i) == 0:
            break
    else:
        counter += 1
        print(str(counter) + ".", n)

    if counter == 25:
        break

# b.)
for szam in range(1, 200):
   if szam > 1:
       for i in range(2, szam):
           if (szam % i) == 0:
               break
       else:
           print(szam)

# c.)
for szam in range(1, 500):
   if szam > 1:
       for i in range(2, szam):
           if (szam % i) == 0:
               break
       else:
           raktar = szam
print(raktar)

# d.)
for szam in range(1000, 2000):
   if szam > 1:
       for i in range(2, szam):
           if (szam % i) == 0:
               break
       else:
           raktar = szam
           break
print(raktar)