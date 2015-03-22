import math


numwords = [
	[
		'',
		'one',
		'two',
		'three',
		'four',
		'five',
		'six',
		'seven',
		'eight',
		'nine',
	],
	[
		'',
		'',
		'',
		'',
		'',
		'',
		'',
		'',
		'',
		'',
		'ten',
		'eleven',
		'twelve',
		'thirteen',
		'fourteen',
		'fifteen',
		'sixteen',
		'seventeen',
		'eighteen',
		'nineteen',
	],
	[
		'',
		'',
		'twenty',
		'thirty',
		'forty',
		'fifty',
		'sixty',
		'seventy',
		'eighty',
		'ninety',
	]
]
numprefs = [
	'thousand',
	'million'
]

def num_to_words(num):
	words = []
	pref_count = 0;


	# group numbers into 3
	groups = format(num, ",").split(",")
	num_groups = len(groups)

	# iterate through each group
	for g in groups:
		num_hundred = 0
		tmp_num = int(g)
		num_groups = num_groups - 1

		# if this group is zero, append empty word
		if int(g)==0:
			continue

		# if hundreds, add the hundred word
		if int(g) >= 100:
			num_hundred = int( g[0] + '00' )
			words.append( numwords[0][int(g[0])] + ' hundred' )
			tmp_num = int(g) - num_hundred

		# add and if number is less than a hundred and preceding another word
		if len(words)>0 and tmp_num>0:
			words.append('and')

		# if greater than 19, add the twenties, thirties etc. word
		if tmp_num > 19:
			num_ten = int( math.floor( tmp_num/10 ) * 10 )
			words.append( numwords[2][ num_ten/10 ] )
			tmp_num = tmp_num - num_ten

		# if less than 19 but greater than 9, add the teens word
		if tmp_num<=19 and tmp_num>9:
			words.append( numwords[1][tmp_num] )

		# add the ones word
		if tmp_num<9 and tmp_num>0:
			words.append( numwords[0][tmp_num] )

		# add the thousands, millions word
		if num_groups >= 1:
			# print( 'num_groups: ' + str(tmp_num) )
			words.append(numprefs[num_groups-1])


	print(words)

def main():
	num_to_words(1203450)

if __name__ == '__main__':
	main()