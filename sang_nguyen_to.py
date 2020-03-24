def sang_nguyen_to(start = 0, end = 100):
	# Khởi tạo một mảng chưa end - start phần tử 

	length = (end - start)
	elements = [True] * length
	elements[start], elements[start] = False, False

	start = 2
	for i in range(start, length):
		j = i * i
		while j < length:
			elements[j] = False
			j += i

	for i in range(start, length):
		if elements[i]:
			print(i, end=" ")
	return elements

sang_nguyen_to(20,1000)
