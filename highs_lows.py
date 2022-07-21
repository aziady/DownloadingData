import csv

#filename = 'sitka_weather_07-2018_simple.csv'
filename = 'sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

