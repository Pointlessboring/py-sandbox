import csv
from datetime import datetime
import matplotlib.pyplot as plt

# filename = 'data/sitka_weather_07-2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'
# filename = 'data/MTL2021.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Sample code to print header information. Later commented out.
    headers = []      
    for index, column_header in enumerate(header_row):
        headers.append(column_header)
        

# Get high temperature from this file.
    dates, highs, lows = [], [], []

    max_pos = headers.index("TMAX")
    min_pos = headers.index("TMIN")
    station_pos = headers.index("NAME")
    station_name = ""
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        
        try: 
            high = int(row[max_pos])
            low = int(row[min_pos])
            station_name = row[station_pos]
        except ValueError:
            print(f"Missing data for {current_date}")
        else: 
            high = int(row[max_pos])
            low = int(row[min_pos])
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)

# Format plot.
ax.set_title(f"Daily high and low temperatures, {station_name}", fontsize = 20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.fill_between(dates, highs, lows, facecolor='blue' , alpha=0.1)
plt.show()