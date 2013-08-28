## A palindromic number reads the same both ways.
## The largest palindrome madie from the product
## of two 2-digit numbers is 9009 = 91 99.
## Find the largest palindrome made from
## the product of two 3-digit numbers.

def palindromic_num():
	li = []
	for i in range(999, 99, -1):
		for j in range(999, 99, -1):
			p = str(i*j)
			l = len(p)
			if len(p)%2:
				p1 = p[0:l/2]
				p2 = p[l/2+1:l]
			else:
				p1 = p[0:l/2]
				p2 = p[l/2:l]
			if p1 == p2[::-1]:
				li.append((i*j, i, j))
	m = max([i[0] for i in li])
	for x in li:
		if x[0] == m:
			print x
		
palindromic_num()
