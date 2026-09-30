# *****************************
# Kalkulačka spropitného
# 30. 9. 2026
# *****************************

print("KALKULAČKA SPROPITNÉHO")       # titulní text

celkova_cena = float(input("Zadej celkovou cenu: "))
spropitne = int(input("Zadej spropitné: "))
pocet_lidi = int(input("Zadej počet lidí: "))

# celkova_cena = celkova_cena + celkova_cena * spropitne / 100 #
celkova_cena += celkova_cena * spropitne / 100
print(celkova_cena)

uhrada_za_jednoho = round(celkova_cena / pocet_lidi, 2)
print(uhrada_za_jednoho)

uhrada_za_jednoho = round(celkova_cena / pocet_lidi + 0.5)
print(f"Celková cena: {celkova_cena} dělená {pocet_lidi} je po zaokrouhléní {uhrada_za_jednoho}")

