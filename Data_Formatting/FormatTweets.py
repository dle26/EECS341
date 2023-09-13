#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:57:52 2020

@author: anibaljt
"""

### script for structuring .csv files for input into SQLite


import pandas as pd 
import numpy as np
import string
import pickle

''' 
Tweet:
   
tweet_ID
text
date
Time
country
User_name
Bio
Num_followers
Sentiment score
 
'''


    
def extract_time(word):
    

    for n,char in enumerate(word):
        if char == ':' and word[n-3] == ' ':
            index = n-3
            break
        elif char == ':' and word[n-2] == ' ':
            index = n-2
            break

    return (word[0:index][-2] + word[0:index][-1] + "-03-2020"),word[index+1:list(word).index('+')-1]



    
def extract_country(words):
    
    country_cities = pd.read_csv('cities.csv')
    lst = words.split()
    lst =  [word for word in lst if word not in string.punctuation]
   

    ### cities
    city_matches = list(set(country_cities['city']) &  set(lst))
    countries = []
    for city in city_matches:
        if list(country_cities['country'])[list(country_cities['city']).index(city)] not in countries:
            countries.append(list(country_cities['country'])[list(country_cities['city']).index(city)])
            
    ### states
    sub_matches = list(set(country_cities['subcountry']) &  set(lst))

    for csub in sub_matches:
        if list(country_cities['country'])[list(country_cities['subcountry']).index(csub)] not in countries:
            countries.append(list(country_cities['country'])[list(country_cities['subcountry']).index(csub)])
        

    country = list(set(country_cities['country']) &  set(lst))
    for c in country:
         if c not in countries:
            countries.append(c)
        
    
    country = ""

    #### only look at top 10 twitter countries
    if  len(list({'United States','Japan','United Kingdom','Saudi Arabia','Brazil','Turkey','India','Indonesia','Russia','Mexico'} & set(countries))) > 0:
        for c in list({'United States','Japan','United Kingdom','Saudi Arabia','Brazil','Turkey','India','Indonesia','Russia','Mexico'} & set(countries)):
            country += (c + ", ")
     
        return country
    return None
    



def format_tweets():

    hydrated = pd.read_csv('alltweets.csv')
    all_tuples = []
    alltext = []
    for n,index in enumerate(list(hydrated.index)):
        if type(hydrated['id'].values[n]) in [str,np.int64] and type(hydrated['text'].values[n]) in [str,np.int64]:
            tup = (int(hydrated['id'].values[n]),)
            tup += (hydrated['text'].values[n],)
            if hydrated['text'].values[n] in alltext:
                continue
            alltext.append(hydrated['text'].values[n])
        else:
            continue
    
        date,time = extract_time(hydrated['created_at'].values[n])
        date = date.split('-')
        time = time.split(':')

        tup += (int(date[2]),int(date[1]),int(date[0]),)
        tup += (int(time[0]),int(time[1]),)

    
        if type(hydrated['user_location'].values[n]) in [str,np.int64]:
            countries = extract_country(hydrated['user_location'].values[n])
            tup += (countries,)
        else:
            tup += (None,)
    
    
        if type(hydrated['user_screen_name.1'].values[n]) in [str,np.int64]:
            un =  ''.join((c for c in str(hydrated['user_screen_name.1'].values[n].lower()) if ord(c) < 128))
            tup += (un,)
        else:
            tup += (None,)
        
        if type(hydrated['user_description'].values[n]) in [str,np.int64]:
            un =  ''.join((c for c in str(hydrated['user_description'].values[n].lower()) if ord(c) < 128))
            tup += (un,)
        else:
            tup += (None,)
        
        if type(hydrated['user_followers_count'].values[n]) in [str,np.int64]:
            tup += (int(hydrated['user_followers_count'].values[n]),)
        else:
            tup += (None,)
        
        if type(hydrated['retweet_count'].values[n]) in [str,np.int64]:
            tup += (int(hydrated['retweet_count'].values[n]),)
        else:
            tup += (None,)
    
        tup += (float(hydrated['sentiment score'].values[n]),)
        all_tuples.append(tup)
 

    pickle.dump(all_tuples,open("tweettuples.pkl","wb"))    
    
    
    
    
def main():
    format_tweets()  
    
if __name__ == '__main__':
    main()
    
