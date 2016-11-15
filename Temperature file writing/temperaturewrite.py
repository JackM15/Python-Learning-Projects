"""
Here's a rather challenging exercise that integrates functions, loops,
conditionals, and file handling.

In exercise 4, you recursively printed out converted temperature in the command
line.

For this exercise, please consider the same list of Celsius values again as
input:

temperatures=[10,-20,-289,100]

Try to make a script that converts Celsius to Fahrenheit and creates a text
file and stores the converted values inside the text file.
Your text file content should look like this:

50.0
-4.0
212.0

Please don't write any message in the text file when input is lower than
-273.15.
"""

# Create the list of input temperatures
inputTemps = [10, -20, -289, 100]
# Output list (will be appended to the file later)
outputTemps = []

# loop over the temperature inputs and convert them to celcius.
for temp in inputTemps:
    # convert to fahrenheit
    fahrenheit = (temp * 1.8) + 32
    outputTemps.append(fahrenheit)

# create/open a file and append the outputTemps to the file on a new line each.
with open("temperatureOutput.txt", "w") as file:
    # For each item in the outputTemps, add to file on new line
    for temperature in outputTemps:
        if temperature > -273.15:
            file.write(str(temperature) + "\n")
        else:
            print("The temp: " + str(temperature) + "was under -273.15 F.")
            print("Ignoring this one!")
