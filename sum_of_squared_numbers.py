def square_of_numbers(number_list):
	sum = 0
	for index in range(0,len(number_list)):
		number_list[index] = number_list[index] ** 2
		sum += number_list[index]
	return sum

list_of_numbers = [2,3,4,5,7]

print(square_of_numbers(list_of_numbers))