import csv

from matplotlib import pyplot as plt

# Get high temperatures from file.
#filename = 'sitka_weather_07-2018_simple.csv'
filename = 'sitka_weather_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    #for index, column_header in enumerate(header_row):
     #   print(index, column_header)
    highs = []
    for row in reader:
        highs.append(row[8])

    #print(highs)
    # Plot data.
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(highs, c='red')

    # Format plot.
    plt.title("Daily high temperatures, 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Temperature (F)", fontsize=16)
    #plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
