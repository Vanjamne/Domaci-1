# 12.	Napisati funkciju koja računa sumu 3 integera. Ukoliko su 2 integera ista, suma će odmah biti jednaka 0.
# Npr. 2 ,3, 2 – 2 I 2 su jednaki..

Int1 = input("Unesite Vas prvi broj:")
Int2 = input("Unesite Vas drugi broj:")
Int3 = input("Unesite Vas treci broj:")
Zbir = int(Int1) + int(Int2) + int(Int3)

def my_function(brojevi):
    if int(Int1) == int(Int2) or int(Int3):
        print("Vas zbir je 0")
    elif int(Int1) + int(Int2) + int(Int3):
        print(f"Vas zbir je {Zbir}")


brojevi = [int(Int1), int(Int2), int(Int3)]
my_function(brojevi)