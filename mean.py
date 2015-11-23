import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

# use ggplot style sheet
style.use('ggplot')


mn = np.zeros(100000)
for i in range(1,100000):

	count = 0

	for j in range(1,i):
		a = random.randint(1,6)
		if a == 1:
			count = count + 1

	average = float(count)/float(i)
	mn[i]=average
print mn
fig = plt.figure()
plt.plot(mn)
fig.savefig('temp.png', dpi=fig.dpi)
