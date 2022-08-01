digits = input("> ")

reverse = ""
for x in digits:
    reverse = x + reverse

print(reverse, end="")
