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
		tmp = {}
		for s in self.set_of_sets:
			for e in s:
				if tmp.has_key(e) is False:
					tmp[e] = e
		result = tmp.values()
		return result

	def intersections(self):
		tmp = {}
		intersects = {}
		set_number = 0
		for s in self.set_of_sets:
			if set_number == 0:
				for e in s:
					tmp[e] = e
				set_number = set_number + 1
			else:
				for e in s:
					if tmp.has_key(e):
						intersects[e] = e
				tmp = intersects
				intersects = {}
		return tmp



la = SetOperation()
la.set_of_sets = [[1,2,3,78] , [3,45,332,54] , [3,213,5,68]]
na = la.intersections()
print(na)