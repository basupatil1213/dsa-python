from collections import Counter
def count_pairs(values):
    seen = set()
    pairs = 0
    for value in values:
        reverse = value[::-1]
        if reverse in seen:
            pairs += 1
            seen.remove(reverse)
        else:
            seen.add(value)
    return pairs


signals1 = ["cd", "ac", "dc", "ca", "zz"]
signals2 = ["ab", "ba", "cc"]
signals3 = ["aa", "ab"]

'''
Example Output:
2
1
0
'''

print(count_pairs(signals1))
print(count_pairs(signals2))
print(count_pairs(signals3))


'''
Problem 1: Cook Off
In a reality TV show, contestants are challenged to do the best recreation of a meal cooked by an all-star judge using limited resources. The meal they must recreate is represented by the string target_meal. The contestants are given a collection of ingredients represented by the string ingredients.

Help the contestants by writing a function max_attempts() that returns the maximum number of copies of target_meal they can create using the given ingredients. You can take some letters from ingredients and rearrange them to form new strings.

def max_attempts(ingredients, target_meal):
    pass
Example Input:

ingredients1 = "aabbbcccc"
target_meal1 = "abc"

ingredients2 = "ppppqqqrrr"
target_meal2 = "pqr"

ingredients3 = "ingredientsforcooking"
target_meal3 = "cooking"
Example Output:

2
3
1
'''

# def max_attempts(ingredients, target_meal):
#     ingredients_c = dict(Counter(ingredients))
#     target_meal_c = dict(Counter(target_meal))

#     c = []

#     for key, value in target_meal_c.items():
#         if key in ingredients:
#             c.append(min(value, ingredients_c[key]))
    
#     return min(c)

# ingredients1 = "aabbbcccc"
# target_meal1 = "abc"
# print(max_attempts(ingredients1, target_meal1))
# ingredients2 = "ppppqqqrrr"
# target_meal2 = "pqr"
# print(max_attempts(ingredients2, target_meal2))

# ingredients3 = "ingredientsforcooking"
# target_meal3 = "cooking"
# print(max_attempts(ingredients3, target_meal3))


'''
Problem 2: Dialogue Similarity
Watching a reality TV show, you notice a lot of contestants talk similarly. We want to determine if two contestants have similar speech patterns.

We can represent a sentence as an array of words, for example, the sentence "I've got a text!" can be represented as sentence = ["I've", "got", "a", "text"].

You are given two sentences from different contestants sentence1 and sentence2 each represented as a string array and given an array of string pairs similar_pairs where similar_pairs[i] = [xi, yi] indicates that the two words xi and yi are similar. Write a function is_similar() that returns True if sentence1 and sentence2 are similar, and False if they are not similar.

Two sentences are similar if:

They have the same length (i.e., the same number of words)
sentence1[i] and sentence2[i] are similar
Notice that a word is always similar to itself, also notice that the similarity relation is not transitive. For example, if the words a and b are similar, and the words b and c are similar, a and c are not necessarily similar.

def is_similar(sentence1, sentence2, similar_pairs):
    pass
Example Usage:

sentence1 = ["my", "type", "on", "paper"]
sentence2 = ["my", "type", "in", "theory"]
similar_pairs = [ ["on", "in"], ["paper", "theory"]]

sentence3 = ["no", "tea", "no", "shade"]
sentence4 = ["no", "offense"]
similar_pairs2 = [["shade", "offense"]]

print(is_similar(sentence1, sentence2, similar_pairs))
print(is_similar(sentence3, sentence4, similar_pairs2))
Example Output:

True
Example 1 Explanation: "my" and "type" are similar to themselves. The words at 
indices 2 and 3 of sentence1 are similar to words at indices 2 and 3 of 
sentence2 according to the similar_pairs array. 

False
Example 2 Explanation: Sentences are of different length.
'''
def is_similar(sentence1, sentence2, similar_pairs):
    if len(sentence1) != len(sentence2):
        return False
    similarity_dict = {}

    for pair in similar_pairs:
        similarity_dict[pair[0]] = pair[1]
    
    for i in range(len(sentence1)):
        if sentence1[i] == sentence2[i]:
            continue
        if sentence1[i] in similarity_dict:
            if similarity_dict[sentence1[i]] != sentence2[i]:
                return False
        else:
            return False

    return True

sentence1 = ["my", "type", "on", "paper"]
sentence2 = ["my", "type", "in", "theory"]
similar_pairs = [ ["on", "in"], ["paper", "theory"]]

sentence3 = ["no", "tea", "no", "shade"]
sentence4 = ["no", "offense"]
similar_pairs2 = [["shade", "offense"]]

print(is_similar(sentence1, sentence2, similar_pairs))
print(is_similar(sentence3, sentence4, similar_pairs2))

