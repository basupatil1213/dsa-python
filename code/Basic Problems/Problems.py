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

print("~*~*~*~*~ Problem 1 ~*~*~*~*~")

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
output = linear_search(items, target)
print(f"Expected Output: 3\nActual Output: {output}")

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
output = linear_search(items, target)
print(f"Expected Output: -1\nActual Output: {output}")

print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")

'''
Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

bouncy and flouncy both increment the value of the variable tigger by 1.
trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.

def final_value_after_operations(operations):
	pass
Example Usage:

operations = ["trouncy", "flouncy", "flouncy"]
final_value_after_operations(operations)

operations = ["bouncy", "bouncy", "flouncy"]
final_value_after_operations(operations)
Example Output:

2
4
'''

print("~*~*~*~*~ Problem 2 ~*~*~*~*~")

def final_value_after_operations(operations):
    tigger = 1
    for operation in operations:
        if operation == "bouncy" or operation == "flouncy":
            tigger += 1
        else:
            tigger -= 1
    return tigger

operations = ["trouncy", "flouncy", "flouncy"]
output = final_value_after_operations(operations)
print(f"Expected Output: 2\nActual Output: {output}")

operations = ["bouncy", "bouncy", "flouncy"]
output = final_value_after_operations(operations)
print(f"Expected Output: 4\nActual Output: {output}")

print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")

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
'''

print("~*~*~*~*~ Problem 3 ~*~*~*~*~")

def tiggerfy(word):
    word = word.lower()
    word = word.replace("t", "")
    word = word.replace("i", "")
    word = word.replace("gg", "")
    word = word.replace("er", "")
    return word

word = "Trigger"
output = tiggerfy(word)
print(f"Expected Output: r\nActual Output: {output}")

word = "eggplant"
output = tiggerfy(word)
print(f"Expected Output: eplan\nActual Output: {output}")

word = "Chor"
output = tiggerfy(word)
print(f"Expected Output: Choir\nActual Output: {output}")

print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")

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

print("~*~*~*~*~ Problem 4 ~*~*~*~*~")

def non_decreasing(nums):
    allowance = 1
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            allowance -= 1
            if allowance < 0:
                return False
    return True

nums = [4, 2, 3]
output = non_decreasing(nums)
print(f"Expected Output: True\nActual Output: {output}")

nums = [4, 2, 1]
output = non_decreasing(nums)
print(f"Expected Output: False\nActual Output: {output}")

print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")


