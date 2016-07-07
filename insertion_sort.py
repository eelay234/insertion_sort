import random
import math
import time

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
	i = j - 1
	while i >= 0 and A[i] > key:
	    A[i+1] = A[i]
	    i -= 1
	A[i+1] = key

a = []
for i in range(1, 101):
    a.append(int(random.random()*10001))

begin = time.time()
insertion_sort(a)
end = time.time()

print a
print "It took %.2f seconds" % (end - begin)
