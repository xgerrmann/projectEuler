#!/usr/bin/python3
# Good tips for generating primes:
# http://code.activestate.com/recipes/366178-a-fast-prime-number-list-generator/

# Attempt 1 unsuccesfull: 775121
# Attempt 2 succesfull: #NO spoiler
import math

list_primes = [2]

n = 0
number = 600851475143

# 1. Generate list of possible primes
for ii in range(3,math.floor(number**0.5)+1,2):
	isPrime = True
	threshold = ii**0.5
	for prime in list_primes:
		if ii%prime==0:
			isPrime = False
			break
		if prime > threshold:
			break
	if(isPrime):
		list_primes.append(ii)
		print(ii)

# 2. Check which of the primes is the answer
for prime in reversed(list_primes):
	if(number%prime==0):
		print(prime)
		break
