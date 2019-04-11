#!/usr/bin/env python

import xml.etree.ElementTree as ET 
import argparse
import os


def main():
#######################
#parse arguments
	parser = argparse.ArgumentParser(description='Insert full sequences to a beast *.xml template file')
	parser.add_argument('-p', '--phylip', type=str, help='full path to phylip file', required=True)
	parser.add_argument('-t', '--template', type=str, help='full path to xml-template file', required=True)
	parser.add_argument('-o', '--outfile', type=str, help='Name of output file. Will be written in the location of phylip file', required=True)
	args = parser.parse_args()
	
	outpath = os.path.join(os.path.dirname(args.phylip), 'beast_' + args.outfile + '.xml')
	
	#phy2xml(args.phylip, args.template, outpath)
#####################
	# parse template xml file
	tree = ET.parse(args.template)
	root = tree.getroot()
	# iterate through tree to find alignment on a per taxon basis
	for seq in root.findall("./alignment/sequence/taxon"):
		# find all seq tags (key) and the taxon (value)
		for key, value in seq.attrib.items():
			#open alignment file
			with open(args.phylip, 'r') as phy:
				first = phy.readline()
				for line in phy:
					sample = line.split()[0]
					# find the sample in phy that matches the current taxon in the xml tree
					if sample == value:
						sequence = line.split()[1]
						# replace xml seq tag sequence with the phylip sequence
						seq.tail = sequence
	print('done')
	# write tree to file					
	tree.write(outpath)
	

if __name__ == '__main__':
	main()