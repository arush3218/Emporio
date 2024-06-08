from bs4 import BeautifulSoup
import requests
import re

def extract_product_name(url):
    
    pattern = r"([^/]+)/dp/"
    
    match = re.search(pattern, url)
    if match:
        product_title = match.group(1).replace('-', ' ')
        return flipkart_scrape(product_title)
    else:
        return "Product name not found"

def flipkart_scrape(product_title):
    
    url = f'https://www.flipkart.com/search?q={product_title}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f'Error fetching page: {e}')
        return None, None

    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract product title
    product_title = soup.find('div', {'class': 'KzDlHZ'})
    if product_title:
        product_title = product_title.get_text(strip=True)
    else:
        product_title = None

    # Extract product price
    product_price = None
    price_element = soup.find('div', {'class': 'Nx9bqj _4b5DiR'})
    if price_element:
        product_price = price_element.get_text(strip=True).replace(',', '').replace('.', '')

    return product_title, product_price