import sys

arg = int(sys.argv[1])
ring = 0

while arg > (((2 * ring) + 1) ** 2):
	ring += 1

bottomRight = (((2 * ring) + 1) ** 2)
bottomLeft = bottomRight - (2 * ring)
topLeft = bottomLeft - (2 * ring)
topRight = topLeft - (2 * ring)

if arg == bottomRight or arg == bottomLeft or arg == topLeft or arg == topRight:
	print(ring * 2)

mid = 0

if arg < bottomRight and arg > bottomLeft:
	mid = bottomRight - ring

if arg < bottomLeft and arg > topLeft:
	mid = bottomLeft - ring

if arg < topLeft and arg > topRight:
	mid = topLeft - ring

if arg < topRight:
	mid = topRight - ring

if arg == mid:
	print(ring)

if arg < mid:
	offset = 0
	while (arg + offset) < mid:
		offset += 1
	print(ring + offset)

if arg > mid:
	offset = 0
	while (arg - offset) > mid:
		offset += 1
	print(ring + offset)