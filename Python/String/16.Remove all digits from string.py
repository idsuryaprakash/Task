#16.Remove all digits from string
s = "abc123xyz"
print("".join([i for i in s if not i.isdigit()]))