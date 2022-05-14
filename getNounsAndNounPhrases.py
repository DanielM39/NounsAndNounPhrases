#! python3.9
from sys import argv
import Nouns

blob = Nouns.parse(argv)

if blob is not None:
	i = 1
	print("Nouns:")
	for noun in Nouns.remove_duplicates(blob.noun_phrases):
		if (' ' not in noun) and (noun.strip().lower() not in Nouns.EXCLUTIONS) and (not noun.strip().isnumeric()):
			print("\t%d: %s" % (i,noun))
			i = i + 1
	print("Noun Phrases:")
	for nounP in Nouns.remove_duplicates(blob.noun_phrases):
		if (' ' in nounP) and (nounP.strip().lower() not in Nouns.EXCLUTIONS) and (not nounP.strip().isnumeric()):
			print("\t%d: %s" % (i,nounP))
			i = i + 1