# Here, we have the python functions used to derive the tuples that were sent to our dataset.  

- VirusPapers.py: Mines the ScienceDirect database using the API key in config.json  
- FormatCORDPapers.py: Formats the CORD-19 papers into tuples that can be sent to the database  
- FormatVirusPapers.py: Formats the ScienceDirect Virus papers into tuples that can be sent to the database  
- FormatTweets.py: Parses the tweets csv file to extract relevant information such as country, text, bio, etc.  
- FormatCSV.py: Extracts relevant information from the Cases, Measures, and countries data and places this information into tuples  
- StandardizeCountries.py: Ensures consistency in the country names between Virus papers and Country dataset.
