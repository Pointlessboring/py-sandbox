from multiprocessing.dummy import current_process


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1