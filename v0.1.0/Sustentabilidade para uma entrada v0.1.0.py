#                   R E G I S T E R      D A T A 

#==========================================================================#
#==========================================================================#

# Import libraries
from datetime import datetime 

#==========================================================================#

# DATE

while True:
    # Get date in the format dd/mm/yyyy
    date_str = input("\n Insert date in the format dd/mm/yyyy: ")

    # Initializing format 
    format = "%d/%m/%Y"

    # Validating the format 
    result = True

    # Checking if value is in the format or not
    try:
        result = bool(datetime.strptime(date_str, format))
    except ValueError:
        result = False

    # Printing validation of the result
    if (result==True):
        print("\n Valid date")
        break #Goes to next part
    else:
        print("\n Invalid date")

#==========================================================================#

# WATER CONSUMPTION

# Get amount of water consumed

while True:
    water_consumption = float(input("\n\n Insert amount of water consumed today approximately in liters: "))

    # Checking if value is valid
    if (water_consumption >= 0):
        print("\n Valid amount")
        break #Goes to next part
    else:
        print("\n Invalid amount")

#==========================================================================#

# POWER CONSUMED

while True:
    power_consumption = float(input("\n\n Insert amount of power consumed in kWh: "))

    # Checking if value is valid 
    if (power_consumption >=0):
        print("\n Valid amount")
        break #Goes to next part
    else:
        print("\n Invalid amount")


#==========================================================================#

# GENERATION OF NON-RECYCLABLE TRASH

while True:
    trash_total_kg = float(input("\n\n Insert amount of non-recyclable trash produced today in kg: "))

    # Checking if value is valid 
    if (trash_total_kg >=0):
        print("\n Valid amount")
        break #Goes to next part
    else:
        print("\n Invalid amount")

#==========================================================================#

# PORCENTAGE OF RECYCLABLE TRASH

while True:
    percentage_trash = float(input("\n\n Insert percentage of recyclable trash: "))

    # Checking if value is valid 
    if (percentage_trash >=0 and percentage_trash<=100):
        print("\n Valid percentage")
        break #Goes to next part
    else:
        print("\n Invalid percentage")



#==========================================================================#

# MEANS OF TRANSPORTATION USED

print("\n\n MEANS OF TRANSPORTATION:")
print("\n 1 - Public transportation (bus, subway, train)")
print("\n 2 - Bicycle")
print("\n 3 - Walking")
print("\n 4 - Car (fossil fuel)")
print("\n 5 - Electric car")
print("\n 6 - Shared ride")

while True:
    transportation = int(input("\n\n Insert 1, 2, 3, 4, 5 or 6 for the transportation used today: "))

       # Checking if value is valid 
    if (transportation >= 1 and transportation <= 6):
        print("\n Valid option")
        break #Goes to next part
    else:
        print("\n Invalid option")


#==========================================================================#
#==========================================================================#


# RANKING OF EACH PARAMETER


print("\n\n =================================================================")
print("\n\n SUSTENTABILITY")

#==========================================================================#

# WATER CONSUMPTION

if (water_consumption < 150):
    print("\n Water consumption: High sustentability")
elif (water_consumption >= 150 and water_consumption <= 200):
    print("\n Water consumption: Moderate sustentability")
else: 
    print("\n Water consumption: Low sustentability")

#==========================================================================#

# POWER CONSUMPTION

if (power_consumption < 5):
    print("\n Power consumption: High sustentability")
elif (power_consumption >= 5 and power_consumption <= 10):
    print("\n Power consumption: Moderate sustentability")
else:
    print("\n Power consumption: Low sustentability")

#==========================================================================#

# GENERATION RECYCLABLE TRASH

if (percentage_trash > 50):
    print("\n Generation of recyclable trash: High sustentability")
elif (percentage_trash <= 50 and percentage_trash >= 20):
    print("\n Generation of recyclable trash: Moderate sustentability")
else:
    print("\n Generation of recyclable: Low sustentability")

#==========================================================================#

# MEANS OF TRANSPORTATION USED

if (transportation == 2 or transportation == 3 or transportation == 5):
    print("\n Means of transportation: High sustentability")
elif (transportation == 1 or transportation == 6):
    print("\n Means of transportation: Moderate sustentability")
else:
    print("\n Means of transportation: Low sustentability")

print("\n\n\t\t *END OF THE PROGRAM* \n\n")