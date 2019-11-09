# 10.	Napisati program koji od korisnika trazi neki broj (integer!) I printati rezultat koji je jednak n+nn+nnn
# Primjer:
# 5+55+555 = 615

n = input("Unesite vas broj:")
nn = n + n
nnn = nn+n
# nint = int(n)


if n.isdigit():
    print(f"Rezultat je:", int(n) + int(nn) + int(nnn))
elif n.isalpha():
    print("Molimo Vas unesite broj!")







