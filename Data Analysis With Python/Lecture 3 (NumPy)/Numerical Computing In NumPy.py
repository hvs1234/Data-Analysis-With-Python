'''
Q- Given some climate data for the region, we can now predict what the yield of apples in the region might look like. Sample data are:-

Region      Temp(F)     Rainfall(mm)       Humidity(%)
Kanto       73          67                  43
Johto       91          88                  64
Hoenn       87          134                 58
Sinnoh      102         43                  37
Unova       69          96                  70

To begin, we can define some variables to record the climate data for a region.
'''

kanto_temp = 73
kanto_rainfall = 67
kanto_humidity = 43

w1,w2,w3 = 0.3,0.2,0.5

kanto_yield_apples = kanto_temp * w1 + kanto_rainfall * w2 + kanto_humidity * w3
print(f"Expected yield of apples in kanto region is: {kanto_yield_apples}")

kanto = [73,67,43]
johto = [91,88,64]
hoenn = [87,134,58]
sinnoh = [102,43,37]
unova = [69,96,70]

weights = [w1,w2,w3]

def crop_yields(region,weights):
    result = 0
    for x,w in zip(region,weights):
        result += x * w
    return result

print(f"{crop_yields(kanto,weights)}")
print(f"{crop_yields(johto,weights)}")
print(f"{crop_yields(hoenn,weights)}")
print(f"{crop_yields(sinnoh,weights)}")
print(f"{crop_yields(unova,weights)}")