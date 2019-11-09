# 9.	Od korisnika tražiti da unese naziv fajla sa ekstenzijom (Ekstenzija je .exe,.doc I sl.).
# Nakon unosa printajte koja je ekstenzija tog fajla.

Unos = input("Unesite naziv fajla sa ekstenzijom:")

if Unos.endswith(".rar"):
    print(format("Vasa ekstenzija je:" + Unos[-4:]))
elif Unos.endswith(".zip"):
    print(format("Vasa ekstenzija je:" + Unos[-4:]))
elif Unos.endswith(".msi"):
    print(format("Vasa ekstenzija je:" + Unos[-4:]))
elif Unos.endswith(".ppt"):
    print(format("Vasa ekstenzija je:" + Unos[-4:]))
elif Unos.endswith(".xls"):
    print(format("Vasa ekstenzija je:" + Unos[-4:]))
elif Unos.endswith(".doc"):
    print(format("Vasa ekstenzija je:" + Unos[-4:]))
elif Unos.endswith(".iso"):
    print(format("Vasa ekstenzija je:" + Unos[-4:]))
elif Unos.endswith(".py"):
    print(format("Vasa ekstenzija je:" + Unos[-3:]))
elif Unos.endswith(".html"):
    print(format("Vasa ekstenzija je" + Unos[-5:]))
elif Unos.endswith(".torrent"):
    print(format("Vasa ekstenzija je:" + Unos[-8:]))
else:
    print(format("Ekstenzija nije podrzana, molimo Vas unesite podrzanu ekstenziju!"))
