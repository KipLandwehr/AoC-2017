import fileinput

total = 0

for line in fileinput.input():
	numbers = line.split()
	min = int(numbers[0])
	max = int(numbers[0])
	for i in range(0, len(numbers)):
		if int(numbers[i]) < min:
			min = int(numbers[i])
		if int(numbers[i]) > max:
			max = int(numbers[i])
	total += max - min

print(total)

fileinput.close()