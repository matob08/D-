from random import*

spodok = int(input("Zadaj mi dolnú hranicu intervalu (napr. 1): "))
vrch = int(input("Zadaj mi vrchnú hranicu intervalu (napr. 10): "))

odpocet1 = randrange (spodok,vrch+1)

odpoved = input("Myslíš na číslo " + str(odpocet1) + "? ")

if odpoved == "áno":
    input("Čaves!")
    
elif odpoved == "nie":
        if vrch + 1 == odpocet1 or odpocet1 > 1:
            odpoved2 = input("Je tvoje číslo väčšie alebo menšie ako " + str(odpocet1) + "? ")
            if vrch + 1 == odpocet1:
                input ("Tvoje číslo je " + odpocet1 + ", čaves!")
        if odpoved2 == "menšie":
            odpocet2 = randrange (spodok, vrch)
            odpoved3 = input("Je tvoje číslo " + str(odpocet2) + "? ")
            if odpoved3 == "áno":
                input ("Čaves!")
            if odpoved3 == "nie":
                odpoved4 = input ("Je tvoje Číslo väčšie alebo menšie ako " + str(odpocet2) + "? ")
                if odpoved4 == "väčšie":
                    odpocet5 = randrange (odpocet2, vrch + 1)
                    odpoved5 = input ("Je tvoje číslo " + odpocet5 + "? ")
                if odpoved4 == "menšie":
                    odpocet5 = randrange (spodok, odpocet2 + 1)
                    odpoved5 = input ("Je tvoje čislo " + "? ")
            if odpoved5 == "áno":
                input ("čaves")