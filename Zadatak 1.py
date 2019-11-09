# 4.Ako imate string “Prvi Domaći” kako da izdvojite slovo ć iz stringa?
# Kako biste razbili string na dvije riječi [“Prvi”, “Domaći”]?
# Kako biste našli indeks slova D, a kako biste uklonili slovo D?


word = "Prvi Domaci"

print(len(word))
print(word[-2])
print(word.split(" "))
print(word[5])
print(word.replace( "D"," " ))