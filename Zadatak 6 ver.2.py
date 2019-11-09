# 9.	Od korisnika tražiti da unese naziv fajla sa ekstenzijom (Ekstenzija je .exe,.doc I sl.).
# Nakon unosa printajte koja je ekstenzija tog fajla.

Unos = input("Unesite naziv fajla sa ekstenzijom:")
Unos2 = Unos.split(".")

print(f"Vasa ekstenzija je:.{Unos2[-1]}")
