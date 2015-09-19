import math
f = open('input.txt','r')
data = f.readlines()
d = []
for line in data:
	word = (line.strip('\n'))
	d.append(float(word))


def SD(data):
	avg = mean(data)
	s = 0
	for i in data:
		d = (i-avg)**2
		s = s + d
	sigma = s/len(data)
	return math.sqrt(sigma)

def mean(data):
	s= 0
	for i in data:
		s = s + i
	avg = s/len(data)
	return avg

print SD(d)
	

