import random, time

# Set up the constants:
WIDTH = 70  # (!) Try changing this to 10 or 30.
PAUSE_AMOUNT = 0.05  # (!) Try changing this to 0 or 1.0.

gapsize = 20
gapstart = WIDTH//2 - gapsize//2

while True:
    print( ("#" * gapstart)  + (" " * gapsize) + ("#" * (WIDTH - gapsize - gapstart)))
    gapsize  = min(WIDTH//2, max(1, gapsize + random.randint(-1,1)))
    gapstart = min((WIDTH-gapsize-1), max(1, gapstart + random.randint(-1,1)))
    
    time.sleep(PAUSE_AMOUNT)