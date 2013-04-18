## If we list all the natural numbers below 10 that are
## multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of
## these multiples is 23.

## Find the sum of all the multiples of 3 or 5 below 1000.



def get_multiples(n, m1, m2):
	L = []
	for i in range(1, n):
		if i%m1 == 0:
			L.append(i)
		else:
			if i%m2 == 0:
				L.append(i)
	return L
	
	
	
def get_sum():
	L = get_multiples(1000, 3, 5)
	sum = 0
	for i in L:
		sum += i		
	return sum
	

print (get_sum())
