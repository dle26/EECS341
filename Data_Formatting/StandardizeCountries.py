#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 00:31:51 2020

@author: anibaljt
"""

import pandas as pd
import pickle


def standardize_country_names_virus():
    
    c19 = pickle.load(open('viruspapertuples.pkl','rb'))

    countries = pd.read_csv('countries.csv')

    all_countries = []
    for tup in c19:
        all_countries.append(tup[8])
        

    newc = []
    allnewtup = []
    for n,country in enumerate(all_countries):
        newc = []
        if country is not None:
            for c in list(countries.index):
                if country.find(countries.loc[c]['country'].lower()) > -1:
                    newc.append(countries.loc[c]['country'].lower())
                           
                if len(newc) == country.split(','):
                    break
        
            if country.find('usa') > -1:
                newc.append('united states')
    
            if country.find('taiwan') > -1:
                newc.append('taiwan')
    
            if country.find('reunion') > -1:
               newc.append('reunion island')
    

            if country.find('uk') > -1:
                newc.append('united kingdom')
    
            if country.find('brasil') > -1:
                newc.append('brazil')

            
            tup = (c19[n][0],)
            for i in range(1,len(c19[n])):
                if i != 6:
                    tup += (c19[n][i],)
      
                else:
                    update = ""
                    for item in list(set(newc)):
                        update += (item + ", ")
                    if update != "":
                        print(update)
                    tup += (update,)
                allnewtup.append(tup)

        else:
             allnewtup.append(c19[n])
      
    pickle.dump(allnewtup,open('viruspapertuples.pkl','wb'))
      
        
def standardize_covid_names_virus():
   '''
   all_countries = []
   for tup in v:
   all_countries.append(tup[5])
   all_countries = list(set(all_countries))

   '''
   pass

def main():
    standardize_country_names_virus()

    
    
if __name__ == "__main__":
        main()