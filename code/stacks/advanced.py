'''
Problem 1: Extra Treats
In a pet adoption center, there are two groups of volunteers: the "Cat Lovers" and the "Dog Lovers."

The center is deciding on which type of pet should be receive extra treats that week, and the voting takes place in a round-based procedure. In each round, each volunteer can exercise one of the two rights:

Ban one volunteer's vote: A volunteer can make another volunteer from the opposite group lose all their rights in this and all the following rounds.
Announce the victory: If a volunteer finds that all the remaining volunteers with the right to vote are from the same group, they can announce the victory for their group and prioritize their preferred pet for extra treats.
Given a string votes representing each volunteer's group affiliation. The character 'C' represents "Cat Lovers" and 'D' represents "Dog Lovers". The length of the given string represents the number of volunteers.

Predict which group will finally announce the victory and prioritize their preferred pet for extra treats. The output should be "Cat Lovers" or "Dog Lovers".

def predictAdoption_victory(votes):
  pass
Example Usage:

print(predictAdoption_victory("CD")) 
print(predictAdoption_victory("CDD")) 
Example Output:

Cat Lovers
Dog Lovers
'''

from collections import deque
def predictAdoption_victory(votes):
    
    c_q = deque()
    d_q = deque()

    for i, vote in enumerate(votes):
        if vote == 'C':
            c_q.append(i)
        else:
            d_q.append(i)

    n = len(votes)
    while c_q and d_q:

        c_i  = c_q.popleft()
        d_i = d_q.popleft()

        if c_i < d_i:
            c_q.append(c_i + n)
        else:
            d_q.append(d_i + n)
    
    return 'Cat Lovers' if len(c_q) > 0 else "Dog Lovers"



print(predictAdoption_victory("CD")) 
print(predictAdoption_victory("CDD")) 

'''
Problem 2: Pair Up Animals for Shelter
In an animal shelter, animals are paired up to share a room. Each pair has a discomfort level, which is the sum of their individual discomfort levels. The shelter's goal is to minimize the maximum discomfort level among all pairs to ensure that the rooms are as comfortable as possible.

Given a list discomfort_levels representing the discomfort levels of n animals, where n is even, pair up the animals into n / 2 pairs such that:

Each animal is in exactly one pair, and
The maximum discomfort level among the pairs is minimized. Return the minimized maximum discomfort level after optimally pairing up the animals.
Return the minimized maximum comfort level after optimally pairing up the animals.

def pair_up_animals(discomfort_levels):
  pass
Example Usage:

print(pair_up_animals([3,5,2,3]))  
print(pair_up_animals([3,5,4,2,4,6])) 
Example Output:

7
8
'''

def pair_up_animals(discomfort_levels):
    discomfort_levels.sort()

    res = 0

    l, r = 0, len(discomfort_levels) - 1

    while l < r:
        res = max(discomfort_levels[l] + discomfort_levels[r], res)
        l += 1
        r -= 1
    
    return res

print(pair_up_animals([3,5,2,3]))  
print(pair_up_animals([3,5,4,2,4,6])) 

'''
Problem 3: Rearrange Animals and Slogans
You are given a string s that consists of lowercase English letters representing animal names or slogans and brackets. The goal is to rearrange the animal names or slogans in each pair of matching parentheses by reversing them, starting from the innermost pair.

After processing, your result should not contain any brackets.

def rearrange_animal_names(s):
  pass
Example Usage:

print(rearrange_animal_names("(dribtacgod)"))
print(rearrange_animal_names("(!(love(stac))I)")) 
print(rearrange_animal_names("adopt(yadot(a(tep)))!")) 
Example Output:

dogcatbird
Ilovecats!
adoptapettoday!
'''

def rearrange_animal_names(s):
    '''
    add value to stack until I encounter ')' bracket.
    once you encounter it remove and add all of them to string and stop when you encounter '('
    add the resulting string to res stack
    '''
    stack = []
    for i in s:
        if i == ')' and stack and stack[-1] != '(':
            temp = []
            while stack:
                character = stack.pop()
                if character == '(':
                    break
                temp.append(character) 
            stack.extend(temp)
        else:
            stack.append(i)
    
    return ''.join(stack)

print(rearrange_animal_names("(dribtacgod)"))
print(rearrange_animal_names("(!(love(stac))I)")) 
print(rearrange_animal_names("adopt(yadot(a(tep)))!")) 


'''
Problem 4: Append Animals to Include Preference
You are managing an animal adoption center, and you have two lists of animals: available and preferred, both consisting of lowercase English letters representing different types of animals.

Return the minimum number of characters that need to be appended to the end of the available list so that preferred becomes a subsequence of available.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

def append_animals(available, preferred):
  pass
Example Usage:

print(append_animals("catsdogs", "cows")) 
print(append_animals("rabbit", "r")) 
print(append_animals("fish", "bird"))
Example Output:

2
0
4
'''

def append_animals(available, preferred):
    preferred_length = len(preferred)

    l = i = 0

    while i < len(available) and l < preferred_length:
        if available[i] == preferred[l]:
            l += 1
        i += 1
    
    return preferred_length - l


print(append_animals("catsdogs", "cows")) 
print(append_animals("rabbit", "r")) 
print(append_animals("fish", "bird"))