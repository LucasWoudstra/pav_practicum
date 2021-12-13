height = 24
#makes sure input is between 0 and 23
while height < 0 or height > 23:
    height = int(input("Height: "))

#loops till height
for i in range(1, height + 1):

    #prints the correct amount of spaces
    for space in range(0, height - 1):
        print("", end=" ")
    height -= 1

    #prints the correct amount of #
    for charac in range(0, i + 1):
        print("#", end="")
        
    print("")



