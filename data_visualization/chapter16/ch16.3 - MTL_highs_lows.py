import csv
from datetime import datetime
import matplotlib.pyplot as plt

# filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/MTL2021.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Sample code to print header information. Later commented out.
    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

# Get high temperature from this file.
    dates, highs, lows = [], [] , []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        
        try: 
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else: 
            high = int(row[5])
            low = int(row[6])
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)

# Format plot.
ax.set_title("Daily high and low temperatures, MTL 2021 May onward", fontsize = 24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.fill_between(dates, highs, lows, facecolor='blue' , alpha=0.1)
plt.show()