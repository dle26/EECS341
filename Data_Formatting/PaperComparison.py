#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:14:14 2020

@author: anibaljt
"""


import nltk
import pickle
import string



def extract_keywords(text): 
    
    words =  nltk.word_tokenize(text) 
    words = [word.lower() for word in words if word not in string.punctuation or word == '.']
    tagged_words = nltk.pos_tag(words)
    search_words = []
    
    for n,word in enumerate(tagged_words):
        if n < len(tagged_words)-1:
            if (word[1][0] == 'N' and tagged_words[n+1][1][0] == 'J') or (word[1][0] == 'N' and tagged_words[n+1][1][0] == 'N'):
                if len(word[0]) < 50 and len(tagged_words[n+1][0]) < 50:
                    if word[0] + " " + tagged_words[n+1][0] not in search_words:
                        search_words.append(word[0] + " " + tagged_words[n+1][0])
            if (word[1][0] == 'NNP' and tagged_words[n+1][1][0] == 'J') or (word[1][0] == 'NNP' and tagged_words[n+1][1][0] == 'N'):
                if len(word[0]) < 50 and len(tagged_words[n+1][0]) < 50:
                    if word[0] + " " + tagged_words[n+1][0] not in search_words:
                        search_words.append(word[0] + " " + tagged_words[n+1][0])
        bigram = True

        if (word[1][0] == 'NNP') and word[0].find('data') == -1 and not bigram:
            if word[0] not in search_words:
                search_words.append(word[0])
        
        
        bigram = False
        
        
    return search_words
 
    
def extract_string(words):
    
    similarities = ""
    bigrams = ""
    for word in words:
        if len(word.split()) > 1:
            similarities +=word + ", "
            bigrams +=word + ", "
    
    return similarities,bigrams
    


def compare_covid_virus_paper(downsample=None):
    
    covidpaper = pickle.load(open('covidpapertuples.pkl','rb'))
    viruspaper = pickle.load(open('viruspapertuples.pkl','rb'))

    all_tuples = []
    ind = 0

    for n,tup in enumerate(covidpaper):
          for nn,tup1 in enumerate(viruspaper):
            if tup[1] != tup1[1] and tup1[1] != 'authors':
                entry = (ind,tup[1],tup1[1],)
                ind+=1
                abstextlist1  = extract_keywords(tup[2])
                abstextlist2 = extract_keywords(tup1[2])
                comparison = list(set(abstextlist1) & set(abstextlist2))
                wordresult,bigramresult = extract_string(comparison)
                entry += (wordresult,)
                entry += (bigramresult,)
        
            fulltextlist1  = extract_keywords(tup[7])
            fulltextlist2 = extract_keywords(tup1[7])
            comparison = list(set(fulltextlist1) & set(fulltextlist2))
            wordresult,bigramresult = extract_string(comparison)
            entry += (wordresult,)
            entry += (bigramresult,)
            all_tuples.append(entry)
            if downsample is not None:
                if nn > downsample:
                    break
          if downsample is not None:
            if n > downsample:
                break
    
    pickle.dump(all_tuples,open("papercomparison.pkl","wb"))
    
    
    

def virus_compare(downsample=None):

    viruspaper = pickle.load(open('viruspapertuples.pkl','rb'))

    all_tuples = []
    ind = 0
    jj=0
    for n,tup in enumerate(viruspaper):
        k = 0
        for nn,tup1 in enumerate(viruspaper[n:len(viruspaper)]):
            if tup[1] != tup1[1] and tup1[1] != 'authors':
                entry = (ind,tup[1],tup1[1],)
                ind+=1
                abstextlist1  = extract_keywords(tup[2])
                abstextlist2 = extract_keywords(tup1[2])
                comparison = list(set(abstextlist1) & set(abstextlist2))
                wordresult,bigramresult = extract_string(comparison)
                entry += (wordresult,)
                entry += (bigramresult,)
                fulltextlist1  = extract_keywords(tup[7])
                fulltextlist2 = extract_keywords(tup1[7])
                comparison = list(set(fulltextlist1) & set(fulltextlist2))
                wordresult,bigramresult = extract_string(comparison)
                entry += (wordresult,)
                entry += (bigramresult,)
                all_tuples.append(entry)
                k += 1
            if downsample is not None:
                if k > downsample:
                    break
        jj+=1
        if downsample is not None:
            if jj > downsample:
                break
        
    pickle.dump(all_tuples,open("viruspapercomparison.pkl","wb"))



def tweet_paper_compare(downsample=None):
    
    covidpaper = pickle.load(open('covidpapertuples.pkl','rb'))
    tweets = pickle.load(open('tweettuples.pkl','rb'))
    
    all_tuples = []
    ind = 0
    jj = 0
    for n,tup in enumerate(covidpaper):
      k = 0
      if tup[1] != 'authors':
         for nn,tup1 in enumerate(tweets):
            entry = (ind,tup[1],tup1[0],)
            ind += 1
            textlist1  = extract_keywords(tup[1])
            textlist2 = extract_keywords(tup1[1])
            comparison = list(set(textlist1) & set(textlist2))
            wordresult,_ = extract_string(comparison)
            entry += (wordresult,)
            print(entry)
            all_tuples.append(entry)
            k += 1
            if downsample is not None:
                if k > downsample:
                    break
         jj+=1 
         if downsample is not None:
            if jj > downsample:
                break
      
    pickle.dump(all_tuples,open("tweetcomaparisontuples.pkl","wb"))



def compare_covid_to_covid(downsample=None):
    covidpaper = pickle.load(open('covidpapertuples.pkl','rb'))
    all_tuples = []
    ind = 0
    jj=0

    for n,tup in enumerate(covidpaper):
       k = 0
       if tup[1] != 'authors':
        for nn,tup1 in enumerate(covidpaper[n:len(covidpaper)]):
            if tup[1] != tup1[1] and tup1[1] != 'authors':
                entry = (ind,tup[1],tup1[1],)
                ind+=1
                abstextlist1  = extract_keywords(tup[2])
                abstextlist2 = extract_keywords(tup1[2])
                comparison = list(set(abstextlist1) & set(abstextlist2))
                wordresult,bigramresult = extract_string(comparison)
                entry += (wordresult,)
                entry += (bigramresult,)
                fulltextlist1  = extract_keywords(tup[7])
                fulltextlist2 = extract_keywords(tup1[7])
                comparison = list(set(fulltextlist1) & set(fulltextlist2))
                wordresult,bigramresult = extract_string(comparison)
                entry += (wordresult,)
                entry += (bigramresult,)
                all_tuples.append(entry)
                k += 1
            
            if downsample is not None:
                if k > downsample:
                    break
        jj += 1
        if downsample is not None:
           if jj > downsample:
               break
           
    pickle.dump(all_tuples,open("covidpapercomparison.pkl","wb"))
    




def main():
    compare_covid_virus_paper(downsample=100)
    virus_compare(downsample=100)
    tweet_paper_compare(downsample=100)
    compare_covid_to_covid(downsample=100)
    
    
    
if __name__ == '__main__':
    main()
        
           