import string
from datetime import datetime #importing the date module to calculate age

def ID():#calling function to validate ID

    while True:

        id = input("Please enter your ID number")
        if len(id) == 13 and string.digits == True:
            print("Correct")
        else:
            return id
#id = ID() # calling this in the main 

def age(dateofbirth):
    year = dateofbirth[:2]
    month = dateofbirth[2:4]
    day = dateofbirth[4:6]
    return day+"/"+month+"/"+year


def calculate_Age(dateofbirth):

    dateofbirth = datetime. date(age)
    end_date = datetime.date(31, 12, 2021)
    time_difference = end_date - dateofbirth
    age_one = time_difference
    return age_one

def gender(): # make this function just like all functions take an argument to execute the code.
    if int(gender) in range(0000, 4999):
        return"female"
    elif int(gender) in range(5000, 9999):
        return"male"
    else:
        return"Error"

def citizenship(): # make this function just like all functions take an argument to execute the code.
    if int(id[10]) == 0:
        return"South African Citizen"
    elif int(id[10]) ==1:
        return"Permanent resident"

    if len(id) == 13 and string.digits == True:

        print(age)
        print(calculate_Age)
        print(gender)
        print(citizenship)
    else:
        print("invalid ID number")
        print("Wrong number of characters")
        print("empty string")
        
        exit()

#Adding a main at the bottom of your file 
if __name__ == "__main__":
    print("hello Gugu")
    id = ID()
    print(id)
    print("goood bye Gugu")
