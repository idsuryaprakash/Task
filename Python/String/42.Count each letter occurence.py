#42.Count each letter occurence
s = "banana"
for ch in set(s):
    print(ch, "=", s.count(ch))