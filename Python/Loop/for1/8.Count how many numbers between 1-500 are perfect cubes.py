#8.Count how many numbers between 1-500 are perfect cubes
count = 0
for i in range(1,501):
    if round(i**(1/3))**3 == i:
        count += 1
print("Perfect cubes count:", count)
