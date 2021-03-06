from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two dice.

die_1 = Die(8)
die_2 = Die(8)

# Make some random rolls and store them in a list
results = []
number_roll = 1000

for roll_num in range(number_roll):
    result = die_1.roll() * die_2.roll()
    results.append(result)

# Analysze the results

frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1,  max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.

x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling 1D6 x 1D6 {number_roll} times',
                    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6xd6.html')