#! python3.9
from sys import argv
import Nouns

blob = Nouns.parse(argv)

if blob is not None:
	i = 1
	for nounP in Nouns.remove_duplicates(blob.noun_phrases):
		if (nounP.strip().lower() not in Nouns.EXCLUTIONS) and (not nounP.strip().isnumeric()):
			print("%d: %s" % (i,nounP.title()))
			i = i + 1