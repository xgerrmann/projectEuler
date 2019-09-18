#!/usr/bin/python3

sum = 0
A = 1
B = 2

while B <= 4000000:
	if B % 2 == 0:
		sum += B
	B = A + B
	A = B - A

print(sum)


