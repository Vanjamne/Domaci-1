# 14.	Korisnik ima 3 opicije za unos. Ukoliko unese “Evo me opet!” printati “Dobrodosli opet!”.
# Ako unese “123” -- “Zasto opet ti?”, a ako unese “Programiranje” -- “Nema nista bez vjezbe!!!!”.

print("1: Evo me opet")
print("2: 123")
print("3: Programiranje")
odg = (int(input("Unesite jednu od ponudjenih opcija:")))

if odg == 1:
    print("Dobrodosli opet!")
elif odg == 2:
    print("Zasto opet ti?")
else:
    print("Nema nista bez vjezbe!!!!")


# Unos = input("Unesite jednu od opcija")