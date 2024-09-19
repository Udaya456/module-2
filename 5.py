#ask to enter Medival unites

talents= float(input("enter the talets:"))
pounds=float(input("enter the pounds:"))
lots=float(input("enter the lots:"))

kilograms=((talents*20+pounds)*32+lots)*0.0133
grams=1000.0*(kilograms-int(kilograms))

print(f"The weight in modern units;")
