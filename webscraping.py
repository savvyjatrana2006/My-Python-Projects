import requests  
from bs4 import BeautifulSoup  

# Step 1: Send a GET request to the website  
url = 'http://justdile.com'  
response = requests.get(url)  

# Step 2: Parse the content of the page  
soup = BeautifulSoup(response.content, 'html.parser')  

# Step 3: Extract data (e.g., title of the page)  
title = soup.title.string  
print(f'Title: {title}')