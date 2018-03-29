from __future__ import division
from collections import Counter, defaultdict
import itertools
import time
import sys
import re
import os
import argparse

parser = argparse.ArgumentParser(prog = " bluebio codon program", \
                                usage = 'parses inputed amino acids. Please enter string of uppercase amino acids eg. AVI.')
parser.add_argument('-in', '--inputFile', required = True , \
                    help = 'amino acid input set, please enter string of upper case amino acids, eg. AVI')
args = parser.parse_args()
aa = args.inputFile

translation = {'TTT': 'F', 'TCT': 'S', 'TAT': 'Y', 'TGT': 'C',
                     'TTC': 'F', 'TCC': 'S', 'TAC': 'Y', 'TGC': 'C',
                     'TTA': 'L', 'TCA': 'S', 'TAA': '*', 'TGA': '*',
                     'TTG': 'L', 'TCG': 'S', 'TAG': '*', 'TGG': 'W',
                     'CTT': 'L', 'CCT': 'P', 'CAT': 'H', 'CGT': 'R',
                     'CTC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R',
                     'CTA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R',
                     'CTG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R',
                     'ATT': 'I', 'ACT': 'T', 'AAT': 'N', 'AGT': 'S',
                     'ATC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S',
                     'ATA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R',
                     'ATG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R',
                     'GTT': 'V', 'GCT': 'A', 'GAT': 'D', 'GGT': 'G',
                     'GTC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G',
                     'GTA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G',
                     'GTG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'
                     }

# nomenclature for degenerate codons
expanded_code = {'A': ['A'], 'C': ['C'], 'G': ['G'], 'T': ['T'],
                 'W': ['A', 'T'], 'S': ['C', 'G'], 'M': ['A', 'C'], 'K': ['G', 'T'], 'R': ['A', 'G'], 'Y': ['C', 'T'],
                 'B': ['C', 'G', 'T'], 'D': ['A', 'G', 'T'], 'H': ['A', 'C', 'T'], 'V': ['A', 'C', 'G'],
                 'N': ['A', 'C', 'G', 'T']
                 }

# helpful for validating input
valid_nucleotides = 'ACGTWSMKRYBDHVN'
valid_aa = 'GAVLIMFWPSTCYNQDEKRH*'


def get_codon_for_amino_acids(aa):

#get lists of input values
    v = list(aa)
    y = len(v)

#print input values of the amino acids given.
    print "\ninput list:\n", set(v), "\n"

#tranlates amino acids given.
    test = {codon:AA for codon, AA in translation.items() for \
    bb in v for aa in bb if AA == aa}

    x = defaultdict(list)

    for key, value in sorted(test.iteritems()):
        x[value].append(key)

#sepearte out test (translated amino acids) into 3 lists of codons/
    codon1 = []
    codon2 = []
    codon3 = []
    for key, value in x.items():
        C1, C2, C3 = zip(*value)
        codon1.append(tuple(C1))
        codon2.append(tuple(C2))
        codon3.append(tuple(C3))    

    
#flatten out lists of tuples for sing lists of all nucleotides in each codon.
    eCodon1 = [element for tupl in codon1 for element in tupl]
    eCodon2 = [element for tupl in codon2 for element in tupl]
    eCodon3 = [element for tupl in codon3 for element in tupl]

    
#counts the number of possible codons for each amino acid to be used 
#as a counter for finding the percent efficiency.
    percent = []
    for i in codon1:
        percent.append(len(i))
    smallest = min(percent)
    largest = max(percent)
    percentADD = "{0:.0f}%".format((smallest / largest)*100)


#removes non-efficient codons from test-list, searches expanded_code for 
#expanded codons and arranges them in seperate sets.
    for x in eCodon1:
        if eCodon1.count(x) < y:
            print eCodon1.remove(x)
            truth1 = {AA for AA, codon in expanded_code.items() for bb in \
            eCodon1 if x not in codon}
        else:
            truth1 = {AA for AA, codon in expanded_code.items() for bb in \
            sorted(list(set((eCodon1)))) if sorted(list(set((eCodon1)))) == codon}
    for x in eCodon2:
        if eCodon2.count(x) < y:
            eCodon2.remove(x)
            truth2 = {AA for AA, codon in expanded_code.items() for bb in \
            eCodon2 if x not in codon}
        else:
            truth2 = {AA for AA, codon in expanded_code.items() for bb in \
            sorted(list(set((eCodon2)))) if sorted(list(set((eCodon2)))) == codon}    
    for x in eCodon3:
        if eCodon3.count(x) < y:
            eCodon3.remove(x)
            truth3 = {AA for AA, codon in expanded_code.items() for bb in \
            eCodon3 if x not in codon}
        else:
            truth3 = {AA for AA, codon in expanded_code.items() for bb in \
            sorted(list(set((eCodon3)))) if sorted(list(set((eCodon3)))) == codon}    
    

#rearanges data for presentation, adds percent efficiency.
    final = list(itertools.product(truth1, truth2, truth3))
    end1 = [''.join(p) for p in final]
    end2 = set(end1)

    print "set of most efficient codons:\n", [end2, percentADD], "\n"
    


def truncate_list_of_amino_acids(aa):

    """
    :param amino_acids: set
        the amino acids we want to code for, i.e. {'A','I','V'}
    :return: set
        the set of sets of amino acids that can be coded with 100% efficiency, i.e. {frozenset({'V', 'A'}), frozenset({'V', 'I'})}
    """

    pass


if __name__ == "__main__":

    get_codon_for_amino_acids(aa)