import sys
import random

n = int(sys.argv[1])
m = int(sys.argv[2])
print n, m
for i in range(n):
    for j in range(m):
        print random.randrange(-32768, 32767), 
    print
    
