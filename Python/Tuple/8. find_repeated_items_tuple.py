tu = ("Ssuray",2,34.08,2,2,True,True)
dup=[]
for i in tu:
    if tu.count(i) > 1 and i not in dup:
        dup.append(i)
print(dup)    
