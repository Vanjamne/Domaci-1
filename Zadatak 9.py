# 13.	Korisnik unosi temperaturu u stepenima Celizijusovih, a vi vracate tu temperaturu u Ferhajtima.
# Ferhajti su jednaki = (celsius * 1.8) + 32. Odaditi I obrnuto.

Temperatura = input("Unesite temperaturu u Celzijus-ima:")

def Stanje(temp):
    print(f"Spoljasnja temperatura je: {Temperatura} farnehajta.")

celsius_to_fahr = [(int(Temperatura) * 1.8) + 32]

Stanje(celsius_to_fahr)


Temp = input("Unesite temperaturu u Fahrenheit-ima:")

def Funkcija(Temp):
    print(f"Spoljasnja temperatura je {Temp} celzijusa.")

fahr_to_celsius = [(int(Temp) - 32) * (5/9)]

Funkcija(fahr_to_celsius)