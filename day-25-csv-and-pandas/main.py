# # with open("weather_data.csv") as weather_data_file:
# #     data = weather_data_file.readlines()
# #     print(data)
# #     data = []
# #     print(weather_data_file.readlines())
# #     for _ in weather_data_file.readlines():
# #         new_data = _.strip()
# #         data.append(new_data)
# # print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     print(data)
# #     for row in data:
# #         print(row)
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# # Python way of calculating average:
# temp_list = data["temp"]
# average_temp = sum(temp_list) / len(temp_list)
# print("Python traditional way:", average_temp)
#
# # Pandas way of calculating average:
# print("Pandas average:", data["temp"].mean())
#
# # Pandas find the maximum value:
# print("Pandas max value:", data["temp"].max())
#
# # Get Data in Columns:
# print(data["condition"])
# print(data.condition)
#
# # Get Data in Row:
# # Get entire row of data where the day is equal to Monday:
# # Step 1. Get hold of entire data table data[]
# # Step 2. Inside that data table, get hold of the column data[data.day]
# # Step 3. Inside that column, check for the row where value is equal to Monday:
# print(data[data.day == "Thursday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp_f = (int(monday.temp) * 9/5) + 32
# print("Monday temperature in Fahrenheit", monday_temp_f)
#
# # Create DataFrame from scratch:
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data_pandas = pandas.DataFrame(data_dict)
# print(data_pandas)
#
# # Convert DataFrame to a CSV file:
# data_pandas.to_csv("new_data.csv")

import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# grey_fur = 0
# red_fur = 0
# black_fur = 0
#
# for fur in squirrel_data["Primary Fur Color"]:
#     if fur == "Gray":
#         grey_fur += 1
#     elif fur == "Cinnamon":
#         red_fur += 1
#     elif fur == "Black":
#         black_fur += 1
#
# print("Grey:", grey_fur, "Red:", red_fur, "Black:", black_fur)

grey_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_fur = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

squirrel_count = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_fur, red_fur, black_fur]
}

df = pandas.DataFrame(squirrel_count)
print(df)
df.to_csv("squirrel_count.csv")
