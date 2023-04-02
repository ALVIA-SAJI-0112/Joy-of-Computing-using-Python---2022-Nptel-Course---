import pandas as d
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyser
nltk.downloader.download('vader_lexicon')
file='/Users/path....date_file.xslsx'
xl=pd.ExcelFile(file) #Read from Excel
dfs=xl.parse(xl.sheet_names[0])#Parsing
dfs=list(dfs['Timeline'])#removes the blank rows from the data
print(dfs)
sid=SentimentIntensityAnalyser()
str1="UTC+05:30"
for data in dfs:
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])
