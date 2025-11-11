#11.Remove digits from a string
s = "Python123is4fun"
result = "".join([i for i in s if not i.isdigit()])
print(result)