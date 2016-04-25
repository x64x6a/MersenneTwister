import mt
import os

def prettify_numlist(numbers):
    n = 6
    return '[ ' + '  '.join(map(str,numbers[:n])) + ' ... ' + ' '.join(map(str,numbers[-n:])) + ' ]'

# Create seed
seed = int(os.urandom(4).encode('hex'), 16)
print 'Seed: {seed}\n'.format(seed=seed)

# Start Mersenne Twister generator
server = mt.MTServer(seed=seed)
s = server.start()

# Get 624 numbers from the PRNG generator
numbers = []
for i in range(624):
    numbers.append(s.next())
print 'Random numbers: {numbers}\n'.format(numbers=prettify_numlist(numbers))

raw_input('\n>')
print '='*50,'\n'

##################################################################################################################

print 'Back tracking to the state...\n'
# Calculate current state
state = mt.backtrack(numbers)

print 'Found state:     {n}'.format(n=prettify_numlist(state))
print 'Server\'s state:  {n}'.format(n=prettify_numlist(state))
raw_input('\n>')

# Set current state
rand = mt.MersenneTwister(0)
rand.setstate(state)

N = 1000000
print 'Checking the next {n} numbers for PRNG...\n'.format(n=N)

# Check next 100 numbers
for i in range(N):
    assert s.next() == rand.getrandbits(32)

# It worked!!!
print '\nIt worked!!!\n'
