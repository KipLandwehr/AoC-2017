import fileinput

count = 0

for line in fileinput.input():
	tWords = line.split()
	uWords = set(tWords)
	if len(tWords) == len(uWords):
		count += 1

print(count)

fileinput.close()