#40.Extract only numbers
s = "abc123xyz456"
print("".join([i for i in s if i.isdigit()]))