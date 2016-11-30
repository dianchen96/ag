1. 
Online running time: 
Worst Case: O(N*N!) (All permutations are in the dictionary), where N is the length of the query. 

Offline running time:
O(N), where N is the total number of characters in the dictionary

2. 
Memory Complexity: 
Worst Case: O(N), where N is the total number of characters in the dictionary


3. 
Optimization:
Store the trie data structure on disk. The children field of each node is the filenames of other nodes stored
on the disk. This can be done by using the pickle library of python. When traversing the trie, we only keep one trie node in memory.


### Algorithm description:
During the offline phase, I built a trie and store all the words into the trie. This allows fast string query. During the online phase, I iterate through all the permutations of the query word and check if its in the dictionary by querying the trie. I made a small optmization at querying the trie: since the permutations are generated in order, if a word does not exist in the trie (terminate at some node), all permutations that has the same perfix are directly ignored. 