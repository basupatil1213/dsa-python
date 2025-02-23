'''
Problem 1: Arrange Guest Arrival Order
You are organizing a prestigious event, and you must arrange the order in which guests arrive based on their status. The sequence is dictated by a 0-indexed string arrival_pattern of length n, consisting of the characters 'I' meaning the next guest should have a higher status than the previous one, and 'D' meaning the next guest should have a lower status than the previous one.

You need to create a 0-indexed string guest_order of length n + 1 that satisfies the following conditions:

guest_order consists of the digits '1' to '9', where each digit represents the guest's status and is used at most once.
If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
Return the lexicographically smallest possible string guest_order that meets the conditions.

def arrange_guest_arrival_order(arrival_pattern):
  pass
Example Usage:

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  
Example Output:

123549876
4321
'''

def is_valid_format(posts):
    d = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    
    stack = []

    for post in posts:
        if post in d:
            if not stack or stack[-1] != d[post]:
                return False
            stack.pop()
        else:
            stack.append(post)


'''
PProblem 1: Arrange Guest Arrival Order
You are organizing a prestigious event, and you must arrange the order in which guests arrive based on their status. The sequence is dictated by a 0-indexed string arrival_pattern of length n, consisting of the characters 'I' meaning the next guest should have a higher status than the previous one, and 'D' meaning the next guest should have a lower status than the previous one.

You need to create a 0-indexed string guest_order of length n + 1 that satisfies the following conditions:

guest_order consists of the digits '1' to '9', where each digit represents the guest's status and is used at most once.
If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
Return the lexicographically smallest possible string guest_order that meets the conditions.

def arrange_guest_arrival_order(arrival_pattern):
  pass
Example Usage:

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  
Example Output:

123549876
4321
💡 Hint: Stacks
This question may be answered using a stack, which is a new data structure. To learn more about stacks and how to use them in Python, check out the unit cheatsheet or use a search engine or generative AI tool to conduct your own research.
'''

def arrange_guest_arrival_order(arrival_pattern):
    stack = []
    result = []

    for i in range(len(arrival_pattern) + 1):
        stack.append(str(i + 1))

        if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
            while stack:
                result.append(stack.pop())

    return ''.join(result)

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD")) 