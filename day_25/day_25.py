# Day 25 - Working with CSV files and Pandas library
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)


# Pandas Library
# data = pandas.read_csv("./weather_data.csv")
# print(data)

# Pandas DataFrames and Series: Working with Rows and Columns
# data_dict = data.to_dict()
# print(data_dict)

# Data Series
# temp = data["temp"] #to get the data in the temp column. Can also be done using data.temp
# average_temp = temp.mean()
# max_temp = temp.max()
# min_temp = temp.min()
# print(f"Temperatures: {temp}")
# print(f"Average temp: {round(average_temp, 2)}")
# print(f"Max temp: {round(max_temp, 2)}")
# print(f"Min temp: {round(min_temp, 2)}")

# Selecting specific row data
# monday = data[data.day == "Monday"]
# print(monday)

# # Eg. Get the row where the temperature is at its maximum
# maximum_temp = data[data.temp == data.temp.max()]
# # print(maximum_temp)

# # Eg: Convert Monday's temp value to Frenheit
# monday = data[data.day == "Monday"]
# mond_temp = monday.temp[0]
# mond_temp_f = mond_temp * 9/5 + 32
# print(mond_temp_f)



# Creating DataFrames from scratch
data_dict = {
    "students": ["Amy", "James", "Shakea"],
    "grades": [75, 85, 99]
}

data = pandas.DataFrame(data_dict)
print(data)

# # Eg: Get the row of the student with the highest grades
# # 1. Get the highest grade
# highest_grade = data["grades"].max()
# # 2. Row with the highest grade (Name and Grade)
# highest_grade_row = data[data.grades == highest_grade]
# print(highest_grade_row)


# Converting DataFrames back to CSV files
data.to_csv("new_data.csv") #to_csv() takes the path where you want to save the file as an argument.