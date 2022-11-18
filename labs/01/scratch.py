import random
import sys
for k in range(500):
    sys.stdout.write(f"{random.randint(0,10000)}")
    for j in range(8):
        sys.stdout.write(f" {random.randint(0,10000)}")
    sys.stdout.write("\n")
