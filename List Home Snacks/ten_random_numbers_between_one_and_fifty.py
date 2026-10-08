import random

sum_of_even_indices = 0
sum_of_odd_indices = 0
counter = 0
average = 0
sum_of_numbers = 0
product = 1
list_of_numbers = []

for numbers in range(1,11):
	random_numbers = random.randint(1,50)
	list_of_numbers.append(random_numbers)
	counter += 1


largest_number = list_of_numbers[0]
smallest_number = list_of_numbers[0]

for index in range(0,len(list_of_numbers)):
	if list_of_numbers[index] > largest_number:
		largest_number = list_of_numbers[index]

	if list_of_numbers[index] < smallest_number:
		smallest_number = list_of_numbers[index]
	
	
	sum_of_numbers += list_of_numbers[index]

	if index % 2 == 0:
		sum_of_even_indices += list_of_numbers[index]
	else:
		sum_of_odd_indices += list_of_numbers[index]

average = sum_of_numbers / counter


for index in range(2,len(list_of_numbers),3):
	product *= list_of_numbers[index]
	


print(list_of_numbers)
print("The length of the list =", counter)
print("Sum of elements at even positions =", sum_of_even_indices)
print("Sum of elements at odd positions =", sum_of_odd_indices)
print("The product of third indices =", product)
print("The average of the numbers =", average)
print("The largest number =", largest_number)
print("The smallest number =", smallest_number)


def count_words(list_of_words):
	word = []
	count = 0
	for index in range(0,len(list_of_words)):
		if type(list_of_words[index]) == str:
			count += 1

			if len(list_of_words[index]) >= 2 and list_of_words[index][0] == list_of_words[index][-1]:
				word.append(list_of_words[index])
					
	return word,count

word_list = ["eye","them",9,"lovely",10,"madam"]
results = count_words(word_list)

print(f"The number of words = {results[1]}")
print(f"The words with the same first and last letters = {results[0]}")
	

	