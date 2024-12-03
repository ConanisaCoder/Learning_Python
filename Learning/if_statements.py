# if = Do some Code Only if Some
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too Old to Sign up")
elif age>= 18:
    print("You are you now Singed Up!")
elif age<0:
    print("You haven't been born Yet!")
else:
        print("Your to Young")

response = input("Would you Like Food? (Y/N): ")

if response == "Y":
     print("Have some food!")
     input("Enter to Close:")
else:
     print("No Food for You")
     input("Enter to Close:")

