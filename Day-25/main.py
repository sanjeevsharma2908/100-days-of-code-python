# with open('weather_data.csv', 'r') as file:
#     data = file.readlines()
#     print(data)

# import csv
# with open('weather_data.csv', 'r') as file:
#     data = csv.reader(file)
#     tempratures = []
#     for row in data:
#         if row[1] != "temp":
#             tempratures.append(int(row[1]))
#     print(tempratures)

import pandas
#data = pandas.read_csv('weather_data.csv')
#print(data)
# data_dict = data.to_dict()
# print(data_dict)
#
# data_list = data['temp'].to_list()
# avg_tempreature  = sum(data_list) / len(data_list)
# print(round(avg_tempreature))
# print(max(data_list))
# print(data['temp'].max())
# print(data['temp'].idxmax())
# print(data['temp'].min())
# print(data['condition'])
# print(data.condition)

#Get data in row
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == 'Monday']
# print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# data_dict = {
#     "students":["Amy","James","Sanjeev"],
#     "scores":[76,56,65]
# }
# framed_data = pandas.DataFrame(data_dict)
# print(framed_data)
# framed_data.to_csv('new_data.csv')

data  = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color":["Gray", "Cinnamon", "Black"],
    "Count":[gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')






