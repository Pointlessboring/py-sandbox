apple_devices = []
apple_devices.insert(0,"iPhone")
apple_devices.insert(0,"Apple TV")
apple_devices.insert(0,"Apple TV 4k")
apple_devices.append("iPad")
apple_devices.append("Apple watch")
apple_devices.insert(0,"Macmini")
apple_devices.insert(0,"Macbook Pro")
apple_devices.insert(0,"Thunderbolt Display")

print(apple_devices)
print(sorted(apple_devices))

apple_devices.sort()
print(apple_devices)
last_element = apple_devices.pop()
print("\nLast device is: ",last_element)
print(f"\n3rd device is: {apple_devices[2]}")
print(f"\n1st device is: {apple_devices[0]}")

del apple_devices[0]
print(f"\nNew 1st device is: {apple_devices[0]}")