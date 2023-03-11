import pandas as pd
import requests
from dotenv import load_dotenv
import os

load_dotenv()

NEWS_API_KEY = os.getenv('NEWS_API_KEY')

url = ('https://newsapi.org/v2/everything?'
       'q=ChatGPT&'
       f'apiKey={NEWS_API_KEY}')

response = requests.get(url)

# Convert response to Python dictionary
data_dict = response.json()

# Convert dictionary to pandas DataFrame
data = pd.DataFrame.from_dict(data_dict['articles'])

# Save DataFrame to CSV file in data folder
data.to_csv('data/news.csv', index=False)