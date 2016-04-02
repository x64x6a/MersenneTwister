import mt

# Start Mersenne Twister generator
server = mt.MTServer()
s = server.start()

# Get 624 numbers from the PRNG generator
numbers = []
for i in range(624):
    numbers.append(s.next())

# Calculate current state
state = mt.backtrack(numbers)

# Set current state
rand = mt.MersenneTwister(0)
rand.setstate(state)

# Check next 100 numbers
for i in range(100):
    assert s.next() == rand.getrandbits(32)

# It worked!!!
print "It worked!!!"
