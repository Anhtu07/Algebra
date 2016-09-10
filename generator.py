from random import randint

class Generator:
	def __init__(self):
		self.set_data = [] #storing set X
		self.rel_data = {} #storing relation D

	def open_hash(self, key):
		length = len(self.set_data)
		return (key[0]-1)*length + key[1]

	def generate_set(self, number_of_element):
		i = 1
		while i <= number_of_element:
			self.set_data.append(i)
			i = i + 1

	def generate_rel(self, number_set_element, number_rel_element):
		self.generate_set(number_set_element)
		while len(self.rel_data) < number_rel_element:
			relation = (randint(1, number_set_element), randint(1, number_set_element))
			hash_value = self.open_hash(relation)
			if self.rel_data.has_key(hash_value) != True:
				self.rel_data[hash_value] = relation



# This part is for user interact
# var1 is the cardinality of set X
# var2 is the cardinality of relation D on X
var1 = raw_input('number of element: ')
var1 = int(var1)
var2 = raw_input('number of relation: ')
var2 = int(var2)
la = Generator()
la.generate_rel(var1, var2)
print(la.rel_data)
