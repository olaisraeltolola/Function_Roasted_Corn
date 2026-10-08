number_list = []
for numbers in range(1,16):
	number_list.append(numbers)

print(number_list)



def add_number(list_of_numbers):
	sum_of_numbers = 0
	for index in range(2,len(list_of_numbers),3):
		sum_of_numbers += list_of_numbers[index]

	return sum_of_numbers

list_of_numbers = [2,3,4,6,7,5,9,12,34,7]

print(add_number(list_of_numbers))


def sum_of_first_middle_and_last_numbers(list_of_numbers):
	sum_of_numbers = 0
	if len(list_of_numbers) % 2 == 0:
		average_of_middle_numbers = (list_of_numbers[len(list_of_numbers)//2] + list_of_numbers[(len(list_of_numbers)//2) - 1])//2

		sum_of_numbers = list_of_numbers[0] + list_of_numbers[-1] + average_of_middle_numbers

	else:
		sum_of_numbers = list_of_numbers[0] + list_of_numbers[-1] + list_of_numbers[len(list_of_numbers)//2] 

	return sum_of_numbers

print(sum_of_first_middle_and_last_numbers(list_of_numbers))



