import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [(x*x*x) for x in x_values]

# Set plot style
plt.style.use('seaborn')

# Generate the plot we will be using
# fig is the collection of plot
# ax is a single plot.

fig, ax = plt.subplots()

# the scatter method generate a plot graph
ax.scatter(x_values,y_values, c=y_values, cmap = plt.cm.Blues, s=10)

ax.set_title("Chart of Cubes", fontsize = 24)
ax.set_xlabel("Value", fontsize = 18)
ax.set_ylabel("Cube of Value", fontsize = 18)
ax.tick_params(axis='both', which='major')


# Fixed axis label misformatting - from stackoverflow.com
# the user warning is a bug in the library
ax.set_yticklabels(['{:,}'.format(int(y)) for y in ax.get_yticks().tolist()])
plt.show()