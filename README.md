# Install packages
```bash
pip install -U textblob python-docx
python -m textblob.download_corpora
```
# Run
### For output formatted in a numbered list split into Nouns, and Noun Phrases:
```bash
getNounsAndNounPhrases.py input.file
``` 
### For output as a single unnumbered list:
```bash
getNouns.py input.file
``` 
### For output as a csv:
```bash
getNounsCSV.py input.file
``` 
### Note:
`input.file` can be .docx, .doc (only on windows), or a plain text file (.txt)