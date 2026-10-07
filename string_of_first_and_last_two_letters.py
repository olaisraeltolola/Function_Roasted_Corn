def first_and_last_two_letters(word):
	if len(word) >= 2: 
		new_word = word[0] + word[1] + word[len(word) - 2] + word[len(word) - 1]
		return new_word
	else: 
		return '""'

print(first_and_last_two_letters("ono"))