#41 Words starting with capital letters
s = "Python Is A Great Language"
for word in s.split():
    if word[0].isupper():
        print(word)