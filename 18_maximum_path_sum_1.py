import math

path = [
	[75],
	[95,64],
	[17,47,82],
	[18,35,87,10],
	[20,4,82,47,65],
	[19,1,23,75,3,34],
	[88,2,77,73,7,63,67],
	[99,65,4,28,6,16,70,92],
	[41,41,26,56,83,40,80,70,33],
	[41,48,72,33,47,32,37,16,94,29],
	[53,71,44,65,25,43,91,52,97,51,14],
	[70,11,33,28,77,73,17,78,39,68,17,57],
	[91,71,52,38,17,14,91,43,58,50,27,29,48],
	[63,66,4,68,89,53,67,30,73,16,69,87,40,31],
	[4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
]

path=[
	[0],
	[5,2],
	[5,6,10],
	[2,4,0,5],
	[7,7,1,1,10]
]

# path = [
# 	[1],
# 	[2,1],
# 	[1,1,20],
# 	[40,0,1,2],
# 	[0,0,0,100,0]
# ]
# path = [[1], [1, 20], [0, 1, 2], [0, 0, 100, 0]]
# path = [[20], [1, 2], [0, 100, 0]]
# path = [[2], [100, 0]]

moves = []
path_sum = []
brute_sums = []
brute_combi = []

def main():
	print('#################################################################################################################################')
	print('#################################################################################################################################')

	cmp_sides(path)
	print(moves)
	print(path_sum)
	print(sum(path_sum))

def cmp_sides(path):
	print('SUBJECT: ' + str(path))
	sum1 = 0
	sum2 = 0
	for i in range(0, len(path)):
		left_group = []
		right_group = []

		if isinstance(path[i], int):
			left_group = path[i]
			right_group = path[i]
			sum1 = sum1 + path[i]
			sum2 = sum2 + path[i]
		else:
			row_len = float(len(path[i]))
			row_midpoint = int( math.ceil(row_len/2) )
			last_index = int(row_len)

			if row_len==2:
				left_group = path[i][0]
				right_group = path[i][1]
				sum1 = sum1 + path[i][0]
				sum2 = sum2 + path[i][1]

			elif row_len>2:
				left_group = path[i][0:row_midpoint]

				if row_len%2==0:
					right_group = path[i][row_midpoint:last_index]
				else:
					right_group = path[i][row_midpoint-1:last_index]

				sum1 = sum1 + sum( left_group )
				sum2 = sum2 + sum( right_group )

		# print(left_group)
		# print(right_group)

	new_path = []
	if sum1>sum2:
		moves.append(-1)
		for i in range(1, len(path)):
			new_path.append( path[i][:-1] )
	else:
		moves.append(1)
		for i in range(1, len(path)):
			new_path.append( path[i][1:] )

	path_sum.append(new_path[0][0])
	print(new_path[0][0])

	if len(new_path)>1:
		cmp_sides(new_path)

# def get_sum_brute(path):
	# for i in range(0, len(path)):


if __name__ == '__main__':
	main()