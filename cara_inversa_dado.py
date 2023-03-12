# programa para identificar la cara inversa en un dado

print("----------------------------------")
print("---------CARA_INVERSA-------------")
print("----------------------------------")

#input

c = int(input("ingrese una cara del dado: "))

#processing

Ci = (7 - c)

if 1 <= c <=6:
    print("la cara inversa de" , c, "es" , Ci, )

else:
    print("no es la cara de un dado")