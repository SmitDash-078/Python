# First import the calendar module
import calendar

# Ask of month and year
yy = int(input("Enter a year : "))
mm1 = int(input("Enter starting month : "))
mm2 = int(input("Enter ending month : "))

for mm3 in range(mm1,mm2):
    if ((mm1>13)or(mm2>13)):
        print("Please input a valid month!!!")
        break
    else:
        # Display the calendar
        print(calendar.month(yy, mm3))
