from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6

die = Die()

# Make some random rolls and store them in a list
results = []
number_roll = 1000
for roll_num in range(number_roll):
    result = die.roll()
    results.append(result)

# Analysze the results

frequencies = []

for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling one D{die.num_sides} {number_roll} times',
                    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')