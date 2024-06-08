from bs4 import BeautifulSoup
import requests 
import time 

def croma_scrape(product_title):
    url = f'https://www.croma.com/searchB?q={product_title}%3Arelevance&text={product_title}'
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
    time.sleep(2)
    # Extract product title
    product_title = soup.find('a', {'href': '"/acer-nitro-5-intel-core-i5-13th-gen-gaming-laptop-16gb-512gb-windows-11-home-6gb-graphics-15-6-inch-144-hz-fhd-ips-display-nvidia-geforce-rtx-4050-ms-office-2021-obsidian-black-2-13-kg-/p/302709'})
    if product_title:
        product_title = product_title.get_text(strip=True)
    else:
        product_title = None

    # Extract product price
    product_price = None
    price_element = soup.find('div', {'span': 'amount plp-srp-new-amount'})
    if price_element:
        product_price = price_element.get_text(strip=True).replace(',', '').replace('.', '')
    print(product_price,product_title)
    return product_title, product_price
croma_scrape('acer nitro 5 i5')