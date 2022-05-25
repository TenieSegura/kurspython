#Komputer losuje liczbę z zakresu od 1 do 100.
#Użytkownik podaje swój traf.
#Komuter odpowiada ciepło zimno, ale nie więcej niż 6 razy.
#Jeśli użytkownik zgadnie wygrywa gracz.
#Jeśli po 6 próbach użytkownik nie zgadnie - wygrywa komputer.


import random

gracz = 300
comp = random.randint(1, 100)

for i in range(6):
    prev = gracz
    gracz = int(input("Odgadnij liczbe"))
    if comp == gracz:
        print("Goraco!")
        break
    elif abs(gracz - comp) < abs(prev - comp):
        print("cieplo")
    else:
        print("zimno")

if comp != gracz:
    print("Nie zgadles :(")
    print("Wulosowana liczba to ", comp)



