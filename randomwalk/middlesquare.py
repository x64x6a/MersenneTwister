import math

def middle(generator, seed):
	#Seed2 will be the middle-square
	seed2 = str(generator)

	padd = float(len(str(generator)) - leng)

	# If zero 
	if not (padd % 2):
		seed2 = seed2[:-int(padd / 2)]
		seed2 = seed2[int(padd / 2):]
	else:
		seed2 = seed2[:-int(math.ceil(padd / 2))]
		seed2 = seed2[int(math.floor(padd / 2)):]

	return int(seed2)

#Get a Seed value from the user
seed = input("Enter a seed: ")
leng = len(str(seed))

counter = 0

# Run for 5 rounds
while counter is not 6:
	#Generate int for Seed2
	generator = seed ** 2

	seed = middle(generator, seed)

	print str(seed).zfill(leng)

	counter = counter + 1


