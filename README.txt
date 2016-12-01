1. 
Online running time: 
O(NlogN+mlogm) where N is the number of anagrams, m is the number of characters of query string

Offline running time:
O(Nlogm), where N is the total number of characters in the dictionary, m is the number of character of the longest string

2. 
Memory Complexity: 
O(N), where N is the total number of characters in the dictionary


3. 
Optimization:
Store the filenames of serialized nodes that contain list of anagrams as values of the hashmap. 


### Algorithm description:
During the offline phase, I built a hashmap where key is the sorted lower case string, and values are the words in the dictionary that corresponds. During online phase, I sort the lower case query and find its corresponding anagrams in O(1) time. Later I sort the anagrams in lexical order