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
data = pandas.read_csv("./weather_data.csv")
print(data)
