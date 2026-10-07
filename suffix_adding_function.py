def suffix_add(word):
	if len(word) >= 3:
		suffix = word[len(word) - 3] + word[len(word) - 2] + word[len(word) - 1]
		if suffix == "ing":
			new_word = word + "ly"
		else:
			new_word = word + "ing"

	else:
		new_word = word


	return new_word

print(suffix_add("adding"))