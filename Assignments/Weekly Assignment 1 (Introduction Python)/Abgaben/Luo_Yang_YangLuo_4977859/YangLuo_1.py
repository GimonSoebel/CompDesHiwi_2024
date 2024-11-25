print(f"{"****This is a method that calculate the area and the volume of a room."}{"\n"}{"****Please insert the following parameters: (/m)"}")

wid = int(input("    The width of the room (/m): "))
len = int(input("    The length of the room (/m): "))
hei = int(input("    The height of the room (/m): "))

dic = {}
dic["width"] = wid
dic["length"] = len
dic["height"] = hei

if wid!=0 and len!=0 and hei!=0:

    all_l = [wid,len,hei]

    res = sorted(dic.items(), key=lambda x:x[1])

    area_m = round(wid*len,1)
    area_mm = round(area_m*1e4,1)

    vol_m = round(area_m*hei,1)
    vol_mm = round(vol_m*1e6,1)

    print(f"****The results are shown below:")
    print(f"{"    The volume is "}{vol_m}{" in m³"}{" and "}{vol_mm}{" in mm³"}")
    print(f"{"    The area is "}{area_m}{" in m²"}{" and "}{area_mm}{" in mm²"}")

    print(f"{"    The inputs are sorted as (/m):" }")
    for i in range(3):
        res_i = res[i]
        print(f"        {res_i[0]}:{res_i[1]}")

else:
    print("The inputs are not completed.")