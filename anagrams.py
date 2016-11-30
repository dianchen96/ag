import sys
from itertools import permutations
from sets import Set

class TrieNode:
	""" A TrieNode implemetation
	@c: the character represented this node
	@children: its children TrieNodes
	@isLeaf: boolean; whether this is a leaf TrieNode
	"""
	def __init__(self, c):
		self.c = c
		self.children = {}
		self.isLeaf = True

class Trie:
	""" A wrapper of TrieNode
	@root: its root TrieNode

	>>> trie = Trie()
	>>> trie.add_word('apple')
	>>> trie.find_word('apple')[0]
	True
	>>> trie.find_word('app')[0]
	False
	"""
	def __init__(self):
		self.root = TrieNode(None)

	def add_word(self, word):
		node = self.root
		for c in word:
			if c not in node.children:
				node.children[c] = TrieNode(c)
			node.isLeaf = False
			node = node.children[c]
		node.isLeaf = True

	def find_word(self, word):
		node = self.root
		for i, c in enumerate(word):
			if c not in node.children:
				return False, node, i
			node = node.children[c]
		return node.isLeaf, node, i

def all_casings(input_string):
	if not input_string:
		yield ""
	else:
		first = input_string[:1]
		if first.lower() == first.upper():
			for sub_casing in all_casings(input_string[1:]):
				yield first + sub_casing
	  	else:
	  		for sub_casing in all_casings(input_string[1:]):
	  			yield first.lower() + sub_casing
	  			yield first.upper() + sub_casing



def find_anagrams(word, trie):
	perms = [''.join(p) for p in permutations(word)]
	res = Set([])
	taboo = None

	for p in perms:
		for perm in all_casings(p):
			if taboo:
				index, char = taboo
				if perm[index] == char:
					continue
				else:
					taboo = None
			flag, node, i = trie.find_word(perm)
			if not flag:
				taboo = i, node.c
			else:
				res.add(perm)
	return res

def build_trie(filename):
	with open(filename) as f:
		lines = f.read().splitlines()
	trie = Trie()
	for word in lines:
		trie.add_word(word)
	return trie


if __name__ == "__main__":
	print "Processing data"
	trie = build_trie(sys.argv[1])
	print "Finished processing"
	while True:
		try:
			word = raw_input('> ')
			res = find_anagrams(word, trie)
			if len(res) == 0:
				print "-"
			else:
				print " ".join(sorted(res))
		except KeyboardInterrupt:
			break