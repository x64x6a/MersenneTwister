import socket
import mt

def prettify_numlist(numbers):
    n = 3
    return '[ ' + '  '.join(map(str,numbers[:n])) + ' ... ' + ' '.join(map(str,numbers[-n:])) + ' ]'

HOST = '127.0.0.1'
PORT = 1337

s = socket.create_connection((HOST,PORT))

print "==================================================\n"
print "Connected!\n"
raw_input('>')
print '\n'

numbers = []
print '--------------------------------------------------------'
for i in range(624):
    send = '0'
    print "<--    Sent:",send
    s.send(send+'\n')
    n = s.recv(4096).strip('\n')
    print "--> Received:",n
    numbers.append(int(n))
    print '\n\n\n'
    print '--------------------------------------------------------'
#print '624 random numbers: {numbers}\n'.format(numbers=prettify_numlist(numbers))

raw_input('>')

print '\nBack tracking random numbers to state table...\n'
state = mt.backtrack(numbers)

print 'Found state:     {n}\n'.format(n=prettify_numlist(state))

raw_input('>')
print 'Setting the state using basic Mersenne Twister...'

# Set current state
rand = mt.MersenneTwister(0)
rand.setstate(state)


N = 10000
print 'Checking the next {n} numbers for PRNG...\n\n'.format(n=N)

# Check next 100 numbers
for i in range(N):
    rand_c = rand.getrandbits(32)
    send = str(rand_c)
    print "<--    Sent:",send
    s.send(send+'\n')
    
    rand_s = s.recv(4096).strip('\n')
    rand_s = int(rand_s)
    print "--> Received:",rand_s

    print
    print rand_s == rand_c
    assert rand_s == rand_c
    print '\n'
    print '--------------------------------------------------------'


win = 'Successfully predicted {n} random numbers!'.format(n=N)
print '\n{win}'.format(win=win)
