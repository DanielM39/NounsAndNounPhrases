#! python3.9
from textblob import TextBlob
from sys import argv

if len(argv) > 1:
	txt = ""
	with open(argv[1], 'r', encoding='utf8') as f:
		for line in f:
			txt = txt + ' ' + line
	blob = TextBlob(txt)
	
	i = 1
	print("Nouns:")
	for noun in blob.noun_phrases:
		if ' ' not in noun:
			print("\t%d: %s" % (i,noun))
			i = i + 1
	print("Noun Phrases:")
	for nounP in blob.noun_phrases:
		if ' ' in nounP:
			print("\t%d: %s" % (i,nounP))
			i = i + 1
else:
	print("Usage:\n\t %s input.txt" % argv[0].split('\\')[-1])