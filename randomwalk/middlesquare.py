import math

def middle(generator, seed, length):
	#Seed2 will be the middle-square
	seed2 = str(generator)

	padd = float(len(str(generator)) - length)

	# If zero 
	if not (padd % 2):
		seed2 = seed2[:-int(padd / 2)]
		seed2 = seed2[int(padd / 2):]
	else:
		seed2 = seed2[:-int(math.ceil(padd / 2))]
		seed2 = seed2[int(math.floor(padd / 2)):]

	return int(seed2)

def random(seed):
	length = len(str(seed))
	while 1:
		generator = seed ** 2
		seed = middle(generator, seed, length)
		yield int(str(seed).zfill(length))


if __name__ == '__main__':
	#Get a Seed value from the user
	seed = input("Enter a seed: ")
	length = len(str(seed))

	counter = 0

	# Run for 5 rounds
	while counter is not 6:
		#Generate int for Seed2
		generator = seed ** 2

		seed = middle(generator, seed)

		print str(seed).zfill(length)

		counter = counter + 1


