import fileinput

total = 0

for line in fileinput.input():
	dist = len(line)
	dist /= 2
	for i in range(0, len(line)):
		if line[i] == line[i - int(dist)]:
			total += int(line[i])

print(total)

fileinput.close()