
previous_number = 0
for x in range(1, 11):

    number = previous_number + x

    print("Current Number is " + str(x) +
          " previous Number " + str(previous_number) + " Sum: " + str(number))
    previous_number = x
