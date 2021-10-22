# [ Nyveon ]
# Tarea 2
# VACAS ENTERA BRIGIDA
# B - Aggressive cows 



# Function for checking if a given minimum distance is feasible
def checker(array, checking, cows):
	# True means it is possible
	# In other words, that this or higher is the answers
	# Otherwise, it is lower
	
	distance = 0
	cows -= 1
	for index in range(1, len(array)):

		distance += array[index] - array[index-1] # travelling cows
		
		if distance >= checking: # PLACE COW
			cows -= 1
			distance = 0
	
	return not cows <= 0


# Solution
# Test cases
t = int(input())
for i in range(t):
	
	# Input
	n, c = [int(x) for x in input().split()]	
	stalls = []
	for j in range(n):
		stalls.append(int(input()))
	stalls.sort()
	
	# Binary search on the answer
	
	left = 0
	right = 1000000000
	
	while (left < right):
		mid = (right+left)//2
		
		if checker(stalls, mid, c):
			right = mid
		else:
			left = mid + 1
	
	print(right - 1)
		
		
	