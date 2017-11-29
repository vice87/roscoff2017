#!/usr/bin/python

'''
Translate a nucleotide sequence in input
in all its six reading frames
'''

import os
import sys


# translate triples of nucleotides in amino acids
translationTable = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'*', 'TAG':'*',
    'TGC':'C', 'TGT':'C', 'TGA':'*', 'TGG':'W'
}

# reverse complement of nucleotides
nt2rc = { 'A':'T', 'C':'G', 'G':'C', 'T':'A' }

def translateSequence(ntSeq):
    pass

def reverseComplement(ntSeq):
    pass

def main():
    argv = sys.argv

    # print input sequences reverse-complemented
    inputFasta = argv[1]
    with open(inputFasta,'r') as inputFile:
        for line in inputFile:
            line = line.strip()
            if line == "":
		continue

    return 0

# Check if the program is not being imported
if __name__ == "__main__":
    sys.exit(main())
