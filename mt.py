from os import urandom

def _int32(n):
    return n & 0xffffffff

class MersenneTwister(object):
    """
    Implements a basic Mersenne Twister PRNG
    """
    def __init__(self, seed):
        self.index = 624
        self.mt = [seed] + [0] * 623
        for i in range(1, 624):
            self.mt[i] = _int32(1812433253 * (self.mt[i - 1] ^ self.mt[i - 1] >> 30) + i)

    def setstate(self, state):
        self.mt = state
    def getstate(self):
        return self.mt

    def random(self):
        """
        Returns floating point number from 0.00 to 1.00
        Mimics Python's random.random()
        """
        a = self.random32() >> 5
        b = self.random32() >> 6
        return float((a * 67108864.0 + b) * (1.0 / 9007199254740992.0))

    def getrandbits(self, n):
        """
        Alias to random 32, only accepts 32 bits
        """
        assert n == 32
        return self.random32()        

    def random32(self):
        """
        Returns the next 32 bit random number
        """
        mt = self.mt
        if self.index >= 624:
            k = 0
            while k < 624-397:
                y = (mt[k] & 0x80000000) | (mt[k+1] & 0x7fffffff)
                n = 0x9908b0df if y % 2 else 0
                mt[k] = mt[k+397] ^ (y >> 1) ^ n
                k += 1
            while k < 624-1:
                y = (mt[k] & 0x80000000) | (mt[k+1] & 0x7fffffff)
                n = 0x9908b0df if y % 2 else 0
                mt[k] = mt[k+(397-624)] ^ (y >> 1) ^ n
                k += 1
            y = (mt[624-1] & 0x80000000)|(mt[0] & 0x7fffffff)
            n = 0x9908b0df if y % 2 else 0
            mt[624-1] = mt[397-1] ^ (y >> 1) ^ n
            self.index = 0
        y = mt[self.index];
        self.index += 1
        y ^= (y >> 11)
        y ^= (y << 7) & 0x9d2c5680
        y ^= (y << 15) & 0xefc60000
        y ^= (y >> 18)
        return y

class PyRand(MersenneTwister):
    """
    Emulates Python's random, seed is required
    """
    def __init__(self, seed):
        key = []
        super(PyRand, self).__init__(19650218)
        while seed:
            key.append(seed & 0xffffffff)
            seed = seed >> 32
        if len(key) == 0:
            key = [0]
        
        mt = self.mt
        i = 1
        j = 0
        m = max(624, len(key))
        for k in xrange(m, 0, -1):
            mt[i] = _int32((mt[i] ^ ((mt[i-1] ^ (mt[i-1] >> 30)) * 1664525)) + key[j] + j)
            i += 1
            if i >= 624:
                mt[0] = mt[623]
                i = 1
            j = (j+1) % len(key)

        for k in xrange(623, 0, -1):
            mt[i] = _int32((mt[i] ^ ((mt[i-1] ^ (mt[i-1] >> 30)) * 1566083941)) - i)
            i += 1
            if i >= 624:
                mt[0] = mt[624-1]
                i = 1
        mt[0] = 0x80000000

class MTServer(object):
    def __init__(self, seed, rand=PyRand):
        self.seed = seed
        self.rand = rand
        self.state = []
    def start(self):
        """
        Returns a generator of PRNG numbers
        """
        r = self.rand(self.seed)
        self.state = r.mt
        while 1:
            yield r.getrandbits(32)


def unBitshiftRightXor(value, shift):
    i = 0;
    result = 0;
    while (i * shift < 32):
        partMask = (((0xffffffff << (32 - shift)) & 0xffffffff) >> (shift * i))
        part = value & partMask
        value ^= part >> shift
        result |= part
        i+=1
    return result

def unBitshiftLeftXor(value, shift, mask):
    i = 0
    result = 0
    while (i * shift < 32):
        partMask = ((0xffffffff >> (32 - shift))) << (shift * i)
        part = value & partMask
        value ^= (part << shift) & mask
        result |= part
        i+=1
    return result

def backtrack(numbers):
    """
    Returns the current state of the MT PRNG based on list of 624 numbers
    """
    assert len(numbers) == 624
    state = []
    for n in numbers:
        n = unBitshiftRightXor(n, 18)
        n = unBitshiftLeftXor(n, 15, 4022730752)
        n = unBitshiftLeftXor(n, 7, 2636928640)
        n = unBitshiftRightXor(n, 11)
        state.append(n)
    return state
