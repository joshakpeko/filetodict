#!/usr/bin/env python3
# -*- coding: utf8 -*-

"""ftodconv (file to dict converter) performs transfer of terms and
their definitions found in file, into python dictionary object."""

import json

def ftodict(ifile):
    """save ifile content into a dictionary object and return that
    dictionary."""
    dico = {}
    with open(ifile, 'r', encoding='utf8') as src:
        term_elmt = []   # term elements : term, explanation, examples
        for line in src:
            if line != '\n':
                term_elmt.append(line)
            elif term_elmt:
                # complete with None if some elements are missing
                while len(term_elmt) < 3:
                    term_elmt.append(None)
                term, explan, examp = term_elmt
                try:
                    term = term.strip()
                except AttributeError:  # in case it is None
                    pass
                try:
                    explan = explan.strip()
                except AttributeError:
                    pass
                try:
                    examp = examp.replace(' and', ',')
                    examp = examp.strip('Examples:')
                    examp = [ex.strip() for ex in examp.split(',')]
                except AttributeError:
                    pass
                dico[term] = {
                                'explanation': explan,
                                'examples': examp
                             }
                term_elmt = []      # reset for next sequence
    return dico

# convert animegenres.txt to dictionary object and save as json
if __name__ == '__main__':
    src = 'animegenres.txt'
    animedict = ftodict(src)
    animejson = json.dumps(animedict)
    destname = src.strip('.txt') + '.json'
    with open(destname, 'w') as dest:
        dest.write(animejson)
