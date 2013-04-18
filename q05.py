## 2520 is the smallest number that can be
## divided by each of the numbers from 1 to 10
## without any remainder.
## What is the smallest positive number that is
## evenly divisible by all of the numbers from 1 to 20?

i = 0
sum = 1
while sum != 0:
	i += 1
	sum = 0
	for j in range(1, 21):
		sum += i%j
		if sum != 0:
			break
print i
