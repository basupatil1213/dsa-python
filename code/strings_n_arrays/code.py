
'''
Problem 1: Hunny Hunt
Write a function linear_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. The function should return the first index of target in items, and -1 if target is not in the lst. Do not use any built-in functions.

def linear_search(lst, target):
	pass
Example Usage:

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
linear_search(items, target)

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
linear_search(items, target)
Example Output:

3
-1
'''

def linear_search(lst, target):
	idx = -1
	for i in range(len(lst)):
		if lst[i] == target:
			idx = i
			break
	return idx

print(f' Expected: 3, \n Output: {linear_search(['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn'], 'hunny')}')
print(f' Expected: -1, \n Output: {linear_search(['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn'], 'red balloon')}')

'''
Problem 3: T-I-Double Guh-Er II
T-I-Double Guh-Er: That spells Tigger! Write a function tiggerfy() that accepts a string word and returns a new string that removes any substrings t, i, gg, and er from word. The function should be case insensitive.

def tiggerfy(word):
	pass
Example Usage:

word = "Trigger"
tiggerfy(word)

word = "eggplant"
tiggerfy(word)

word = "Choir"
tiggerfy(word)
Example Output:

"r"
"eplan"
"Chor"

"gtig"
'''

def tiggerfy(word):
	
	

	checkers = set(['t','i','gg','er'])
	print(checkers)

	r = 0
	res = []
	while r < len(word):
		print(f'idx: {r}')
		if  r+1 < len(word) and word[r:r+2].lower() in checkers:
			print(f'2st: {word[r:r+2]}')
			r += 2
		elif word[r].lower() in checkers:
			print(f'1st: {word[r]}')
			r += 1
		else:
			print(f'3st: {word[r]}')
			res.append(word[r])
			r += 1

	return "".join(res)

print(tiggerfy("Trigger"))
print(tiggerfy("eggplant"))
print(tiggerfy("Choir"))
print(tiggerfy("gtig"))

'''
Problem 4: Non-decreasing Array
Given an array nums with n integers, write a function non_decreasing() that checks if nums could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

def non_decreasing(nums):
	pass
Example Usage:

nums = [4, 2, 3]
non_decreasing(nums)

nums = [4, 2, 1]
non_decreasing(nums)
Example Output:

True
False
'''

def non_decreasing(nums):
	availability = 1

	for i in range(1, len(nums)):
		if nums[i] < nums[i-1]:
			availability -= 1
			if availability < 0:
				return False

			if i == 1 or nums[i] >= nums[i-2]:
				nums[i-1] = nums[i]
			else:
				nums[i] = nums[i-1]
	
	return True

print(non_decreasing([4,2,3]))
print(non_decreasing([4,2,1]))


'''
Problem 5: Missing Clues
Christopher Robin set up a scavenger hunt for Pooh, but it's a blustery day and several hidden clues have blown away. Write a function find_missing_clues() to help Christopher Robin figure out which clues he needs to remake. The function accepts two integers lower and upper and a unique integer array clues. All elements in clues are within the inclusive range [lower, upper].

A clue x is considered missing if x is in the range [lower, upper] and x is not in clues.

Return the shortest sorted list of ranges that exactly covers all the missing numbers. That is, no element of clues is included in any of the ranges, and each missing number is covered by one of the ranges.

def find_missing_clues(clues, lower, upper):
   pass
Example Usage:

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99
find_missing_clues(clues, lower, upper)

clues = [-1]
lower = -1
upper = -1
find_missing_clues(clues, lower, upper)
Example Output:

[[2, 2], [4, 49], [51, 74], [76, 99]]
[]
'''

def find_missing_clues(clues, lower, upper):
	res = []
	for i in range(len(clues)):
		if clues[i] > lower:
			res.append([lower, clues[i]-1])
		lower = clues[i] + 1
	
	if upper > lower:
		res.append([lower, upper])
	
	return res

clues = [0, 1, 3, 50, 75]
lower = 0
upper = 99

print(find_missing_clues(clues, lower, upper))
		   
		
	   
