nombre = int(input("Combien de croissants voulez-vous ? "))

if nombre <= 5:
    prix = nombre * 3
else:
    prix = nombre * 2

print("Le prix total est de", prix, "euros.")