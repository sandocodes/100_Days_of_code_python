def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "True"
            else:
                return "False"
        else:
            return "True"
    else:
        return "False"
  
# TODO: Add more code here 👇
def days_in_month(yr, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    num_days = 0
    
    if is_leap(year) and month == 2 :
        return 29
    else:
        return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Year: ")) # Enter a year
month = int(input("Month in number: ")) # Enter a month
days = days_in_month(year, month)
print(days)