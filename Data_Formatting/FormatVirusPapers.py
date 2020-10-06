#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 01:18:14 2020

@author: anibaljt
"""

import pickle

'''
sample tuple structure:
    
(id, title, publication_date, journal, authors, countries, abstract,full_text)
  
'''


def format_virus_papers(downsample=None):
    
    vdata = pickle.load(open('viruspapers.pkl','rb'))
    all_tuples = []
    allpapers = []
    alltitles = []
    j = 0

    for i,paper in enumerate(vdata):
        if paper not in allpapers:
            allpapers.append(paper)
            content = vdata[paper]['full-text-retrieval-response']
        else:
            continue

        if content['coredata']['dc:title'] == None:
            continue
    
        if content['coredata']['dc:title'] in alltitles:
            continue
        else:
            alltitles.append(content['coredata']['dc:title'])

        if 'dc:creator' not in content['coredata']:
            continue
    
        if content['coredata']['dc:creator'] == None:
            continue
    
        if content['coredata']['dc:description'] == None:
            continue


    
        tup = (content['coredata']['dc:identifier'].lower(),)
        tup += (content['coredata']['dc:title'].lower(),)
        tup += (content['coredata']['dc:description'],)
        date = vdata[paper]['pubdate'].split('-')
        tup += (date[0],date[1],date[2],)
        tup += (vdata[paper]['journal'],)
    
        authors = ""
        if type(content['coredata']['dc:creator']) == list:
            for auth in content['coredata']['dc:creator']:
                authors += (auth['$'] + " ").lower()
        else:
            content['coredata']['dc:creator']["$"]
        
        tup += (authors.lower(),)
        tup += (vdata[paper]['countries'],)

        if type(content['originalText']) == str and len(content['originalText']) > 0:
            tup += (content['originalText'].lower(),)
        else:
            continue

        j+=1
        print(j)
        all_tuples.append(tup)

        if downsample is not None:
            if j >= downsample:
                break

    pickle.dump(all_tuples,open("viruspapertuples.pkl","wb"))    



def main():
    format_virus_papers(downsample=1000)
    
    
if __name__ == '__main__':
    main()
    