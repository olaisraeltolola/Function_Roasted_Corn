def maximum_number(*number_list):
	largest_number = number_list[0]
	for number in number_list:
		if number > largest_number:
			largest_number = number
	return largest_number

print(maximum_number(8,4,9,2,5,7,3))