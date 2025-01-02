days_alive = 0
years_t_f = input("Have been alive for over a year (Y/N): ").lower()
if years_t_f == "y":
    year_alive = int(input("How many years have you been alive: "))
    day_Y = year_alive * 365
    days_alive += day_Y 
months_t_f = input("Past that year have been alive for a month (Y/N): ").lower()
if months_t_f == "y":  
    month_1 = int(input("How many 31-day months did you have: "))
    month_2 = int(input("How many 30-day months did you have: "))
    month_3 = int(input("Non-Leap Year Febs: "))
    month_4 = int(input("Lepa Years Febs: "))
    days_alive += month_1 * 31
    days_alive += month_2 * 30 
    days_alive += month_3 * 28
    days_alive += month_4 * 29
days_alive += int(input("How many more days where you alive: "))    
print(f"You where alive for {days_alive} days")