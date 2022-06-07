sandwiches_orders = ['tuna', 'egg', 'brie', 'ham', 'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

print(sandwiches_orders)

print("We are all out of pastrami.\n")
while 'pastrami' in sandwiches_orders:
    sandwiches_orders.remove('pastrami')

for sandwich in sandwiches_orders:
    print(f"I made your {sandwich}.")
    finished_sandwiches.append(sandwich)

print(finished_sandwiches)