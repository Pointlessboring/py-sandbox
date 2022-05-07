big_list = []
my_sum = 0
for n in range (1,1000001):
    big_list.append(n)
    my_sum = my_sum + n
print(f"Min: {min(big_list)}, Max:{max(big_list)}, Sum: {my_sum}")
