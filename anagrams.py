import sys
from itertools import permutations
from sets import Set

class TrieNode:
	def __init__(self, c):
		self.c = c
		self.children = {}
		self.isLeaf = True

class Trie:
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


def find_anagrams(word, trie):
	word = word.lower()
	perms = [''.join(p) for p in permutations(word)]
	res = Set([])
	taboo = None



	for perm in perms:
		if trie.find_word(perm)[0]:
			res.add(perm)
	return res

	# for perm in perms:
	# 	# Process taboos
	# 	if taboo:
	# 		index, char = taboo
	# 		if perm[index] == char:
	# 			continue
	# 		else:
	# 			taboo = None
	# 	flag, node, i = trie.find_word(perm)
	# 	if not flag:
	# 		taboo = i, node.c
	# 	else:
	# 		res.append(perm)
	# return res




def build_trie(filename):
	with open(filename) as f:
		lines = f.read().splitlines()
	trie = Trie()
	for word in lines:
		word = word.lower()
		trie.add_word(word)
	return trie


if __name__ == "__main__":
	# trie = Trie()

	# trie.add_word("alpha")
	# trie.add_word("beta")
	# trie.add_word("gamma")
	# trie.add_word("delta")
	# trie.add_word("beat")
	# trie.add_word("bate")
	# trie.add_word("magma")
	# trie.add_word("taled")

	# print trie.find_word("alpha")



	# print "Processing data"
	trie = build_trie(sys.argv[1])
	print trie.find_word("alpha")
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



# def anagram(w, dict):