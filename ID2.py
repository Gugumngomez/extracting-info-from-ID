from datetime import datetime #importing the date module to calculate age


def ID():#calling function to validate ID
    id = input("Please enter your ID number:")
    while True:
        if len(id) == 13 and id.isdecimal():
            return id
        id = input("Please make sure your ID number is valid:")
#validate the ID        

def getBirthDay(id):
    year = id[:2]
    month = id[2:4]
    day = id[4:6]


    try:
        birth_date = datetime.strptime(f"{year}{month}{day}", "%y%m%d")
        print("Your birthday:", birth_date.strftime("%Y-%m-%d"))
    except ValueError:
        print("Invalid birthdate")

def getGender(id):
    try:
        if int(id[7:10]) in range(0000, 4999):
            return "female"
        elif int(id[7:10]) in range(5000, 9999):
            return "male"
        else:
            return "Invalid Gender"
    except (ValueError, IndexError):
        return "Invalid Gender"

def workMagic(id):

    if int(id[10]) == 0:
        print("SA Citizen")
    elif int(id[10]) == 1:
        print("Permanent resident")

    else:
        print("Invalid ID")
        print("Undefined")
        print("Wrong characters")

    
        

if __name__ == "__main__":
    theID = ID()
    getBirthDay(theID)
    print(getGender(theID))
    workMagic(theID)
