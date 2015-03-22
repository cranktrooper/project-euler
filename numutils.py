
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
	print(groups)

	for g in groups:
		tmp = 0

		# if this group is zero, append empty word
		if int(g)==0:
			words.append('')
			continue

		num_hundred = int( g[0] + '00' )
		print(num_hundred)
		if num_hundred >= 100:
			words.append( numwords[0][int(g[0])] + ' hundred' )
			tmp = int(g) - num_hundred

		if tmp==0:
			continue

		if tmp > 19:
			words.append( numwords[2][int(g[1])] )

		if tmp <= 19 and tmp > 9:
			words.append( numwords[1][int(g[1]+g[2])] )

		if tmp <= 9:
			words.append( numwords[0][int( tmp )] )

		if num_groups > 1:
			words.append(numprefs[num_groups-2])
			num_groups = num_groups - 1


	print(words)

def main():
	num_to_words(5095001)

if __name__ == '__main__':
	main()