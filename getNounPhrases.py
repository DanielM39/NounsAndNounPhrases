#! python3.9
from textblob import TextBlob
from sys import argv

def remove_duplicates(words):
	return list(dict.fromkeys(words))

if len(argv) > 1:
	txt = ""
	with open(argv[1], 'r', encoding='utf8') as f:
		for line in f:
			txt = txt + ' ' + line
	blob = TextBlob(txt)
	#print(blob.noun_phrases)
	i = 1
	for nounP in remove_duplicates(blob.noun_phrases):
		print("%d: %s" % (i,nounP))
		i = i + 1