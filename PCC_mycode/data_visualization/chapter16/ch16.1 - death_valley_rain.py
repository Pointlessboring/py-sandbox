import csv
from datetime import datetime
import matplotlib.pyplot as plt


filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Sample code to print header information. Later commented out.
    # for index, column_header in enumerate(header_row):
    #   print(index, column_header)

# Get high temperature from this file.
    dates, inches = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        inch = float(row[3])
        
        dates.append(current_date)
        inches.append(inch)

# plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, inches, c='blue', alpha=0.5)

# Format plot.
ax.set_title("Daily precipitation, 2018", fontsize = 24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Rain/snow (inches)', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.show()