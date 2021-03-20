from hashlib import md5


def bruteforce(hash, dictonary):
	with open(dictonary, 'r', encoding='ISO-8859-1', newline='') as file:
		words = file.read().splitlines()

	for word in words:
		if hash == md5(bytearray(word, encoding='utf-8')).hexdigest():
			return word
			break
