import socket
import os
import random

def prettify_numlist(numbers):
    n = 6
    return '[ ' + '  '.join(map(str,numbers[:n])) + ' ... ' + ' '.join(map(str,numbers[-n:])) + ' ]'

HOST = '127.0.0.1'
PORT = 1337


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(10)


print '='*50
while 1:
    conn, addr = s.accept()
    print 'New connection!\n'

    
    # Create seed
    seed = int(os.urandom(4).encode('hex'), 16)
    print 'Seed for Python\'s random: {seed}\n'.format(seed=seed)

    serv = random.Random(seed)
    serv.getrandbits(32)
    serv.getrandbits(32)
    serv.getrandbits(32)

    print '--------------------------------------------------------'
    while 1:
        try:
            # Receive guess
            r = conn.recv(4096)
            if not r:
                break
            r = r.strip('\n')

            # Send next random number
            rand = serv.getrandbits(32)
            conn.send(str(rand)+'\n')
            print "Random number recv:",r
            print "Random number sent:",rand

            # Pythons state's last value is the current nth random number.. so ignore it
            state = serv.getstate()[1][:-1]
            print 'Current state:  {n}\n'.format(n=prettify_numlist(state))
            print '--------------------------------------------------------'
        except:
            break
    print "Connection closed!"
    print '='*50

