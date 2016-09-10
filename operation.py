class SetOperation:
	def __init__(self):
		self.set_of_sets = [] #storing sets that are used for operation

	def add(self, set):
		self.set_of_sets.append(set)

	def max(self, s):
		max_value = s[0]
		for element in s:
			if element > max_value:
				max_value = element
		return max_value

	def unions(self):
		length = 0
		for s in self.set_of_sets:
			length = length + self.max(s)
		tmp = [None]*length
		for s in self.set_of_sets:
			for element in s:
				if tmp[element] is None:
					tmp[element] = 1
		result = []
		count = 0
		for e in tmp:
			if e is not None:
				result.append(count)
			count = count + 1
		return result

	def intersections(self):
		


la = SetOperation()
la.set_of_sets = [[1,2,3,78] , [45,332,54] , [213,5,68]]
na = la.unions()
for s in na:
	print(s)