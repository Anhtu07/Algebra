from sys import argv
from random import randint
from math import log
class BinaryOperation:
	def __init__(self):
		self.operation_table = []
		self.size = 0

	def generate_binary_opertion(self, filename, n):
		#Create a binary operation table of * with number of element n 
		#The table of size n x n
		#And save the table in the file 'filename'
		#The table contains only integer from 1 to n
		column = 0
		row = 0
		target = open(filename, "w")
		while row < n: 
			while column < n:
				target.write(str(randint(0, n-1)))
				target.write(" ")
				column = column + 1
			target.write("\n")
			column = 0
			row = row + 1
		target.close()
		self.size = n

	def gen(self, filename, n):
		self.size = n
		column = 0
		row = 0
		target = open(filename, "w")
		target.write("    ")
		for i in xrange(n):
			target.write(str(i))
			if i >= 100:
				target.write(" ")
			elif i >= 10:
				target.write("  ")
			else:
				target.write("   ")
		target.write("\n")
		while row < n:
			target.write(str(row))
			if row >= 100:
				target.write(" ")
			elif row >= 10:
				target.write("  ")
			else:
				target.write("   ")
			while column < n:
				val = randint(0, n-1)
				string = str(val)
				target.write(string)
				if val >= 100:
					target.write(" ")
				elif val >= 10:
					target.write("  ")
				else:
					target.write("   ")
				column = column + 1
			row = row + 1
			target.write("\n")
			column = 0
		target.close()


	def create_table(self, filename):
		#A subroutine to put data in filename to a dict type opertation_table
		file = open(filename, "r")
		array = file.readlines()
		c = 0
		n = self.size
		while c <= n - 1:
			row = []
			tmp = []
			for char in array[c]:
				if char is not ' ':
					tmp.append(char)
				else:
					number = ''
					for ch in tmp:
						number = number + ch
					row.append(int(number))
					tmp = []
			self.operation_table.append(row)
			c = c + 1

	def is_associative(self):
		#Check a binary opertation whether it is associative using Light's algorithm
		#Return true if the operation is associative
		#Return false and print out a triple that dissatisfies associative property
		associative = True
		n = self.size
		for i in xrange(0,n):
			subtable = self.create_subtable(i)
			for x in xrange(0, n):
				val = self.operation_table[x][i]
				for m in xrange(0,n):
					if subtable[x][m] != self.operation_table[val][m]:
						result = [x, i, m]
						print(result)
						associative = False
						break
				if associative is False:
					break
			if associative is False:
				break
		return associative

	def create_subtable(self, i):
		#Create a table of binary operation x*i*y with a fixed i
		n = self.size
		subtable = [[0 for x in xrange(n)] for y in xrange(n)] 
		for x in xrange(0, n):
			val = self.operation_table[i][x]
			for m in xrange(0, n):
				subtable[m][x] = self.operation_table[m][val]
		return subtable
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#The following part is for optimized algorithm for checking whether an operation is associative
#The algortihm run in O(n^2 log n) time-complexity
#If the method return False, the considered binary operation dont have associativity
#If the method return True, the probality of error is 1/n (where n is the size of the table)
	def take_random(self):
		n = self.size
		a = [0 for x in xrange(n)]
		for i in xrange(n):
			a[i] = randint(0, 1)
		return a

	def op(self, a, b):
		n = self.size
		tmp = [0 for x in xrange(n)]
		for i in xrange(n-1):
			if a[i] == 1:
				for j in xrange(n-1):
					if b[j] == 1:
						val = self.operation_table[i][j]
						if tmp[val] == 0:
							tmp[val] = 1
						else:
							tmp[val] = 0
		return tmp

	def check_associative(self):
		n = self.size
		number_of_loop = 7*log(n)
		count = 0
		while count < number_of_loop:
			a = self.take_random()
			b = self.take_random()
			c = self.take_random()
			var1 = self.op(self.op(a, b), c)
			var2 = self.op(a, self.op(b, c))
			if var1 != var2:
				return False
			else:
				return True

#End Algorithm Part
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------

creating_new_file = raw_input("Do you want to generate a new file containing binary operation (Y/N) ?")
binary = BinaryOperation()
if creating_new_file == 'Y':
	filename = raw_input("Enter file's name: ")
	size = raw_input("Enter number of element (i.e enter 8 should give a binary operation table with size 8*8) :")
	size = int(size)
	binary.gen(filename, size)
	#binary.create_table(filename)
	#which_to_run = raw_input("Choose algorithm to run (type L for Light's algorithm/ type R for randomized algorithm: ")
	#if which_to_run == 'L':
	#	result = binary.is_associative()
	#	print(result)
	#else:
	#	result = binary.check_associative()
	#	print(result)
else:
	filename = raw_input("Enter an existing file containing a matrix: ")
	size = raw_input("Enter number of rows in the file: ")
	size = int(size)
	binary.size = size
	binary.create_table('./'+filename)
	print(binary.operation_table)
	which_to_run = raw_input("Choose algorithm to run (type L for Light's algorithm/ type R for randomized algorithm: ")
	if which_to_run == 'L':
		result = binary.is_associative()
		print(result)
	else:
		result = binary.check_associative()
		print(result)
