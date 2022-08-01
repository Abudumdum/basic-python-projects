# Write a program to find how many times a substring appears in the given string
string = "abudu is the best at being abudu"
sub = input("substring:  ")

if sub not in string:
    print(sub + " is not in the string")
else:
    print("The substring appears " + str(string.count(sub)) + " times")
