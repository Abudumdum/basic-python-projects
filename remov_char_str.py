# Write a program to remove characters from a string starting from zero up to n and return a new string.
string = input("string: ")
rem = int(input("no charac: "))

new_str = string[rem:]

if rem >= len(string):
    print("PLEASE CHOOSE ANOTHER NUMBER THE NUMBER YOU HAVE CHOSEN IS TOO BIGGER THE THE STRING")
else:
    print(new_str)
