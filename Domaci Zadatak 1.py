# Ako je cijena računara 400$, štampati koliko treba izdvojiti za plaćanje PDV-a. Potrban format je:
# Cijena računara je 400$. Iznos PDV-a je {pdv}, a cijena računara bez PDV*a je {cijena_računara - pdv}


Cijena = 400
Stopa = 0.21
pdv = Cijena * Stopa

mnozenje = 400 * 0.21
print(mnozenje)
print(int(mnozenje))

# Formatiranje printa/Kao i formatiranje iznosa iy float-a u integer(cijeli broj)

print(f"Cijena racunara je {Cijena}$. Iznos PDVa je {int(pdv)}$, a cijena racunara bez PDVa je {int(Cijena - pdv)}$")

