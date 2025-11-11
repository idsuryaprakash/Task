#14.Count vowels in a string
s = "Education"
vowels = "aeiouAEIOU"
count = sum(1 for i in s if i in vowels)
print(count)