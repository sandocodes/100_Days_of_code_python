import pandas


data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

grey_squirrels_count = len(data[data["PrimaryFurColor"] == "Gray"])
cinnamon_squirrels_count = len(data[data["PrimaryFurColor"] == "Cinnamon"])
black_squirrels_count = len(data[data["PrimaryFurColor"] == "Black"])

print(f"Grey Squirrels: {grey_squirrels_count}")
print(f"Cinnamon Squirrels: {cinnamon_squirrels_count}")
print(f"Black Squirrels: {black_squirrels_count}")


squirrels_count = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(squirrels_count)

df.to_csv("squirrels_count.csv")
