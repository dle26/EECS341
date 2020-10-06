#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:21:50 2020

@author: anibaljt
"""


import sqlite3
import pickle



def insert_data():

    conn = sqlite3.connect('test.db') 
    c = conn.cursor()
    c19papers = pickle.load(open('covidpapertuples.pkl','rb')) 
    print(len(c19papers))

    query = '''INSERT INTO COVID19_PAPER VALUES (?,?,?,?,?,?,?,?,?,?,?)'''
    c.executemany(query,c19papers)
    conn.commit()

    vpapers = pickle.load(open('viruspapertuples.pkl','rb'))
    print(len(vpapers))
    query = '''INSERT INTO VIRUS_PAPER VALUES (?,?,?,?,?,?,?,?,?,?)'''
    c.executemany(query,vpapers)
    conn.commit()
    
    tweets = pickle.load(open('tweettuples.pkl','rb'))
    print(len(tweets))
    query = '''INSERT INTO COVID19_TWEET VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    c.executemany(query,tweets)
    conn.commit()


    measures = pickle.load(open('measuretuples.pkl','rb'))
    query = '''INSERT INTO COVID19_MEASURE VALUES (?,?,?,?,?,?,?,?,?)'''
    c.executemany(query,measures)
    conn.commit()

    cases = pickle.load(open('casetuples.pkl','rb'))
    for i in cases[0]:
        print(type(i))
    query = '''INSERT INTO COVID19_CASE VALUES (?,?,?,?,?,?,?,?,?,?)'''
    c.executemany(query,cases)
    conn.commit()

    
    country = pickle.load(open('countrytuples.pkl','rb'))
    print(len(country[0]))
    query = '''INSERT INTO COUNTRY VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
    c.executemany(query,country)
    conn.commit()

    comparison = pickle.load(open('papercomparison.pkl','rb'))
    all_c = []
    for tup in comparison:
        newtup = (int(tup[0]),)
        newtup += tup[1:len(tup)]
        all_c.append(newtup)

    query = '''INSERT INTO PAPER_COMPARISON VALUES (?,?,?,?,?,?,?)'''
    c.executemany(query,all_c)

    comparison = pickle.load(open('covidpapercomparison.pkl','rb'))
    all_c = []
    for tup in comparison:
        newtup = (int(tup[0]),)
        newtup += tup[1:len(tup)]
        all_c.append(newtup)

    query = '''INSERT INTO COVID19_PAPER_COMPARISON VALUES (?,?,?,?,?,?,?)'''
    c.executemany(query,all_c)
    


    comparison = pickle.load(open('viruspapercomparison.pkl','rb'))
    all_c = []
    for tup in comparison:
        newtup = (int(tup[0]),)
        newtup += tup[1:len(tup)]
        all_c.append(newtup)

    query = '''INSERT INTO VIRUS_PAPER_COMPARISON VALUES (?,?,?,?,?,?,?)'''
    c.executemany(query,all_c)

    comparison = pickle.load(open('tweetcomaparisontuples.pkl','rb'))
    all_c = []
    for tup in comparison:
        newtup = (int(tup[0]),)
        newtup += tup[1:len(tup)]
        all_c.append(newtup)

    query = '''INSERT INTO TWEET_PAPER_COMPARISON VALUES (?,?,?,?)'''
    c.executemany(query,all_c)
    conn.commit()


    
def main():
    insert_data()
    
    
if __name__ == '__main__':
    main()
    





