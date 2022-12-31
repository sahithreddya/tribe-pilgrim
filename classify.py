import pandas as pd
import nltk
from newspaper import Article
from newspaper import Config
nltk.download('punkt')
from newsapi import NewsApiClient
import openai 
import re 

# Openai Classification 

openai.api_key = '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'

class_list = []

for x in range(len(df.content)):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=f"Below is a list of categories: \nFinance \nBusiness \nStartups \nTechnology \nOther \n\n{df.content[x]} \n\nThe above text falls into the category:",
      temperature=0.7,
      max_tokens=5,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0, best_of = 9
    )
#     asia_weekly['class'] = response['choices'][0].text
    class_list.append(response['choices'][0].text)


df['class'] = class_list
df['class'] = df['class'].str.replace('\n','',regex = True)
df['class'] = df['class'].str.replace(r'[^\w\s]+', '',regex = True)

