

import pickle
import pandas as pd

'''
sample tuple structure:
    
(ID, title, pub_date, journal, authors, countries,abstract,full_text,references)
  
'''
  
def format_CORD_Papers(downsample = None):
    
    meta = pd.read_csv('metadata.csv')
    cities = pd.read_csv('cities.csv')

    newtitle = []
    for val in meta['title'].values:
        if type(val) is str:
            newtitle.append(val.lower())
        else:
            newtitle.append(None)
    meta['title'] = newtitle
    print(meta.columns)


    
    corddata = pickle.load(open('corddata.pkl','rb'))

    all_tuples = []
    currpapers = []
    alltitles = []
    j = 0
    i = 0

    for n,paper in enumerate(list(meta['title'].values)):
    
      if paper in corddata.keys() and paper not in currpapers: 
         
        currpapers.append(paper)
                       

        
        if corddata[paper]['metadata']['title'] == "":
            continue
    
     
        if corddata[paper]['metadata']['title'].lower() in alltitles:
            continue
        else:
            alltitles.append(corddata[paper]['metadata']['title'].lower())


        if corddata[paper]['metadata']['authors'] == "" :
            continue
        '''
        if 'abstract' not in corddata[paper]:
            continue
        '''
  
        tup = (corddata[paper]['paper_id'].lower(),)
     
        tup += (corddata[paper]['metadata']['title'].lower(),)

        #print(type(meta['abstract'][list(meta['title']).index(corddata[paper]['metadata']['title'].lower())]))
        if type(meta['abstract'][list(meta['title']).index(corddata[paper]['metadata']['title'].lower())]) is not float:
           tup += (meta['abstract'][list(meta['title']).index(corddata[paper]['metadata']['title'].lower())].lower(),)
        else:
            continue
        


        
        '''
        stringabs = ""
        for dic in corddata[paper]['abstract']:
            for key in dic:
                if key == "text":
                    stringabs += dic[key]
        
        
        if len(stringabs) > 0:
            tup += (stringabs.lower(),)
        else:
            continue
        '''
    
        if type(list(meta['journal'].values)[list(meta['title'].values).index(tup[1])]) not in [str,int]:
            tup = None
            continue
        
                       

        date = list(meta['publish_time'].values)[list(meta['title'].values).index(tup[1])].split('-')
        if len(date) < 3:
            continue



        tup += (date[0],date[1],date[2],)
        tup += (list(meta['journal'].values)[list(meta['title'].values).index(tup[1])].lower(),)

        authors = ""
        countries = ""
        
        for dic in corddata[paper]['metadata']['authors']:
            if dic['middle'] != []:
                middle = dic['middle'][0]
            else:
                middle = ""
        
            if dic['first'] != []:
                first = (dic['first']) + " "
            else:
                first = ""
            
            if dic['last'] != []:
                last = dic['last'] + ", "
            else:
                last = ""


            authors += ((last + first + middle) + " ")
            if len(list(dic['affiliation'].keys())) > 0:
                if 'location' in dic['affiliation']:
                    if 'country' in dic['affiliation']['location']:
                        if countries.find(dic['affiliation']['location']['country']) == -1:
                            countries += (dic['affiliation']['location']['country'] + ", ")
                    if 'country' not in dic['affiliation']['location'] and 'settlement' in dic['affiliation']['location']:
                        city = dic['affiliation']['location']['settlement'].split(',')[0]
                        print(city)
                        if city in list(cities['city']):
                            country = list(cities['country'])[list(cities['city']).index(city)].lower()
                            if countries.find(country) == -1:
                                 countries +=country
  
              
        if len(authors) == 0:
            continue
        else:
             tup += (authors.lower(),)
            
        if len(countries) == 0:
            tup += (None,)
        else:
             tup += (countries.lower(),)
  

        if 'body_text' in corddata[paper]:
            stringtext = ""
            for dic in corddata[paper]['body_text']:
                for key in dic:
                    if key == 'text':
                        stringtext += dic[key]
        
            if len(stringtext) > 0:   
                tup += (stringtext.lower(),) 
            else:
                continue  
        else:
            continue
 
        if 'bib_entries' in corddata[paper]:
            allstringrefs = ""
            for ref in corddata[paper]['bib_entries']:
                if str(ref).find('BIBREF') > -1:
                    stringref = ""
                    for auth in corddata[paper]["bib_entries"][ref]['authors']:
                        stringref = auth['last'] + ", "
                        stringref += auth['first'] + " "
                        if auth['middle'] != []:
                            stringref += (auth['middle'][0] + " ")
                    stringref += corddata[paper]["bib_entries"][ref]['title']
                    allstringrefs += (stringref + " ")
    
    
            if len(allstringrefs) > 0:
                tup += (allstringrefs,)
            else:
                continue
        else:
            continue

        all_tuples.append(tup)
        print(tup)
        j+=1
        if downsample is not None:
            if j >= downsample:
               break

        
    pickle.dump(all_tuples,open("covidpapertuples.pkl","wb"))    
 
    
def main():
    format_CORD_Papers(downsample=1000)
    
    
if __name__ == '__main__':
    main()
    