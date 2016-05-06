import random

def selection_sort(lst):
	for i in range(0, len(lst) -1):
		minIndex = i
		for x in range(i+1, len(lst)):
			if lst[x] < lst[minIndex]:
				minIndex = x
		if minIndex != i:
			lst[i], lst[minIndex] = lst[minIndex], lst[i]
new_lst = random.sample(xrange(0, 10000), 100)		
selection_sort(new_lst)
print(new_lst)

