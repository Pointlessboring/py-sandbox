import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Sample code to print header information. Later commented out.
    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

# Get high temperature from this file.
    dates, si_highs = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        si_highs.append(high)
        

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
# Get high temperature from this file.
    dv_highs = []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try: 
            high = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else: 
            high = int(row[4])
            dv_highs.append(high)
        
# plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, dv_highs, c='red', alpha=0.5)
ax.plot(dates, si_highs, c='blue', alpha=0.5)

# Format plot.
ax.set_title("Daily high temperatures for Death valley and Sitka, 2018", fontsize = 20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.fill_between(dates, dv_highs, si_highs, facecolor='blue' , alpha=0.1)
plt.show()