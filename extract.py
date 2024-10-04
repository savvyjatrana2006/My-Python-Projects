import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Send a request to the Flipkart search results page
url = "https://www.flipkart.com/search?q=mobiles+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

response = requests.get(url, headers=headers)

# Step 2: Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "lxml")

# Step 3: Extract the required information
product_names = []
prices = []
ratings = []

for product in soup.find_all("div", class_="_1AtVbE"):
    name = product.find("div", class_="_4rR01T")
    price = product.find("div", class_="_30jeq3 _1_WHN1")
    rating = product.find("div", class_="_3LWZlK")
    
    if name and price:
        product_names.append(name.text)
        prices.append(price.text.replace('₹', '').replace(',', ''))  # Clean the price
        ratings.append(rating.text if rating else "No Rating")  # Handle missing ratings

# Step 4: Store the extracted data in a DataFrame
data = pd.DataFrame({
    "Product Name": product_names,
    "Price (INR)": prices,
    "Rating": ratings
})

# Step 5: Save the DataFrame to a CSV file
data.to_csv("flipkart_mobiles.csv", index=False)

print("Data saved to flipkart_mobiles.csv")
