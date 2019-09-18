#!/usr/bin/python3
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# >> Find the largest palindrome made from the product of two 3-digit numbers.

#999999
#998899
#997799
#ETC
# For each such number / candidate, check if it is the product of two 3-digit integers.

# So check for 100 to 999

# Since there are (it seems) less candidates than possibilities of possibilities of
# multiplying 2 3-digit integers I will start with the candidates.

# First attempt failed: 100001
# Second attempt succesfull.

import math

left_side_list = list(range(100,1000))

for left_side in reversed(left_side_list):
	# Fast string reverse: https://www.journaldev.com/23647/python-reverse-string
	palindrome = int(str(left_side) + str(left_side)[::-1])
	flag = False
	for ii in range(100,math.floor(palindrome**0.5)+1):
		if(palindrome%ii==0):
			factor = int(palindrome/ii)
			if len(str(factor)) == 3:
				flag = True
				break
	if(flag):
		break
print(palindrome)
