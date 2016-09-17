from sys import argv
from random import randint
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
		n = self.size
		subtable = [[0 for x in xrange(n)] for y in xrange(n)] 
		for x in xrange(0, n):
			val = self.operation_table[i][x]
			for m in xrange(0, n):
				subtable[m][x] = self.operation_table[m][val]
		return subtable


binary = BinaryOperation()
binary.size = 5
binary.create_table('la.txt')
ass = binary.is_associative()
print(ass)
print("\n")
