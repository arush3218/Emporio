import requests
from bs4 import BeautifulSoup
import json
#import schedule
import time
from datetime import datetime

# Function to scrape the product price
def scrape_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    price_element = soup.find('span', {'class': 'a-price-whole'})
    price = float(price_element.text.replace(',',''))
    product_title = soup.find('span', {'id': 'productTitle'})(strip= True)
    if price:
        return price and product_title
    else:
        return "Price not found"

def save_price_to_json(url, filename):
    price = scrape_price(url)
    if price:
        data = {
            "timestamp": datetime.now().isoformat(),
            "price": price,
            'title': product_title
        }
        with open(filename, 'a') as f:
            json.dump(data, f)
            f.write('\n')
        print(f"Saved price {price} at {data['timestamp']}")
    else:
        print("Failed to retrieve the price")

# Function to be scheduled
# def job():
#     url = input('URL:')  # Replace with the actual product URL
#     filename = 'price_data.json'
#     save_price_to_json(url, filename)

# # Schedule the job every hour
# schedule.every().hour.do(job)

# print("Starting the scheduler...")
# while True:
#     schedule.run_pending()
#     time.sleep(1)
url = input('URL:')  # Replace with the actual product URL
filename = 'price_data.json'
save_price_to_json(url, filename)