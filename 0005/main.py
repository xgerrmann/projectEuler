#!/usr/bin/python3

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.

# >> What is the smallest positive number that is evenly divisible
#    by all of the numbers from 1 to 20?

# Only need to check for divisibility by 11 through 20, since e.g. if a number is divisible by
# 18 it will also be divisible by 9. The same holds for 16 and 8, 14 and 7, .. etc.

# The number must be even, since an uneven number divided by an even number leads to a fractional number.

# First attempt unsuccesful: 17907120
# Second attempt succesfull

# 11*12*13*14*15*16*17*18*19*20 is the maximum multiple
#nMax = 670442572800
nMax = 11*12*13*14*15*16*17*18*19*20

# megaNumber = 11x12x13x14x15x16x17x18x19x20 = 670442572800
# if megaNumber /20 / 20 %2==0 then it is evenly divisible by 20, even when the 20 term is removed.
# Solution: try to recursively remove the numbers 11 through 20 from the above number while still adhering to the EVEN divisibility condition.

def recursive_fuction(bigNumber, nMin, nMax):
	# Stop criterion
	if(nMin > nMax):
		return bigNumber
	# Assume lowest number found so far is the one given as input
	minResult = bigNumber
	# Loop over all numbers
	for ii in range(nMin,nMax+1):
		# Check if one can be divided out without affecting EVEN divisibility by all numbers
		if bigNumber % (ii**2) == 0 and int(bigNumber/(ii**2))%2==0:
			# Check if it is still EVENLY divisable by all terms 11 - 20 if the number would have been removed
			flag=False
			for jj in range(nMin,nMax+1):
				if not (int(bigNumber/ii)%jj == 0 and int(bigNumber/ii)%2 == 0):
					flag=True
					break
			if(flag):
				continue
			# Only append when part of lowest answer
			minResult = min(minResult, recursive_fuction(int(bigNumber/ii),nMin,nMax))
	return minResult

print(recursive_fuction(nMax,11,20))

