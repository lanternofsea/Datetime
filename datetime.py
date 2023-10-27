
# code that determines if a guest is of drinking age
import datetime 
import math

def drinking_age(year, month, day):
    """takes inputed DOB and determines if guest can drink"""

    tday = datetime.date.today() # identifies today's date
    bday = datetime.date(year, month, day) # input of DOB

    difference = tday - bday # finds the difference between today and DOB in days
    int_difference = int(str(difference.days)) # turns the difference of days into a string, then an integer

    true_age = math.floor(int_difference / 365 ) #calculates age and rounds to lowest integer (difference in days/365 days=age in years)

    if true_age > 21: # conditional determining if they are 21 or not
        print(f"You are {true_age}, you are legally allowed to drink.")

    elif true_age < 21:
        days_left = round(21 - true_age) # finds out how many years are left till guest is 21
        print (f"Sorry, you are {true_age}. You need to be 21. Come back after {days_left} years.")

    else:
        print("Happy birthday! You are legally allowed to drink.")

# Testing the function
drinking_age(1999, 3, 23)
drinking_age(2006, 8, 19)
drinking_age(2002, 4, 12)
