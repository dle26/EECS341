#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Created on Fri Apr 10 23:02:28 2020

@author: anibaljt
"""


import json
from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch
from elsapy.elsdoc import AbsDoc
import requests
import pickle



def execute_modified(uri,els_client = None,set_limit=25):

    api_response = els_client.exec_request(uri)
    results = api_response['search-results']['entry']

    i = 0
    while i<(int(set_limit/25)-1):
       for e in api_response['search-results']['link']:
           if e['@ref'] == 'next':
               next_url = e['@href']
       api_response = els_client.exec_request(next_url)
       results += api_response['search-results']['entry']
       i+=1

    return results
    
  
def get_countries(data):
    
    
   countries = ""
   if 'affiliation' in data:
       if type(data['affiliation']) == dict:
           if data['affiliation']['affiliation-country'] != None:
               if countries.find(data['affiliation']['affiliation-country']) == -1:
                   countries += (data['affiliation']['affiliation-country'] + ", ")
       else:
          for affil in data['affiliation']:
              if affil['affiliation-country'] is not None:
                  if countries.find(affil['affiliation-country']) == -1:
                      countries += (affil['affiliation-country'] + ", ")
          
   else:
       return None

   return countries.lower()


def text_mine(virus_terms):


  con_file = open("config.json")
  config = json.load(con_file)
  con_file.close()
  client = ElsClient(config['apikey'])
  allurls = []
  virus_dict = pickle.load(open("viruspapers.pkl","rb"))

      
  for term in virus_terms:
    doc_srch = ElsSearch(term, 'sciencedirect')
    results = execute_modified(doc_srch.uri,client,set_limit=5000)

    header = {'X-ELS-APIKey': config['apikey'],'Accept': 'application/json'}


    print("SUCCESSFUL QUERY")

    for num,res in enumerate(results):
        DOI = res['prism:doi']
        URL = 'https://api.elsevier.com/content/article/DOI/' + str(DOI)
        if URL not in allurls:
          allurls.append(URL)
          r = requests.get(URL,headers=header)
          if num != 1457:
            js = json.loads(r.text)
            if 'scopus-id' in js["full-text-retrieval-response"]:
                abd = AbsDoc(scp_id = js["full-text-retrieval-response"]['scopus-id'])
                if abd.read(client):
                    abd.write()

                countries = get_countries(abd.data)
                if countries is not None:
                    js['countries'] = countries
                else:
                    continue


                js['countries'] = countries
                js['pubdate'] = abd.data['coredata']['prism:coverDate']
                js['journal'] = abd.data['coredata']['prism:publicationName']
       
                virus_dict[DOI] = js
                pickle.dump(virus_dict,open("viruspapers.pkl","wb"))
                print(len(virus_dict))
  

def main():
    text_mine(['H1N1'])
    
    
if __name__ == '__main__':
    main()
        
           