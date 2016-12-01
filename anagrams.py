import sys
from sets import Set

def build_dict(filename):
	with open(filename) as f:
		words = f.read().splitlines()
	key_map = {}
	for word in words:
		s_word = str(sorted(word.lower()))
		if s_word not in key_map:
			key_map[s_word] = []
		key_map[s_word].append(word)
	return key_map


def find_anagrams(word, dictionary):
	s_word = str(sorted(word.lower()))
	if s_word not in dictionary:
		return []
	else:
		return dictionary[s_word]



if __name__ == "__main__":
	print "Processing data"
	dictionary = build_dict(sys.argv[1])
	print "Finished processing"
	while True:
		try:
			word = raw_input('> ')
			res = find_anagrams(word, dictionary)
			if len(res) == 0:
				print "-"
			else:
				print " ".join(sorted(res))
		except KeyboardInterrupt:
			break