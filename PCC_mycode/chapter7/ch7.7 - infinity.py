from signal import pause

n = 0

while True:
    n +=1
    prime = True
    for i in range(2,n//2):
        if n % i == 0:
            prime = False
    if prime == True:
        print(f"{n} is a prime number!")
    
            



