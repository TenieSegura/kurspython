import random

gracz = 300
comp = random.randint(1,100)



for i in range(6):
    prev = gracz
    gracz = int(input("Podaj liczbe: "))
    if gracz == comp:
        print("Wygrales :D")
        break
    elif abs(gracz - comp) < abs(prev - comp):
        print("cipelo")
    else:
        print("zimno")

if gracz != comp:
    print("Przegrales :(")
    print("Wybrana liczba to ", comp)



