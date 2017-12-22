import fileinput

count = 0

for line in fileinput.input():
	tWords = line.split()
	for i in range(0, len(tWords)):
		tWords[i] = ''.join(sorted(tWords[i]))
		
	uWords = set(tWords)
	if len(tWords) == len(uWords):
		count += 1

print(count)

fileinput.close()