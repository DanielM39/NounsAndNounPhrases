#! python3.9
from sys import argv
import Nouns

blob = Nouns.parse(argv)

if blob is not None:
	for noun in Nouns.remove_duplicates(blob.noun_phrases):
		if (noun.strip().lower() not in Nouns.EXCLUTIONS) and (not noun.strip().isnumeric()):
			print(noun.title())