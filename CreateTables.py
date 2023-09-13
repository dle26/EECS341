#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:05:49 2020

@author: anibaljt
"""

import sqlite3


def create_tables():
    
    conn = sqlite3.connect('test.db') 
    c = conn.cursor()


    ''' (ID, title, pub_date, journal, authors, countries,abstract,full_text,references) '''

    c.execute('''CREATE TABLE IF NOT EXISTS COVID19_PAPER
             ([ID] TEXT PRIMARY KEY,
             [title] TEXT UNIQUE NOT NULL,
             [abstract] TEXT UNIQUE NOT NULL,
             [pubyear] INTEGER DEFAULT -1,
             [pubmonth] INTEGER DEFAULT -1,
             [pubday] INTEGER DEFAULT -1,
             [journal] TEXT DEFAULT "N/A",
             [authors] TEXT DEFAULT "N/A",
             [countries] TEXT DEFAULT "N/A",
             [full_text] TEXT DEFAULT "N/A",
             [references] TEXT DEFAULT "N/A"
             FOREIGN KEY(countries) REFERENCES COUNTRY(name)
             )''')


    c.execute('''CREATE TABLE IF NOT EXISTS VIRUS_PAPER
             ([ID] TEXT PRIMARY KEY,
             [title] TEXT UNIQUE NOT NULL,
             [abstract] TEXT UNIQUE NOT NULL,
             [pubyear] INTEGER DEFAULT -1,
             [pubmonth] INTEGER DEFAULT -1,
             [pubday] INTEGER DEFAULT -1,
             [journal] TEXT DEFAULT "N/A",
             [authors] TEXT DEFAULT "N/A",
             [countries] TEXT DEFAULT "N/A",
             [full_text] TEXT DEFAULT "N/A"
             FOREIGN KEY(countries) REFERENCES COUNTRY(name)
             )''')
          
            
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
      
  
    c.execute('''CREATE TABLE IF NOT EXISTS COVID19_TWEET
             ([tweet_ID] INTEGER PRIMARY KEY,
             [tweet_text] TEXT UNIQUE NOT NULL,
             [tweet_year] INTEGER DEFAULT -1,
             [tweet_month] INTEGER DEFAULT -1,
             [tweet_day] INTEGER DEFAULT -1,
             [tweet_hour] INTEGER DEFAULT -1,
             [tweet_minute] INTEGER DEFAULT -1,
             [tweet_country] TEXT DEFAULT "N/A",
             [username] TEXT DEFAULT "N/A",
             [bio] TEXT DEFAULT "N/A",
             [numfollowers] INTEGER DEFAULT -1,
             [numretweets] INTEGER DEFAULT -1,
             [sentiment_score] REAL DEFAULT -1
             FOREIGN KEY(tweet_country) REFERENCES COUNTRY(name)
             )''')
         


    c.execute('''CREATE TABLE IF NOT EXISTS COVID19_MEASURE
             (
             [ID] INTEGER PRIMARY KEY,
             [country] TEXT NOT NULL,
             [category] TEXT NOT NULL, 
             [measure] TEXT NOT NULL,
             [comments] TEXT DEFAULT "N/A", 
             [source] TEXT DEFAULT "N/A",
             [implementation_year] INTEGER DEFAULT -1,
             [implementation_month] INTEGER DEFAULT -1,
             [implementation_day] INTEGER DEFAULT -1,
             FOREIGN KEY(country) REFERENCES COUNTRY(name)
             )''')
  


    c.execute('''CREATE TABLE IF NOT EXISTS COVID19_CASE
          
             (
             [ID] INTEGER PRIMARY KEY,
             [country] TEXT NOT NULL,
             [year] INTEGER NOT NULL,
             [month] INTEGER DEFAULT -1,
             [day] INTEGER DEFAULT -1,
             [method_of_discovery] TEXT DEFAULT "N/A",
             [source_of_confirmation] TEXT DEFAULT "N/A",
             [incidence_type] TEXT DEFAULT "N/A",
             [incidence_value] INTEGER DEFAULT -1,
             [outcome] TEXT DEFAULT "N/A",
             FOREIGN KEY(country) REFERENCES COUNTRY(name)
             )''')


    c.execute('''CREATE TABLE IF NOT EXISTS COUNTRY
             ([name] TEXT PRIMARY KEY,
             [population] TEXT DEFAULT "N/A",
             [total_tests] TEXT DEFAULT "N/A", 
             [test_population] TEXT DEFAULT "N/A",
             [density] REAL DEFAULT -1,
             [median_age] REAL DEFAULT -1,
             [urban_pop] REAL DEFAULT -1,
             [quarantine_start_date] TEXT DEFAULT "N/A",
             [school_close_date] TEXT DEFAULT "N/A",
             [hospitalbeds] REAL DEFAULT "N/A",
             [smokers] REAL DEFAULT "N/A", 
             [sex_ratio_birth]  REAL DEFAULT -1,
             [sex_ratio_0-13]  REAL DEFAULT -1,
             [sex_ratio_14-24]  REAL DEFAULT -1,
             [sex_ratio_25-53]  REAL DEFAULT -1,
             [sex_ratio_54-64]  REAL DEFAULT -1,
             [sex_ratio_65plus]  REAL DEFAULT -1,
             [sexratio]  REAL DEFAULT -1,
             [lung_disease]  REAL DEFAULT -1,
             [lung_female] REAL DEFAULT -1,
             [lung_male]  REAL DEFAULT -1,
             [gdp] REAL DEFAULT -1,
             [avg_temp]  REAL DEFAULT -1,
             [first_case] TEXT DEFAULT "N/A"
             )''')
                  

    c.execute('''CREATE TABLE IF NOT EXISTS PAPER_COMPARISON (
                        [ID] INTEGER PRIMARY KEY,
                        [covid_title] TEXT NOT NULL,
                        [virus_title] TEXT NOT NULL,
                        [abstract_shared_keywords] TEXT DEFAULT "N/A",
                        [abstract_shared_bigrams] TEXT DEFAULT "N/A",
                        [fulltext_shared_keywords] TEXT DEFAULT "N/A",
                        [fulltext_shared_bigrams] TEXT DEFAULT "N/A",
                        FOREIGN KEY(covid_title) REFERENCES COVID19_PAPER(title),
                        FOREIGN KEY(virus_title) REFERENCES VIRUS_PAPER(title)
                        )''')


    c.execute('''CREATE TABLE IF NOT EXISTS COVID19_PAPER_COMPARISON (
            [ID] INTEGER PRIMARY KEY,
            [covid_title1] TEXT NOT NULL,
            [covid_title2] TEXT NOT NULL,
            [abstract_shared_keywords] TEXT DEFAULT "N/A",
            [abstract_shared_bigrams] TEXT DEFAULT "N/A",
            [fulltext_shared_keywords] TEXT DEFAULT "N/A",
            [fulltext_shared_bigrams] TEXT DEFAULT "N/A",
            FOREIGN KEY(covid_title1) REFERENCES COVID19_PAPER(title),
            FOREIGN KEY(covid_title2) REFERENCES COVID19_PAPER(title)
    )''')


    c.execute('''CREATE TABLE IF NOT EXISTS VIRUS_PAPER_COMPARISON (
    [ID] INTEGER PRIMARY KEY,
    [virus_title1] TEXT NOT NULL,
    [virus_title2] TEXT NOT NULL,
    [abstract_shared_keywords] TEXT DEFAULT "N/A",
    [abstract_shared_bigrams] TEXT DEFAULT "N/A",
    [fulltext_shared_keywords] TEXT DEFAULT "N/A",
    [fulltext_shared_bigrams] TEXT DEFAULT "N/A",
    FOREIGN KEY(virus_title1) REFERENCES VIRUS_PAPER(title),
    FOREIGN KEY(virus_title2) REFERENCES VIRUS_PAPER(title)
    )''')



    c.execute('''CREATE TABLE IF NOT EXISTS TWEET_PAPER_COMPARISON (
                        [ID] INTEGER PRIMARY KEY,
                        [covid_title] TEXT NOT NULL,
                        [tweetid] TEXT NOT NULL,
                        [shared_keywords] TEXT DEFAULT "N/A",
                        FOREIGN KEY(covid_title) REFERENCES COVID19_PAPER(title),
                        FOREIGN KEY(tweet_ID) REFERENCES COVID19_TWEET(tweet_ID)
                        )''')
    
    

    conn.commit()

    
def main():
    create_tables()
    
    
if __name__ == '__main__':
    main()
    


