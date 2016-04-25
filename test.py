import os
import random
import mt

seed = int(os.urandom(4).encode('hex'), 16)
r1 = random.Random(seed)
r2 = mt.PyRand(seed)


# Test PRNG
for i in range(10):
    assert r1.getrandbits(32) == r2.getrandbits(32)


# Test backtrack to state
numbers1 = []
numbers2 = []
for i in range(624):
    n1 = r1.getrandbits(32)
    n2 = r2.getrandbits(32)
    numbers1.append(n1)
    numbers2.append(n2)

state1 = mt.backtrack(numbers1)
state2 = mt.backtrack(numbers2)
assert state1 == state2

c1 = random.Random(0)
c1.setstate((3, tuple(state1 + [624]), None))
c2 = mt.PyRand(0)
c2.setstate(state2)

for i in range(2000):
    assert r1.getrandbits(32) == c1.getrandbits(32)
    assert r2.getrandbits(32) == c2.getrandbits(32)
    

print

print "Passed"
