import fileinput

total = 0

for line in fileinput.input():
	numbers = line.split()
	for i in range(0, len(numbers)):
		for j in range(i+1, len(numbers)):
			div = 0
			if int(numbers[i]) < int(numbers[j]):
				div = int(numbers[j]) / int(numbers[i])
			if int(numbers[j]) < int(numbers[i]):
				div = int(numbers[i]) / int(numbers[j])
			if float(div).is_integer():
				total += div

print(total)

fileinput.close()