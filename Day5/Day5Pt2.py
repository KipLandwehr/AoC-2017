import fileinput

steps = 0
instructions = []

for line in fileinput.input():
	instructions.append(int(line))

index = 0

while index < len(instructions) and index >= 0:
	temp = index
	index += instructions[temp]
	
	if instructions[temp] < 3:
		instructions[temp] += 1
	else:
		instructions[temp] -= 1
	
	steps += 1

print(steps)

fileinput.close()