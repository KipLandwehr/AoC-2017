import fileinput

#Stores the max value in 'list' in 'max[0]' and the 'list' index of that value into 'max[1]'
def getMax(list, max):
	for i in range(len(list)):
		if list[i] > max[0]:
			max[0] = list[i]
			max[1] = i

#Returns true if all elements in list1 and list2 are equivalent
def listEquiv(list1, list2):
	print("In listEquiv. Lists received:")
	print("list1 = ", list1)
	print("list2 = ", list2)

	if len(list1) != len(list2): return False
	
	retval = True
	for i in range(len(list1)):
		if(list1[i] != list2[i]): retval = False
	print("retval = ", retval)
	return retval

banks = []
for line in fileinput.input():
	banks = line.split()
	for i in range(len(banks)):
		banks[i] = int(banks[i])

fileinput.close()
print("banks = ", banks)

layouts = []
cycles = 0
repeat = True
print("layouts = ", layouts)
print("cycles = ", cycles)
print("repeat = ", repeat)

while repeat:
	#Append current bank layout to 'layouts'
	layouts.append(banks)
	print("layouts = ", layouts)

	#Using max[0] as value and max[1] as index
	max = [0, 0]
	print("max = ", max)

	#Put the max value of banks and the values index into the list 'max'
	getMax(banks, max)
	print("max = ", max)

	#Copy the max value and the index into their own variables
	value = max[0]
	print("value = ", value)
	index = max[1]
	print("index = ", index)

	#Set the index with the max value to zero
	banks[index] = 0
	print("banks = ", banks)

	#Set index to value of next index in rotation
	index = ((index + 1) % len(banks))
	print("index = ", index)

	#Redistribute the money
	for i in range(value):
		banks[index] += 1
		index = ((index + 1) % len(banks))
	
	print("banks = ", banks)
	cycles += 1
	print("cycles = ", cycles)

	for i in range(len(layouts)):
		print("i = ", i)
		print("banks = ", banks)
		print("layouts[i] = ", layouts[i])
		if listEquiv(banks, layouts[i]):
			repeat = False
	
	print("repeat = ", repeat)

print(cycles)