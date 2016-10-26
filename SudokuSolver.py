
import csv, math

grid = []
row1 = []
with open('easy_sudoku.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		#if len(row) == 9:
			#row1.append(row)
		print row
			
print ("hello world")
