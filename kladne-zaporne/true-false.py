# text čísla

cislo = float(input("Zadej číslo: "))
absolutni_hodnota = cislo
if cislo>0:
    print("Zadané číslo je kladné")
else:
    if cislo<0:
        print("Zadané číslo je záporné")
        absolutni_hodnota = -cislo
    else:
        print("Nula")

print(f"Absolutní hodnota: {cislo} je {absolutni_hodnota}")