'''
Problem 3: Cows and Bulls
In a reality TV show, contestants play a mini-game called Bulls and Cows for a prize. The objective is to guess a secret number within a limited number of attempts. You, as the host, need to provide hints to the contestants based on their guesses.

When a contestant makes a guess, you provide a hint with the following information:

The number of "bulls," which are digits in the guess that are in the correct position.
The number of "cows," which are digits in the guess that are in the secret number but are located in the wrong position.
Given the secret number secret and the contestant's guess guess, return the hint for their guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

def get_hint(secret, guess):
    pass
Example Input:

secret1 = "1807"
guess1 = "7810"

secret2 = "1123"
guess2 = "0111"

print(get_hint(secret1, guess1))
print(get_hint(secret2, guess2))
Example Output:

1A3B
Example 1 Explanation: 
Bulls are connected with a '|' and cows are marked with an asterisk:
"1807"
  |
"7810"
 * **

1A1B
Example 2 Explanation:
Bulls are connected with a '|' and cows are marked with an asterisk:
"1123"        "1123"
  |      or     |
"0111"        "0111"
   *              *
Note that only one of the two unmatched 1s is counted as a cow since the 
non-bull digits can only be rearranged to allow one 1 to be a bull.
'''

def get_hint(secret, guess):
    secret_dict = Counter(secret)
    bulls = 0
    cows = 0

    for i in range(len(guess)):
        if guess[i] == secret[i]:
            bulls += 1
            secret_dict[secret[i]] -= 1
        elif guess[i] in secret_dict and secret_dict[guess[i]] > 0:
            cows += 1
            secret_dict[guess[i]] -= 1
    
    return f'{bulls}A{cows}B'

secret1 = "1807"
guess1 = "7810"

secret2 = "1123"
guess2 = "0111"

print(get_hint(secret1, guess1))
print(get_hint(secret2, guess2))

'''
Problem 4: Count Winning Pairings
In a popular reality TV show, contestants pair up for various challenges. The pairing is considered winning if the sum of their "star power" is a power of two.

You are given an array of integers star_power where star_power[i] represents the star power of the i-th contestant. Return the number of different winning pairings you can make from this list, modulo 10^9 + 7.

Note that contestants with different indices are considered different even if they have the same star power.

def count_winning_pairings(star_power):
    pass
Example Usage:

star_power1 = [1, 3, 5, 7, 9]
print(count_winning_pairings(star_power1))

star_power2 = [1, 1, 1, 3, 3, 3, 7]
print(count_winning_pairings(star_power2))
Example Output:

4
15
'''

'''
Problem 5: Assigning Unique Nicknames to Contestants
In a reality TV show, contestants are assigned unique nicknames. However, two contestants cannot have the same nickname. If a contestant requests a nickname that has already been taken, the show will add a suffix to the name in the form of (k), where k is the smallest positive integer that makes the nickname unique.

You are given an array of strings nicknames representing the requested nicknames for the contestants. Return an array of strings where result[i] is the actual nickname assigned to the ith contestant.

def assign_unique_nicknames(nicknames):
    pass
Example Usage:

nicknames1 = ["Champ","Diva","Champ","Ace"]
print(assign_unique_nicknames(nicknames1))

nicknames2 = ["Ace","Ace","Ace","Maverick"]
print(assign_unique_nicknames(nicknames2)) 

nicknames3 = ["Star","Star","Star","Star","Star"]
print(assign_unique_nicknames(nicknames3))
Example Output:

["Champ","Diva","Champ(1)","Ace"]
["Ace","Ace(1)","Ace(2)","Maverick"]
["Star","Star(1)","Star(2)","Star(3)","Star(4)"]
'''

def assign_unique_nicknames(nicknames):
    d = {}
    res = []
    for nickname in nicknames:
        if nickname in d:
            res.append(f'{nickname}({d[nickname]})')
            d[nickname] += 1
        else:
            res.append(nickname)
            d[nickname] = 1
    
    return res

nicknames1 = ["Champ","Diva","Champ","Ace"]
print(assign_unique_nicknames(nicknames1))

nicknames2 = ["Ace","Ace","Ace","Maverick"]
print(assign_unique_nicknames(nicknames2)) 

nicknames3 = ["Star","Star","Star","Star","Star"]
print(assign_unique_nicknames(nicknames3))

'''
Problem 6: Pair Contestants
In a reality TV challenge, contestants must be paired up in teams. Each team's combined score must be divisible by a target number k. You are given an array of integers scores representing the scores of the contestants and an integer k.

You need to determine whether it is possible to pair all contestants such that the sum of the scores of each pair is divisible by k.

Return True if it is possible to form the required pairs, otherwise return False.

def pair_contestants(scores, k):
    pass
Example Usage:

scores1 = [1,2,3,4,5,10,6,7,8,9]
k1 = 5
print(pair_contestants(scores1, k1))

scores2 = [1,2,3,4,5,6]
k2 = 7
print(pair_contestants(scores2, k2))

scores3 = [1,2,3,4,5,6]
k3 = 10
print(pair_contestants(scores3, k3)) 
Example Output:

True
True
False
'''
def pair_contestants(scores, k):
    d = {i:1 for i in range(len(scores))}

    for i in range(len(scores)):
        for j in range(i+1, len(scores)):
            if d[i] > 0 and d[j] > 0 and (scores[i] + scores[j]) % k == 0:
                d[i] = 0
                d[j] = 0
    
    return sum(d.values()) == 0


scores1 = [1,2,3,4,5,10,6,7,8,9]
k1 = 5
print(pair_contestants(scores1, k1))

scores2 = [1,2,3,4,5,6]
k2 = 7
print(pair_contestants(scores2, k2))

scores3 = [1,2,3,4,5,6]
k3 = 10
print(pair_contestants(scores3, k3)) 