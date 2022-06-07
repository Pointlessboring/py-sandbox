players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

print("\n Slices: Copy or references?")

# testing: are slices a view or a copy. They are a copy
slice = players[0:3]
slice[0] = 'john'
print(slice)
print(players)

print("\n")
print("Here are the players on my team:")
for player in players:
    print(player.title())

print("\n")
print("Here are the last 3 players on my team:")
for player in players[-3:]:
    print(player.title())