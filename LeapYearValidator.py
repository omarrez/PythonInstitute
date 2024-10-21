"""
This program will validate if any year you input is a Leap Year, Common Year, or not within
the Gregorian Period when it was first defined those year's categories
"""
year = int(input("Enter a year: "))

if (year<1582):
    result = "Not within the Gregorian Calendar Period"
    
else:
    if ((year%4)!=0):
        result = "a Common Year"
    
    elif ((year%100)!=0):
        result = "a Leap Year"
    
    elif ((year%400)!=0):
        result = "a Common Year"
    
    else:
        result = "a Leap Year"

print(f"The year {year} is {result}.")
