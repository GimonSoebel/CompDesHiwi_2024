Height = float(5.5)
Width = float(10.3)
Length = float(10.3) 

Area_m2 = Width * Length
print (Area_m2)

Volume_m3 = Width * Length * Height
print (Volume_m3)

print (f"{Area_m2:.2f}")
print (f"{Volume_m3:.2f}")

Area_mm2 = Area_m2 * 1000000
Volume_mm3 = Volume_m3 * 1000000000

print (f"{Area_mm2:.2f}")
print (f"{Volume_mm3:.2f}")

if Height > Width and Height > Length:
    print("\nThe Height of your room greater both its Width and Length.")
elif Width > Height and Width > Length:
    print("\nThe Width of your room greater both its Height and Length.")
elif Length > Width and Length > Height:
    print("\nThe Length of your room greater both its Width and Height.")
else:
    print("\nTwo or more dimensions are equal and dominate the room size.")