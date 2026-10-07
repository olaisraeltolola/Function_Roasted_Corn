def remove_odd_index(word):
	new_word = ""
	for index in range(0,len(word)):
		if index % 2 != 0:
			new_word += word[index]
	return new_word

print(remove_odd_index("semicolon"))