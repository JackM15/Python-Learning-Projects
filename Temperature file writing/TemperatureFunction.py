# little program to convert celcius to Fahrenheit
# import time to allow sleeping to look like its calculating
import time

# functions
def convertAndWrite(temperature):
    # code to convert and write Here
    print("Converting temperature to Fahrenheit...")
    time.sleep(2)
    print("Converted!")
    print("\n\n")
    time.sleep(1)
    return int(temperature) * 1.8 + 32

def saveToFile(resultToSave):
    with open("temperatureLog.txt", "a+") as file:
        print("Writing to the temperature Log.")
        time.sleep(2)
        file.write(resultToSave)
        print("File written!")


# infinite loop so it keeps asking if the user wants to convert more
while True:
    temperature = float(input("What temperature would you like converted?\n"))
    converted = convertAndWrite(temperature)
    print("****************************************************************\n")
    print(str(temperature) + " is equal to " + str(converted) + " Fahrenheit\n")
    print("****************************************************************\n")
    time.sleep(3)
    # Ask if they want to save it to a file:
    doesUserWantToSave = input("Do you want to save this to the log file? y/n\n")
    if doesUserWantToSave == "y":
        time.sleep(2)
        resultToSave = "\n{} is equal to {} Fahrenheit.".format(str(temperature),str(converted))
        saveToFile(resultToSave)
    else:
        time.sleep(2)
        print("No problem!")

    # ask if they want to try again?
    tryAgain = input("Would you like to convert another?\n")
    time.sleep(1)
    if tryAgain == "No" or tryAgain == "no":
        print("Exiting Program!")
        time.sleep(3)
        break
    else:
        print("Ok, let's try again!")
