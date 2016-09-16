from sys import argv
from random import randint
class BinaryOperation:
	def __init__(self):
		self.operation_table = []
		self.size = 0

	def generate_binary_opertion(self, filename, n):
		#Create a binary operation table of with number of element n 
		#The table of size n x n
		#And save the table in the file 'filename'
		#The table contains only integer form 1 to n
		column = 1
		row = 1
		target = open(filename, "w")
		while row <= n: 
			while column <= n:
				target.write(str(randint(1, n)))
				target.write(" ")
				column = column + 1
			target.write("\n")
			column = 1
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

	#def is_associative(self):
		#Check a binary opertation whether it is associative using Light's algorithm


filename = raw_input("Enter file's name: ")
n = raw_input("Enter number of element of the binary operation: ")
n = int(n)

binary = BinaryOperation()
binary.generate_binary_opertion(filename, n)
binary.create_table(filename)
print(binary.operation_table)
