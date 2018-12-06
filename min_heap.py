class Heap:
	def __init__(self):
		self.heap_array = []
		
	def insert(self, k):
		#Inserts new element at the last index
		self.heap_array.append(k)
		
		#Percolate node to correct position
		self.percolate_up(len(self.heap_array)-1)
		
	def extract_min(self):
		if self.is_empty():
			return None
		
		#Save the element to extract
		min_elem = self.heap_array[0]
		
		#Move last element to first spot
		last_elem = self.heap_array.pop()

		if len(self.heap_array) != 0:
			self.heap_array[0] = last_elem
		else:
			return last_elem
		self.percolate_down(0)
		return min_elem
		
	def is_empty(self):
		return len(self.heap_array) == 0
		
	def percolate_up(self, index):
		#Traverse indexes until balanced or at last child index (1)
		while index > 0:
			parent_index = (index - 1) // 2
			
			#Found the correct spot
			if self.heap_array[index] >= self.heap_array[parent_index]:
				return
			else:
				#Swap current node with parent
				temp = self.heap_array[index]
				self.heap_array[index] = self.heap_array[parent_index]
				self.heap_array[parent_index] = temp
				
				#Prepare to check the next node
				index = parent_index
				
	def percolate_down(self, index):
		child_index = 2 * index + 1
		value = self.heap_array[index]
		
		while child_index < len(self.heap_array):
			
			min_value = value
			min_index = -1
			i=0
			
			#check children to see which is bigger
			while i < 2 and i + child_index < len(self.heap_array):
				if self.heap_array[i + child_index] < min_value:
					min_value = self.heap_array[i + child_index]
					min_index = i + child_index
				i = i+1
			
			
			if min_value == value:
				return
			else:
				
				temp = self.heap_array[index]
				self.heap_array[index] = self.heap_array[min_index]
				self.heap_array[min_index] = temp
				
				index = min_index
				child_index = 2 * index + 1
