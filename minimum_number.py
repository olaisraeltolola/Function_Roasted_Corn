def minimum_number(*number_list):
	smallest_number = number_list[0]
	for number in number_list:
		if number < smallest_number:
			smallest_number = number
	return smallest_number

print(minimum_number(8,4,9,2,5,7,3))