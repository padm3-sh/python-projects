print("Welcome to this leap year checker")
input_year = input("Enter the year to check: ")

year = int(input_year)

if (year % 4 == 0 and year % 100 != 0):
    print("This is a leap year.")
elif(year % 100 == 0 and year % 400 == 0):
    print("This is a leap year.")
else:
    print("This is not a leap year.")