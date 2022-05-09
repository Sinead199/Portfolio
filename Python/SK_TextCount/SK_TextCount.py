# -*- coding: utf-8 -*-
"""
Created on Fri May  6 15:17:17 2022

@author: Sinead K
"""

# 1) Convert a string to lowercase characters.

s = """Imagine a vast sheet of paper on which straight Lines, Triangles, Squares, Pentagons, Hexagons, and other figures, instead of remaining fixed in their places, move freely about, on or in the surface, but without the power of rising above or sinking below it, very much like shadows - only hard and with luminous edges - and you will then have a pretty correct notion of my country and countrymen. Alas, a few years ago, I should have said "my universe": but now my mind has been opened to higher views of things."""
 
#do not change any code above this line
#your code here
s_lower = s.lower()
print("The string in lowercase: ")
print(s_lower)

# 2) Split the lowercase string into individual words.

words = list() #do not delete. this list must contain the list of words. 
 
#your code goes here
words = s_lower.split()

print("The string split into individual words: ")
print(words) #do not delete 
#do not write any code past here

# 3) Count the number of words in the lowercase string.

print("The number of words in the string is: ",len(words))

# 4) Determine the number of distinct words in the lowercase string.

distinct_words = set(words)
print("The number of distinct words is: ",len(distinct_words))

# 5) Calculate the number of times each word appears in the lowercase string.

word_freq = dict()

for word in words:
    if (word in word_freq):
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("The frequency that words appear in the string:")
print(word_freq) 

# 6) Remove the punctuation from the lowercase string.

import string #import the string module 
#use the string.punctuation built-in python to create a list of all punctuations
punctuation_list =  list(string.punctuation)  #do not delete this

w_clean = list()
#your code goes here 
for word in words:
    for letter in word:
        if letter in punctuation_list:
            word = word.replace(letter,"")   
    w_clean.append(word)
    w_clean = list(filter(None, w_clean))
        
print("This is the string without punctuation:")
print(w_clean)
print("The number of words in the cleaned list is :",len(w_clean))
print("The number of distinct words in the cleaned list is: ",len(set(w_clean)))

# 7) Perform a count analysis on the text without punctuation characters.

count_ana = dict()

for word in w_clean:
    if (word in count_ana):
        count_ana[word] += 1
    else:
        count_ana[word] = 1
        
print("Count Analysis:")
for key, value in count_ana.items():
    print ((key, value))