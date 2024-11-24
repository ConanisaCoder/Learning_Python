func = input("/ = Division, * = Mutilplication, + = Addtion, - = Subtraction: ")
if func == "/":
    num = int(input("What Number do you want to Divide: "))
    start = int(input("What number should the Table Start: "))
    stop = int(input("What number should the Table Stop at: "))
    for i in range(start,stop+1,1):
        total = num/i
        print(f"{num} / {i} = {total}")
elif func == "*":
    num = int(input("What Number do you want to mutiply: "))
    start = int(input("Where do want the Table to start: "))
    stop = int(input("What number should the table end at: "))
    for i in range(start, stop + 1,1):
        total = num * i
        print(f"{num} * {i} = {total}")
elif func == "+":
    num = int(input("What number do want yo add: "))
    start = int(input("Where should the table start: "))
    stop = int(input("Where should the table start: "))
    for i in range(start,stop+1,1):
        total =  num + i
        print(f"{num} + {i} = total")
elif func == "-":
    num = int(input("The number you want to subtract: "))
    start = int(input("Where should the table start: "))
    stop = int(input("Where should the table start: "))
    for i in range(start,stop+1,1):
        total = num - i
        print(f"{num} + {i} = {total}")
input("Enter to Close: ")