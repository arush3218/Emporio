from bs4 import BeautifulSoup
import requests 

def reldig_scrape(product_title):
    url = f'https://www.reliancedigital.in/search?q={product_title[:5]}:relevance'
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
    product_title = soup.find('p', {'class': 'sp__name'})
    if product_title:
        product_title = product_title.get_text(strip=True)
    else:
        product_title = None

    # Extract product price
    product_price = None
    price_element = soup.find('div', {'span': 'TextWeb__Text-sc-1cyx778-0 gimCrs'})
    if price_element:
        product_price = price_element.get_text(strip=True).replace(',', '').replace('.', '')
    #print(product_price,product_title)
    return product_title, product_price
#reldig_scrape('acer nitro 5 i5')

