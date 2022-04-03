import random
import json

#Starting variables
rollerList = []
rList = []
output = []
#variable used to convert list to str
rollStr = ""
genStr = ""

#Open json, creates var data with loaded json.
with open("wordlist.json","r") as wl:
    data = json.load(wl)

#While loop to gather input as an integer and stop from entering anything != 1-9.
while True:
    try:
        userInput = int(input("Enter number of words to generate:"))
        if userInput == 0:
            print("Enter a positive number.")
        else:
            userInput >= 1
            break
    except ValueError:
        print("Enter a number.")
        continue
#function for times, and to clear rollerList
def times_to_run(times, f):
    for i in range(times): f()

#Function for roll
def roller():
    #Loop to roll 5 single digit numbers 1-6, creates var roll out of rollerList.
    for i in range(5):
        rollerList.append(str(random.randint(1,6)))
        roll = rollStr.join(rollerList)
        #print(roll)
        #print(rollerList)
        #Checks length, if 5, append to rlist and clear rollerList.
        if len(rollerList) == 5:
            rList.append(roll)
            rollerList.clear()

#Runs function based on userInput
times_to_run(userInput, roller)

#Function that looks for words and appends to output.  Then it runs.
def generate():
    for i in rList:
        for k, v in data.items():
            if k == i:
                output.append(v)
generate()

#Final Product
print(" ".join(output))
