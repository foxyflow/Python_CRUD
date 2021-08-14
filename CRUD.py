#After pressing play, please place curser in a newline in the console: Then follow the prompts: Step 3 is always: Enjoy.
# Luke Fox 1177897
# This project uses CRUD to update a csv for teenage activity entries.
# The console application acts as an address-book for teenagers to try be more organised.
import csv
import re

myList = []  # Global variable to collect information by the end-user.

print("\nWelcome to your activities diary ... Here are your activities so far:\n")
# Read file:
csv_file = open('activitiesCSVv4.csv', newline='')
for line in csv_file:
    print(line)

## Search
activitySpecific = input(
    "\nWhich activity would you like to look-up?\n ").title()  # title case for all Caps or lowercase.
with open('activitiesCSVv4.csv', 'r', newline='') as file:
    activities = csv.reader(file)
    for row in activities:
        if row[1] == activitySpecific:
            print(row)  # Read the remaining data.

##C (Create)
##Create file and declare attibutes:
with open('activitiesCSVv4.csv', 'a+', newline='') as newCSV:  # When run: csv-file created.
    myNewFile = csv.writer(newCSV)
    myNewFile.writerow(["Id", "Activity", "Description", "Activity-level"])  # Headers created

    numberOfActivities = int(input("Please enter the number of activities you would like: "))
    for i in range(numberOfActivities):
        new_activity_ID = input("Activity " + str(i + 1) + ". Please enter a new activity ID: ")
        new_activity = input("Activity " + str(i + 1) + ". Please enter a new type of activity: ")
        new_activity_description = input("Activity " + str(i + 1) + ". Please enter a new activity description: ")
        new_activity_level = input("Activity " + str(i + 1) + ". Please enter a new activity level, EG beginner: ")
        myNewFile.writerow([new_activity_ID, new_activity, new_activity_description, new_activity_level])
        ##Input initialised from user (with values):

##R (Read)
##Reading: the now re-created file:
with open('activitiesCSVv4.csv', 'r', newline='') as file:
    myFile = csv.reader(file)
    for row in myFile:
        myList.append(row)
print(myList)  ##for 2D array.
# print(myList) #showing 2D array created.


## Displaying the file content to the user and print row number to make selection easy.
print("Please see details of the csv file below: ")
for i in range(len(myList)):
    print("Row " + str(i) + " : " + str(myList[i]))  ##Displaying the CSV file to user via console.

##U (Update)
##Inserting in the middle of the file:
## Which row would you like to change?
editRow = int(input("\nPlease select row to change. Enter 1 to " + str(len(myList) - 1) + " :"))
print("Please enter new details for each of the following: ")

##Allow user to add changes and append changes to the list
for i in range(len(myList[0])):
    newDetails = input("Please enter new data for " + str(myList[0][i] + " :"))
    myList[editRow][i] = newDetails

##Show the user the new list and confirm changes:
print("\n Please see the details of the new file below:")
for i in range(len(myList)):
    print("Row " + str(i) + " :" + str(myList[i]))

##If changes are made, write the new file
changeCSV = input("\nPlease confirm changes to the CSV file? y/n ").title()

if changeCSV == "y":
    with open('activitiesCSVv4.csv', 'w+', newline='') as file:
        myFile = csv.writer(file)
        for i in range(len(myList)):
            myFile.writerow(myList[i])

##Delete -- activity:
lines = list()
delete_row = input("Please enter an activity name to be delete its row.")
with open('activitiesCSVv4.csv', 'r', newline='') as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        lines.append(row)
        for field in row:
            if field == delete_row.title():
                lines.remove(row)
with open('activitiesCSVv4.csv', 'w', newline='') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)
print(lines)
print("That row has now been deleted\n")
print("Here are your activities\n")


txt = str(myList)
deleteSpace = re.sub("\s", "", txt)
print(deleteSpace)

##Re-display contents: After final search:
print("\nHere are your updated activities:\n")
csv_file = open('activitiesCSVv4.csv', newline='')
for line in csv_file:
    print(line)


def space():
    print("\n\n\n")


def goodbye_message():
    print("Enjoy your activities! And, have a nice rest of the day")


space()
goodbye_message()
exit()
