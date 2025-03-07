from collections import Counter
'''
Problem 1: The Library of Alexandria
In the ancient Library of Alexandria, a temporal rift has scattered several important scrolls across different rooms. You are given a dictionary library_catalog that maps room names to the number of scrolls that room should have and a second dictionary actual_distribution that maps room names to the number of scrolls found in that room after the temporal rift.

Write a function analyze_library() that determines if any room has more or fewer scrolls than it should. The function should return a dictionary where the keys are the room names and the values are the differences in the number of scrolls (actual number of scrolls - expected number of scrolls). You must loop over the dictionaries to compute the differences.

def analyze_library(library_catalog, actual_distribution):
    pass
Example Usage:

library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}


print(analyze_library(library_catalog, actual_distribution))
Example Output:

{'Room A': 0, 'Room B': -10, 'Room C': 10, 'Room D': 0}
'''

def analyze_library(library_catalog, actual_distribution):
    res = {}

    for key, value in library_catalog.items():
        res[key] = actual_distribution[key] - library_catalog[key]
    
    return res

library_catalog = {
    "Room A": 150,
    "Room B": 200,
    "Room C": 250,
    "Room D": 300
}

actual_distribution = {
    "Room A": 150,
    "Room B": 190,
    "Room C": 260,
    "Room D": 300
}


expected_res = {'Room A': 0, 'Room B': -10, 'Room C': 10, 'Room D': 0}
actual_res = analyze_library(library_catalog, actual_distribution)
print(analyze_library(library_catalog, actual_distribution))

print("Sucess" if actual_res == expected_res else "Failure")


'''
Problem 2: Grecian Artifacts
You've spent your last few trips exploring different periods of Ancient Greece. During your travels, you discover several interesting artifacts. Some artifacts appear in multiple time periods, while others in just one.

You are given two lists of strings artifacts1 and artifacts2 representing the artifacts found in two different time periods. Write a function find_common_artifacts() that returns a list of artifacts common to both time periods.

def find_common_artifacts(artifacts1, artifacts2):
    pass
Example Usage:

artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))
'''

def find_common_artifacts(artifacts1, artifacts2):
    a1set = set(artifacts1)
    res = []

    for artifact in artifacts2:
        if artifact in a1set:
            res.append(artifact)

    return res
        
artifacts1 = ["Statue of Zeus", "Golden Vase", "Bronze Shield"]
artifacts2 = ["Golden Vase", "Silver Sword", "Bronze Shield"]

print(find_common_artifacts(artifacts1, artifacts2))

'''
Problem 3: Souvenir Declutter
As a time traveler, you've collected a mountain of souvenirs over the course of your travels. You're running out of room to store them all and need to declutter. Given a list of strings souvenirs and a integer threshold, declutter your souvenirs by writing a function declutter() that returns a list of souvenirs strictly below threshold.

def declutter(souvenirs, threshold):
    pass
Example Usage:

souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3

souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold = 2
Example Output:

["alien egg", "map", "statue"]
["sword"]
'''
def declutter(souvenirs, threshold):
    counter = Counter(souvenirs)
    return [souvenir for souvenir in counter if counter[souvenir] < threshold]

souvenirs1 = ["coin", "alien egg", "coin", "coin", "map", "map", "statue"]
threshold1 = 3

print(declutter(souvenirs1, threshold1))

souvenirs2 = ["postcard", "postcard", "postcard", "sword"]
threshold2 = 2

print(declutter(souvenirs2, threshold2))

'''
Problem 4: Time Portals
In your time travel adventures, you are given an array of digit strings portals and a digit string destination. Return the number of pairs of indices (i, j) (where i != j) such that the concatenation of portals[i] + portals[j] equals destination.

Note: For index values i and j, the pairs (i, j) and (j, i) are considered different - order matters.

def num_of_time_portals(portals, destination):
    pass
Example Usage:

portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))
Example Output:

4
2
6
'''

def num_of_time_portals(portals, destination):
    res = 0

    for i in range(len(portals)):
        for j in range(i+1, len(portals)):
            if portals[i] + portals[j] == destination:
                res += 1
            if portals[j] + portals[i] == destination:
                res += 1

    return res

portals1 = ["777", "7", "77", "77"]
destination1 = "7777"
portals2 = ["123", "4", "12", "34"]
destination2 = "1234"
portals3 = ["1", "1", "1"]
destination3 = "11"

print(num_of_time_portals(portals1, destination1))
print(num_of_time_portals(portals2, destination2))
print(num_of_time_portals(portals3, destination3))