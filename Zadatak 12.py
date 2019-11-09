# 1.	Tražite neki broj od korisnika. Ukoliko je broj paran napisati “Unijeli ste paran broj!”,
# ukoliko nije poruka je “Vas broj nije paran”. Ako korisnik unese neka slova napisati “Molimo Vas unesite broj!!!”
# Napomena – Koristiti %(moduo). Istražiti sta je to!

Broj = input("Molimo Vas unesite vas broj:")


if Broj.isalpha():
    print("Molimo Vas unesite broj!!!")
elif int(Broj) % 2 == 0:
    print(f"Unijeli ste paran broj!")
else:
    print("Vas Broj nije paran")
