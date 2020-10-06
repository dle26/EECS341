#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:49:06 2020

@author: anibaljt
"""

import pandas as pd
import pickle
import numpy as np

#### formatting case data
'''
tuple

EVENT_NAME
DATE_REPORTED
DATE_TYPE
ALO_NAME
AL1_NAME
LOCATION_TYPE
CONFIRM_STATUS
OUTCOME

'''


def format_cases(downsample = None):

    cases = pd.read_csv('cases.csv')
    all_tuples = []
    idn = 0
    for n,index in enumerate(list(cases.index)):
        if type(cases['EVENT_NAME'].values[n]) in [str,int] and type(cases['DATE_REPORT'].values[n]) in [str,int]:
            tup = (idn,)
            tup += (cases['AL0_NAME'].values[n].lower(),)
            date = cases['DATE_REPORT'].values[n].split('-')
            tup += (int(date[0]),int(date[1]),int(date[2]),)
            idn += 1
        else:
            continue

        tup += (cases['DATE_TYPE'].values[n].lower(),)

        tup += (cases['LOCATION_TYPE'].values[n].lower(),) 
        tup += (cases['CONFIRM_STATUS'].values[n].lower(),) 
        tup += (cases['VALUE'].values[n],) 
        tup += (cases['OUTCOME'].values[n].lower(),) 
    
        all_tuples.append(tup)
    
        if downsample is not None:
            if n > downsample:
                break
    
    pickle.dump(all_tuples,open("casetuples.pkl","wb"))



def format_measures():
    
    measures = pd.read_csv('measures.csv')
    all_tuples = []
    idn = 0
    for n,index in enumerate(list(measures.index)):
        if type(measures['COUNTRY'].values[n]) in [str,int] and type(measures['CATEGORY'].values[n]) in [str,int]:
            tup = (idn,)
            tup += (measures['COUNTRY'].values[n].lower(),)
            tup += (measures['CATEGORY'].values[n].lower(),)
            idn += 1
        else:
            continue
    

        tup += (measures['MEASURE'].values[n].lower(),)


        if type(measures['COMMENTS'].values[n]) in [str,int]:
            tup += (measures['COMMENTS'].values[n].lower(),)
        else:
            tup += (None,)
        
            
        if type(measures['SOURCE_TYPE'].values[n]) in [str,int]:
            tup += (measures['SOURCE_TYPE'].values[n].lower(),)
        else:
            tup += (None,)
        
     
        if type(measures['DATE_IMPLEMENTED'].values[n]) in [str,int]:
            date = measures['DATE_IMPLEMENTED'].values[n].split("/")
            tup += (date[2],date[0],date[1],)
        else:
            tup += (None,None,None)
        all_tuples.append(tup)

    pickle.dump(all_tuples,open("measuretuples.pkl","wb"))    



def format_countries():
    countries = pd.read_csv('countries.csv')
    allcountries = []
    all_tuples = []
    exclude = ['country','region','publicplace','alpha3code','alpha2code','gatheringlimit','gathering','nonessential',
           'healthexp','healthperpop','fertility','avghumidity','recovered','totalcases']

    for n,index in enumerate(list(countries.index)):
        if countries['country'].loc[index] not in allcountries:
            tup = (countries['country'].loc[index].lower(),)
            allcountries.append(countries['country'].loc[index])
            for col in countries.columns:
                if col not in exclude and col.find('death') == -1 and col.find('active') == -1 and col.find('new') == -1 and col.find('critical') == -1 and col.find('div') == -1:
                    if type(countries[col].loc[index]) in [str,int,np.float64]:
                        if type(countries[col].loc[index]) == np.float64:
                            if not np.isnan(countries[col].loc[index]):
                                tup += (countries[col].loc[index],)
                            else:
                                tup += (None,)
                        else:
                            if type(countries[col].loc[index]) is not int:
                                tup += (countries[col].loc[index].lower(),)
                
                    else:
                         tup += (None,)
                        
        #print(tup)
        all_tuples.append(tup)

    pickle.dump(all_tuples,open("countrytuples.pkl","wb"))    

 
    
def main():
   # format_cases(downsample=None)
   # format_measures()
   format_countries()
    
    
    
if __name__ == '__main__':
    main()
    