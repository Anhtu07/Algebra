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
		if (number_set_element <= 0) or (number_rel_element < 0):
			print("Why are you doing this to me :v")
			return
		if number_rel_element > number_set_element*number_set_element:
			print("What do you from me :v")
			return
		while len(self.rel_data) < number_rel_element:
			relation = (randint(1, number_set_element), randint(1, number_set_element))
			hash_value = self.open_hash(relation)
			if self.rel_data.has_key(hash_value) != True:
				self.rel_data[hash_value] = relation



# This part is for user interact
# var1 is the cardinality of set X
# var2 is the cardinality of relation D on X


if __name__ == '__main__':
	from sys import argv
	script, filename = argv
	var1 = raw_input('Enter number of element in X (from 1 to 1000) : ')
	var1 = int(var1)
	var2 = raw_input("Enter number of element in  relation D (from 1 to 10^6) : ")
	var2 = int(var2)
	gen = Generator()
	gen.generate_rel(var1, var2)

	target = open(filename, 'w')
	charaters = gen.rel_data.values()
	for char in charaters:
		target.write(str(char))
		target.write('\n')
	target.close()

