
##Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
##projecteuler.net/problem=13

f = open('data_prob13.txt', 'r')
n = 0
for line in f:
	n += int(line)
print n
print str(n)
print str(n)[:10] 
