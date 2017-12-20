import fileinput

total = 0

for line in fileinput.input():
	for i in range(0, len(line)):
		if line[i] == line[i - 1]:
			total += int(line[i])

print(total)

fileinput.close()