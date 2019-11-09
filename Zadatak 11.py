# 15.	Napisati program koja za unijeti URL (string), izvlači (parsira) samo domain name i vraća ga kao string.
# Pretpostaviti da korisnik unosi ispravan URL.
# Primjeri:
# get_domain("http://github.com/carbonfive/raygun"), izlaz "github.com"
# get_domain("https://google.com"), output = "google.com"
# get_domain("http://github.com/carbonfive/raygun"), output = "github.com"
# get_domain(input = "http://www.zombie-bites.com"), output = "zombie-bites.com"


URL = input("Unesite website:")
URL2 = URL.split('/')[2]

print(f"Unijeti domain name je :{URL2}")