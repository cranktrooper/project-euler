import numutils

def main():
	words = ''

	for i in range(1,1001):
		words = words + numutils.num_to_words(i)
		# print( numutils.num_to_words(i) )

	print( len(words.replace(" ","")) )

if __name__ == '__main__':
	main()