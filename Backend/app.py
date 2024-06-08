
from amazonAZ import scrape_amazon
from database import product_history
from notification import email_notification
from flipkart import extract_product_name, flipkart_scrape
from croma import croma_scrape
from reldig import reldig_scrape
from dataTrackk import save_price_to_json
def main():
    url, budget = user_input()
    product_title, product_price = scrape_amazon(url)
    if product_title and product_price: 
        fproduct_title, fproduct_price = extract_product_name(url)              #extract
        cproduct_title, cproduct_price = croma_scrape(product_title)
        rproduct_title, rproduct_price = reldig_scrape(product_title)
        
        product_history(product_title, product_price, company_name='amazon',)       #store
        save_price_to_json(company_name='Amazon',product_title=product_title,product_price=product_price)
        
        product_history(fproduct_title, fproduct_price, company_name='flipkart')
        save_price_to_json(company_name='Flipkart',product_title=fproduct_title,product_price=fproduct_price)
        
        product_history(cproduct_title, cproduct_price, company_name='croma')
        save_price_to_json(company_name='Croma',product_title=cproduct_title,product_price=cproduct_price)

        product_history(rproduct_title,rproduct_price,company_name='reliance diigital')
        save_price_to_json(company_name='Reliance Digital',product_title=rproduct_title,product_price=rproduct_price)
        
        if float(product_price) <= budget:
            print('This product is within your budget.')
            email_notification()
        else:
            print('This product is not within your budget.')
    else:
        print('Could not retrieve product details.')

def user_input():
    url = input('Product URL: ')
    budget = float(input('Budget: '))
    return url, budget

if __name__ == '__main__':
    main()
    
#https://www.amazon.in/Acer-i5-12500H-Processor-15-6-inch-AN515-58/dp/B09X79JDC5/