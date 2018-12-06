from min_heap import *

def main():
	#Create heap
	heap = Heap()

	#Read numbers from file into heap
	with open("numbers.txt") as file:
		
		line = file.read()
		numbers = line.split(",")
		for num in numbers:
			heap.insert(float(num))
	file.close()
	#Print sorted list
	while not heap.is_empty():
		print(heap.extract_min())
main()