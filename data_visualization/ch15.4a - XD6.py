from random import randint
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create XD6 dice.

num_dice = randint(1,5)
dices = []
for n in range(num_dice+1):
    dices.append(Die(6))


# Make some random rolls and store them in a list
results = []
number_roll = 1000

for roll_num in range(number_roll):
    result = 0
    for die_num in range(1,num_dice+1):
        result += dices[die_num].roll()
    results.append(result)

# Analysze the results

frequencies = []
max_result = sum([dice.num_sides for dice in dices])

for value in range(2,  max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling {die_num}D6 {number_roll} times',
                    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')