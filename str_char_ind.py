# Write a program to accept a string from the user and display characters that are present at an even index number.
string = input("> ")
print(" The original string is " + string)
print("Printing only even index characters ")
for x in string:
    if string.index(x) % 2 == 0:
        print(x)
# change the 0 in ln 6 to 1 for odd numbers
