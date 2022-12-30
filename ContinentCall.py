import pandas as pd
import numpy as np
from newsapi.newsapi_client import NewsApiClient
from datetime import date,timedelta
from newspaper import Article
from newspaper import Config
import openai 


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent

# openai classification function 
def classify(text):
    openai.api_key = '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'

    class_list = []
    for x in range(len(text)):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Below is a list of categories: \nFinance \nBusiness \nStartups \nTechnology \nOther \n\n{text[x]} \n\nThe above text falls into the category:",
        temperature=0.7,
        max_tokens=5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0, best_of = 9
        ) 
        class_list.append(response['choices'][0].text)
        return class_list
        # text = class_list
        # text= text.str.replace('\n','',regex = True)
        # text = text.str.replace(r'[^\w\s]+', '',regex = True)

# continent call-- data extraction -- summary extraction[newspaper api] -- news classification

class ContinentCall:
    def __init__(self, ud):
        print('s')
        print(ud)
    def region(temp,continent):
        # Date functions to use in all the query parameters
        dt_today = date.today()
        dt_week = dt_today - timedelta(7)
        newsapi = NewsApiClient('6e14aba1dfc84a5094aaed459344a228')
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
        df['class'] = None

        # getting the summary of the article 
        for x in range(len(df.url)):
            try:
                article = Article(df.url[x],config = config)
                article.download()
                article.parse()
                article.nlp()
                df.content[x] = article.summary
                df['content'] = df['content'].replace('\n', '',regex = True) 
                df['class'][x] = classify(df['content'][0])
            except Exception as e:
                print('x')

        list_ = []
        try:   
            df.drop(['urlToImage'], axis=1,inplace=True)                                                  
            for x in df.source:
                list_.append(x['name'])
        except:
            print('No image or source')
    
        df.source = pd.DataFrame(list_)                  
        return df.values.tolist()
    



            
            




