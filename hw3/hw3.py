#Rock Beom Kim
#rk5dy
#Programming Assignment 3: Trading
import sys
import math
f = open(sys.argv[1], "r")
fileLine = f.read()
f.close()
lines = fileLine.split("\n")
"""
nlog(n) closest pairs call
"""
def findMin(a):
	#base case length 2: find the length
	if (len(a) < 3):
		return distance(a[0], a[1])
	#base case length 3: easy check of the major permutations of the three points
	if (len(a) < 4):
		dist1 = distance(a[0], a[1])
		dist2 = distance(a[1], a[2])
		dist3 = distance(a[0], a[2])
		if (dist1 < dist2 and dist1 < dist3):
			return dist1
		elif (dist2 < dist3 and dist2 < dist1):
			return dist2
		else:
			return dist3
	#split the array according to the vertical line
	split = len(a) / 2
	lSplit = a[:split]
	rSplit = a[split:]
	"""
	Recursive call to find the minimum of each half
	lMin = delta_L
	rmin = delta_R
	"""
	lMin = findMin(lSplit)
	rMin = findMin(rSplit)
	
	#find the delta for the delta_{L,R}
	tmpMin = 0.0
	if (lMin < rMin):
		tmpMin = lMin
	else:
		tmpMin = rMin
	
	#use list comprehensions to filter out the amount of points in the two half arrays
	divideLine = lSplit[len(lSplit) - 1][0] + rSplit[0][0] / 2
	leftHalf = [(x,y) for (x,y) in a[:split] if x > divideLine - tmpMin]
	rightHalf = [(x,y) for (x,y) in a[split:] if x < divideLine + tmpMin]
	merged = leftHalf + rightHalf

	merged.sort(cmp = ycmp)	
	i = 0
	j = 0
	"""
	I know it's a double while loop, but it's actually not n^2 because at most there are 7 inner steps
	"""
	while (i < len(merged)):
		j = i + 1
		while (j < i+8 and j < len(merged)):
			tmptmpMin = distance(merged[i], merged[j])
			if (tmptmpMin < tmpMin):
				tmpMin = tmptmpMin
			j += 1
		i += 1
	return tmpMin
	
#the comparison of x values for the first sort
def xcmp(a, b):
	return cmp(a[0], b[0])

#the comparison of y values for second sort
def ycmp(a, b):
	return cmp(a[1],b[1])

#distance formula to condense code
def distance(a, b):
	return math.sqrt((a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]))

#formatting the decimal value
def formatD(a):
	if "." not in a:
		return a
	else:
		nums = a.split(".")
		if (len(nums[1]) < 5):
			#make sure the value is rounded to 4 decimal places
			tmpD = nums[1].strip()
			while (len(tmpD) < 4):
				tmpD = tmpD + "0"
			return nums[0] + "." + tmpD
		else:
			postDecimal = int(nums[1][:5])
			#rounding up the decimal value
			if (postDecimal % 10 > 4):
				postDecimal += 10
				return nums[0] + "." + str(postDecimal)[:4] 
			#else return the decimal as is
			return nums[0] + "." + str(postDecimal)[:4]

index = 0
#this while loop goes through each test case
while (index < len(lines)):
	#noPoints = the number of points per test case
	noPoints = int(lines[index])
	tmpIndex = index + 1
	index += noPoints + 1
	if (noPoints == 0):
		break
	#print str(noPoints)
	points = []
	#gets list of points for each test case
	for a in range(0, noPoints):
		point = lines[a + tmpIndex].split(" ")
		points.append(((float(point[0])), (float(point[1]))))
	#sort so making the divide line is easier
	points.sort(cmp = xcmp)
	minimum = findMin(points)
	minD = formatD(str(minimum))

	#space ship can't go more than 10k distance
	if (float(minD) > 10000):
		print "infinity"
	else:
		print minD
