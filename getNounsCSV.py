#! python3.9
from sys import argv
import Nouns

blob = Nouns.parse(argv)

if blob is not None:
	with open("{}csv".format(argv[1].replace(argv[1].split('.')[-1],'')), 'w', encoding="utf8") as csv:
		csv.write("Noun,Meaning,Class?,Reason\n")
		for noun in Nouns.remove_duplicates(blob.noun_phrases):
			if (noun.strip().lower() not in Nouns.EXCLUTIONS) and (not noun.strip().isnumeric()):
				csv.write("{}\n".format(noun.title()))