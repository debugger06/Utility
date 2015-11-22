import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style

# use ggplot style sheet
style.use('ggplot')


mn = np.zeros(100)
for i in range(1,100):

	count = 0

	for j in range(1,i):
		a = random.randint(1,6)
		if a = 1:
			count++
	average = count/if
	mn[i]=average

plt.plot(mn)
