############### Functions with Outputs ###############
# def format_name(f_name, l_name): 
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title() 
    
#     return f"{formated_f_name} {formated_l_name}"

# first = input("First name: ")
# last = input("Last name: ")

# formated_string = format_name(first, last)

# print(formated_string)



def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
  
# TODO: Add more code here 👇
def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_leap(year):
        if month == 2:
            return 29
        else:
            return 28
    else:
        return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Year: ")) # Enter a year
month = int(input("Month in number: ")) # Enter a month
days = days_in_month(year, month)
print(days)
