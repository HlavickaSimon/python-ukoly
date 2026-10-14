pocet = int(input("Zadejte počet lidí: "))
cena_vstupenky = 500

typ_slevy = "beze slevy"

cena_celkova = cena_vstupenky * pocet

if pocet>=4:
    cena_celkova = cena_vstupenky * pocet * 0.75
    typ_slevy = "skupinová sleva"
else:
    vek = float(input("Zadejte věk: "))
    if vek>=65:
        cena_celkova = cena_vstupenky * pocet * 0.8
        typ_slevy = "senioři"
    elif vek<=26:
        student = input("student [ano/ne] ")
        if student =="ano":
            cena_celkova = cena_vstupenky * pocet * 0.7
            typ_slevy = "studenti"
print("Cena 1 osoba", cena_celkova / pocet)
print("Cena 1 celkem", cena_celkova)
print(typ_slevy)