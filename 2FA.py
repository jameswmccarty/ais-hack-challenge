import random
import sys

if len(sys.argv) != 2:
	print("Useage: python",sys.argv[0],'<seed>')
	exit()

random.seed(int(sys.argv[1])) # put seed on command line (e.g. 1705425465)

for _ in range(6):
	print(random.randint(0,9),end='')
print()
