import random
import hashlib
import sys

if len(sys.argv) != 2:
	print("Useage: python",sys.argv[0],'<hash>') # find Birthday_date_hash in console
	exit()

y = 2024
while y > 0:
	for m in range(1,13):
		for d in range(1,32):
			bd_str = str(d).zfill(2)+'/'+str(m).zfill(2)+'/'+str(y).zfill(4)
			h = hashlib.new('sha256')
			h.update(bd_str.encode())
			if sys.argv[1] == h.hexdigest():
				print(bd_str) # post 
				exit()
	y -= 1
