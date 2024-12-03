rows = int(input("How many rows: "))
columns = int(input("How many Collums: "))
symbols =  input("Enter a Sybmols to use: ")

for i in range (rows):
    for j in range (columns ):
        print(symbols, end="")
print()