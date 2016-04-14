import math

def middle(generator, length):
    #Seed will be the middle-square
    seed = str(generator)

    padd = float(len(str(generator)) - length)

    # If zero 
    if not (padd % 2):
        seed = seed[:-int(padd / 2)]
        seed = seed[int(padd / 2):]
    else:
        seed = seed[:-int(math.ceil(padd / 2))]
        seed = seed[int(math.floor(padd / 2)):]

    return int(seed)

def random(seed):
    length = len(str(seed))
    while 1:
        generator = seed ** 2
        seed = middle(generator, length)
        yield int(seed)

if __name__ == '__main__':
    #Get a Seed value from the user
    seed = input("Enter a seed: ")
    length = len(str(seed))
    print length
    counter = 0

    # Run for 5 rounds
    while counter is not 6:
        #Generate int for Seed2
        generator = seed ** 2

        seed = middle(generator, length)

        print str(seed).zfill(length)

        counter = counter + 1


