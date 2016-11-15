# Mega list of destiny
listofstuff = []
# append 20000 numbers to the list.
for number in range(1, 20001):
    listofstuff.append(number)

# Write the list to the file on seperate lines
# Open the file which also creates the file with write permissions
numbersFile = open("numbers.txt", "w")

# Loop to write each number to the file.
for number in listofstuff:
    numbersFile.write(str(number) + "\n")

# close the file.
print("Added " + str(len(listofstuff)) + " strings to: numbers.txt")
numbersFile.close()
