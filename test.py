import os
import random
import mt

seed = int(os.urandom(4).encode('hex'), 16)
r1 = random.Random(seed)
r2 = mt.PyRand(seed)

for i in range(10):
	n1 = r1.getrandbits(32)
	n2 = r2.getrandbits(32)
	print n1==n2,n1,n2
	assert n1 == n2
print

print "Passed"
