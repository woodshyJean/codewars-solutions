
'''A pangram is a sentence that contains every single letter of the alphabet at least once. For example, 
the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once 
(case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.


/////////////////////////////////////////// solution ////////////////////////////////////////////// '''


import string
import collections

def is_pangram(s):
  letters = list(string.ascii_lowercase)
  ns = ''.join(filter(str.isalnum, set(list(s.lower()))))
  ns = [x for x in ns if x not in ['0','1','2','3','4','5','6','7','8','9'] ]
  if len(ns) == len(letters):
    return True
  else:
    return False
