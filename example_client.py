import socket
import mt

def prettify_numlist(numbers):
    n = 6
    return '[ ' + '  '.join(map(str,numbers[:n])) + ' ... ' + ' '.join(map(str,numbers[-n:])) + ' ]'

HOST = '127.0.0.1'
PORT = 1337

s = socket.create_connection((HOST,PORT))

print "Connected!\n"
raw_input('>')
print

numbers = []
for i in range(624):
    s.send('0\n')
    n = s.recv(4096).strip('\n')
    numbers.append(int(n))
print '624 random numbers: {numbers}\n'.format(numbers=prettify_numlist(numbers))

raw_input('>')

print '\nBack tracking to the state...\n'
state = mt.backtrack(numbers)

print 'Found state:     {n}'.format(n=prettify_numlist(state))

raw_input('>')
print 'Setting the state using basic Mersenne Twister...'

# Set current state
rand = mt.MersenneTwister(0)
rand.setstate(state)


N = 100
print 'Checking the next {n} numbers for PRNG...\n\n'.format(n=N)

# Check next 100 numbers
for i in range(N):
    rand_c = rand.getrandbits(32)
    s.send(str(rand_c)+'\n')
    
    rand_s = s.recv(4096).strip('\n')
    rand_s = int(rand_s)

    assert rand_s == rand_c

print 'IT WORKS!!!'