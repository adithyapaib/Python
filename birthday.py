#birthday reminder with dictonary
dob = {"Adithya": "26 Oct", "Keshav": "11 Oct", "Ashwin": "13 Jully", "Prajwal": "15 Oct"   } 
print("Welcome to Birthday Reminder")
for key, value in dob.items():
    print("The birthday of " + key + " is on " + value )    
print(dob.get('Adithya', "Default"))

