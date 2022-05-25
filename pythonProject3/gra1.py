import random
secret_num = 5


while(True):
    gracz = int(input("podaj liczne od 0-20"))
    if gracz == secret_num:
        print("Wygrales")
        break
    else:
        print("Zgaduj dalej")

