# counter
from collections import defaultdict
from collections import Counter
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

counter = defaultdict(int)

for word in words:
    counter[word] += 1

print(dict(counter))

'''
Problem 1: Counting Treasure
Captain Blackbeard has a treasure map with several clues that point to different locations on an island. Each clue is associated with a specific location and the number of treasures buried there. Given a dictionary treasure_map where keys are location names and values are integers representing the number of treasures buried at those locations, write a function total_treasures() that returns the total number of treasures buried on the island.

def total_treasure(treasure_map):
    pass
Example Usage:

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 
Example Output:

15
50
'''

def total_treasures(treasure_map):
    return 0 if not treasure_map else sum(treasure_map.values())

treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

print(total_treasures(treasure_map1)) 
print(total_treasures(treasure_map2)) 


'''
Problem 2: Pirate Message Check
Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.

def can_trust_message(message):
    pass
Example Usage:

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))
Example Output:

True
False
'''
    
def can_trust_message(message):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    counter = dict(Counter(a))

    for c in message:
        if counter[c] != 0:
            counter[c] = 0
    
    return sum(counter.values()) == 0
    
message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

print(can_trust_message(message1))
print(can_trust_message(message2))

'''
Problem 3: Find All Duplicate Treasure Chests in an Array
Captain Blackbeard has an integer array chests of length n where all the integers in chests are in the range [1, n] and each integer appears once or twice. Return an array of all the integers that appear twice, representing the treasure chests that have duplicates.

def find_duplicate_chests(chests):
    pass
Example Usage:

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
Example Output:

[2, 3]
[1]
[]
'''
def find_duplicate_chests(chests):
    counter = dict(Counter(chests))

    return [x for x in counter if counter[x] == 2]

chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]
print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))


'''
Problem 4: Booby Trap
Captain Feathersword has found another pirate's buried treasure, but they suspect it's booby-trapped. The treasure chest has a secret code written in pirate language, and Captain Feathersword believes the trap can be disarmed if the code can be balanced. A balanced code is one where the frequency of every letter present in the code is equal. To disable the trap, Captain Feathersword must remove exactly one letter from the message. Help Captain Feathersword determine if it's possible to remove one letter to balance the pirate code.

Given a 0-indexed string code consisting of only lowercase English letters, write a function is_balanced() that returns True if it's possible to remove one letter so that the frequency of all remaining letters is equal, and False otherwise.

def is_balanced(code):
    pass
Example Usage:

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 
Example Output:

True
Explanation: Select index 4 and delete it: word becomes "argh" and each character has a frequency of 1.

False
Explanation: They must delete a character, so either the frequency of "h" is 1 and the frequency of "a" is 2, or vice versa. It is impossible to make all present letters have equal frequency.
'''

def is_balanced(code):
    unique_count = set()

    counter = dict(Counter(code))

    for key in counter:
        unique_count.add(counter[key])
    print(unique_count)
    return len(unique_count) <= 2

code1 = "arghh"
code2 = "haha"

print(is_balanced(code1)) 
print(is_balanced(code2)) 

'''
Problem 5: Overflowing With Gold
Captain Feathersword and their crew has discovered a list of gold amounts at various hidden locations on an island. Each number on the map corresponds to the amount of gold at a specific location. Captain Feathersword already has plenty of loot, and their ship is nearly full. They want to find two distinct locations on the map such that the sum of the gold amounts at these two locations is exactly equal to the amount of space left on their ship.

Given an array of integers gold_amounts representing the amount of gold at each location and an integer target, return the indices of the two locations whose gold amounts add up to the target.

Assume that each input has exactly one solution, and you may not use the same location twice. You can return the answer in any order.

def find_treasure_indices(gold_amounts, target):
    pass
Example Usage:

gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  
Example Output:

[0, 1]
[1, 2]
[0, 1]
'''

def find_treasure_indices(gold_amounts, target):
    gold_map = {}
    for i in range(len(gold_amounts)):
        if gold_amounts[i] in gold_map:
            return [gold_map[gold_amounts[i]], i]
        gold_map[target - gold_amounts[i]] = i

    return [-1, -1]
gold_amounts1 = [2, 7, 11, 15]
target1 = 9

gold_amounts2 = [3, 2, 4]
target2 = 6

gold_amounts3 = [3, 3]
target3 = 6

print(find_treasure_indices(gold_amounts1, target1))  
print(find_treasure_indices(gold_amounts2, target2))  
print(find_treasure_indices(gold_amounts3, target3))  


'''
Problem 6: Organize the Pirate Crew
Captain Blackbeard needs to organize his pirate crew into different groups for a treasure hunt. Each pirate has a unique ID from 0 to n - 1.

You are given an integer array group_sizes, where group_sizes[i] is the size of the group that pirate i should be in. For example, if group_sizes[1] = 3, then pirate 1 must be in a group of size 3.

Return a list of groups such that each pirate i is in a group of size group_sizes[i].

Each pirate should appear in exactly one group, and every pirate must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

def organize_pirate_crew(group_sizes):
    pass
Example Usage:

group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 
Example Output:

[[5], [0, 1, 2], [3, 4, 6]]
[[1], [0, 5], [2, 3, 4]]
'''

print('--------------Problem 6: Organize the Pirate Crew-----------------')
def organize_pirate_crew(group_sizes):
    groups = {}
    res = []
    for i in range(len(group_sizes)):
        if group_sizes[i] in groups:
            if len(groups[group_sizes[i]]) < group_sizes[i]:
                groups[group_sizes[i]].append(i)
            else:
                res.append(groups[group_sizes[i]])
                groups[group_sizes[i]] = [i]  
        else:
            groups[group_sizes[i]] = [i]
    for values in groups.values():
        res.append(values)
    return res

group_sizes1 = [3, 3, 3, 3, 3, 1, 3]
group_sizes2 = [2, 1, 3, 3, 3, 2]

print(organize_pirate_crew(group_sizes1))
print(organize_pirate_crew(group_sizes2)) 