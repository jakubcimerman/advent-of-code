import math
import numpy as np

data = np.loadtxt('1.txt', unpack=True)

def main_a():
	depth = data
	cnt = 0

	for i in range(len(depth)-1):
		if (depth[i+1]>depth[i]):
			cnt += 1

	print(cnt)

def main_b():
	depth = data
	cnt = 0

	for i in range(len(depth)-3):
		if (depth[i+1]+depth[i+2]+depth[i+3] > depth[i]+depth[i+1]+depth[i+2]):
			cnt += 1

	print(cnt)

main_a()
main_b()