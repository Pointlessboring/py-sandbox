
squares = [value**2 for value in range(1,11)]

print("The first three items in the list are:")
print(squares[:3])

print("The three items from the middle of the list are:")
mid_point = len(squares)//2
print(squares[mid_point-2:mid_point+1])

print("The last three items in the list are:")
print(squares[-3:])

