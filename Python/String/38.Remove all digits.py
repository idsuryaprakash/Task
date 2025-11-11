#38.Remove all digits
s = "abc123xyz"
print("".join([i for i in s if not i.isdigit()]))