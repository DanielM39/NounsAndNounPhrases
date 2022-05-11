#! python3.9
from textblob import TextBlob
from sys import argv

EXCLUTIONS = ["preconditions", "post-conditions", "scenario", "actor", "yyyy/mm/dd", "extensions", "merges", "step",
	"case document name", "alternative path" "ui actions", "primary actor", "customer stakeholders", "main success",
	"basic flow", "business layer", "system response", "case diagram", "main scenario", "alternative flows", 
	"alternative path", "scenario branches"]

def remove_duplicates(words):
	return list(dict.fromkeys(words))

if len(argv) > 1:
	txt = ""
	with open(argv[1], 'r', encoding='utf8') as f:
		for line in f:
			txt = txt + ' ' + line
	blob = TextBlob(txt)
	
	i = 1
	print("Nouns:")
	for noun in remove_duplicates(blob.noun_phrases):
		if (' ' not in noun) and (noun not in EXCLUTIONS):
			print("\t%d: %s" % (i,noun))
			i = i + 1
	print("Noun Phrases:")
	for nounP in remove_duplicates(blob.noun_phrases):
		if (' ' in nounP) and (nounP not in EXCLUTIONS):
			print("\t%d: %s" % (i,nounP))
			i = i + 1
else:
	print("Usage:\n\t %s input.txt" % argv[0].split('\\')[-1])