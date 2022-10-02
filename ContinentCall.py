import pandas as pd
import numpy as np
from newsapi.newsapi_client import NewsApiClient
from datetime import date,timedelta


class ContinentCall:
    def __init__(self):
        print('s')
    def region(temp,continent):
        # Date functions to use in all the query parameters
        dt_today = date.today()
        dt_week = dt_today - timedelta(7)
        newsapi = NewsApiClient('')
        call = newsapi.get_everything(q = continent,
                                    sources = 'wired, vice-news, techcrunch, financial-post,the-wall-street-journal',
                                    from_param = dt_week.strftime('%Y-%m-%d'), 
                                    to = dt_today.strftime('%Y-%m-%d'),
                                    language = 'en',
                                    sort_by = 'relevancy',
                                    ) 
        print(temp)
        # Converts our called data into a pandas dataframe
        df = pd.DataFrame(call['articles']) 
        list_ = []
        try:   
            df.drop(['urlToImage'], axis=1,inplace=True)
            
        
        #Editing the sources column because it's in a dictionary format. Converting it to a list and then to a dataframe
                                                  
            for x in df.source:
                list_.append(x['name'])
        except:
            print('No image or source')
        
        df.source = pd.DataFrame(list_)                  
        return df.values.tolist()

