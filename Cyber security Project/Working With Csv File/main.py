import csv
import pandas

# with open("weather_data.csv") as file:
#     tempr= []
#     data = csv.reader(file)
#     for all_info in data:
#         tempr.append(all_info[1])
#     print(tempr)
#     res = [eval(i) for i in tempr[1:]]
#     print("Modified list is: ", res)

# a = pandas.read_csv("weather_data.csv")

# temp_list = a["temp"].to_list
# print(temp_list)
# average=0
# for i in temp_list():
#     average+=i
# print(average/len(temp_list()))

# print(a["temp"].max())
# monday = a[a.Day=="Monday"]
# print(monday.condition)
# df = a.assign(Fahrenheit=lambda x: (9/5)*x['temp']+32)
# print(df)

# scratch
# new_file ={
#     "student": ["shubham", "sonali", "sonal"],
#     "score": [20, 10, 30]
# }
# data=pandas.DataFrame(new_file)
# data.to_csv("trial.csv")

a = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
cinammon_color_count = len(a[a["Primary Fur Color"]=="Cinnamon"])
gray_color_count = len(a[a["Primary Fur Color"]=="Gray"])
Black_color_count = len(a[a["Primary Fur Color"]=="Black"])

new_file = {
    "color": ["Cinammon", "gray", "black"],
    "total count": [cinammon_color_count,gray_color_count, Black_color_count]
}
data=pandas.DataFrame(new_file)
data.to_csv("primary_fur_color.csv")
