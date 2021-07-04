import string
from datetime import datetime #importing the date module to calculate age

def ID():#calling function to validate ID

    while True:

        id = input("Please enter your ID number:")
        return id

def main():
    id = ID()
    if len(id) == 13 and string.digits == True:
        print("Welcome")
    
    year = id[:2]
    month = id[2:4]
    day = id[4:6]
    print("Your birthday: " + year + "/" + month + "/" + day)
    

    if int(id[7:10]) in range(0000, 4999):
        print("female")
    elif int(id[7:10]) in range(5000, 9999):
        print("male")

    if int(id[10]) == 0:
        print("SA Citizen")
    elif int(id[10]) == 1:
        print("Permanent resident")

    else:
        print("Invalid ID")
        print("Undefined")
        print("Wrong characters")

    
        

if __name__ == "__main__":
    main()
