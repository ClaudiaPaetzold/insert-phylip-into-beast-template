# insert-phylip-into-beast-template

Python script inserting phylip files, that are too big for beauti to handle into a beast xml template file

This script was originally designed, because my RADSeq dataset was to big to be loaded by the BEAST helper 
program BEAUTi (Drummond & Rambaut, 2007).


# Command line Usage

```
>>> python insert_phy2xml.py -h

usage: insert_phy2xml.py [-h] -p PHYLIP -t TEMPLATE -o OUTFILE

Insert full sequences to a beast *.xml template file

optional arguments:
  -h, --help            show this help message and exit
  -p PHYLIP, --phylip PHYLIP
                        full path to phylip file
  -t TEMPLATE, --template TEMPLATE
                        full path to xml-template file
  -o OUTFILE, --outfile OUTFILE
                        Name of output file. Will be written in the location
                        of phylip file
```

# Important

This code does not come with a beast *.xml template file. The User has to create this using a small alignment. 
This alignment **_must_** contain the same taxa as the "real" alignment using identical identifiers.

# Please note

This code is not intended to work with partitions. It is explicitly designed to handle **concatenated datasets only**!

