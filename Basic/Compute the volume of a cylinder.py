radius,length=str(input()).split(',')
radius=float(radius)
length=float(length)
area_of_base = radius * radius * 3.14
volume = area_of_base * length 
print(round(volume,2))