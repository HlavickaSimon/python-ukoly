
cas = int(input("Zadejte hodinu (0-23): "))
if cas < 0:
    print("Hodina nemůže být záporná.")
elif cas >= 24:
    print("Zadávejte platné hodiny.")
elif cas < 5:
    print("Dobrou noc")
elif cas < 9:
    print("Dobré ráno")
elif cas < 12:
    print("Dobré dopoledne")
elif cas == 12:
    print("Dobré poledne")
elif cas < 18:
    print("Dobré odpoledne")
else:
    print("Dobrý večer")