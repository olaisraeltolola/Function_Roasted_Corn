def longest_word(*list):

	length_longest_word = len(list[0])	
	longest_word = list[0]

	for word in list:
		if len(word) > length_longest_word:
			longest_word = word
			length_longest_word = len(word)

	return longest_word, length_longest_word

results = longest_word("welcome","out","weather","mobile","breakfast","journey") 
print(f"{results[0]}, {results[1]}")