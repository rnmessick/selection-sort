import random

def insertion_sort(a_list):
	for idx in range(1, len(a_list)):
		val = a_list[idx]
		order = idx
		while order > 0 and a_list[order-1] > val:
			a_list[order] = a_list[order-1]
			order = order-1
		a_list[order] = val

my_list = random.sample(xrange(0, 10000), 100)
insertion_sort(my_list)
print my_list