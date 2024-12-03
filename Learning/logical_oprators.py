#logical operators (and,or,not) = used to check if two or more conditions are true or false
temp =int(input("what is the temperature outside: "))
# and allows you combine logical statments both vaules have to met
# or combines but only one vaule has to met
# not surrond one or more conditnal statements and flip it so true = false
if not(temp>= 0 and temp<=30):
    print("Tempture is Bad Today")
    print("Do not go outside")
elif not(temp < 0 or  temp > 30):
    print("The Tempture is Good Today")
    print("Go Outside")
