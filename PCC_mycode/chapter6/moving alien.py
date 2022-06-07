alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

print(f"Original position is: ({alien_0['x_position']}, {alien_0['y_position']})")
# Dove the alien to the right
# Determine how far to move the alien based on its current speed

if alien_0['speed'] == "slow":
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else: 
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position is: ({alien_0['x_position']}, {alien_0['y_position']})")

