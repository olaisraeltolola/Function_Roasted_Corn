def word_repeat(word,number):
	if type(number) == int:
		return word * number
	else:
		return word

print(word_repeat("hi",4.5))