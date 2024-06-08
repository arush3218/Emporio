import time
from datetime import datetime
import json

def save_price_to_json(company_name,product_title,product_price):
    filename = 'price_data.json'
    if product_price:
        data = {
            'Website': company_name,
            "timestamp": datetime.now().isoformat(),
            "price": product_price,
            'title': product_title,
        }
        with open(filename, 'a') as f:
            json.dump(data, f)
            f.write('\n')
        print(f"Saved price {product_price} at {data['timestamp']}")
    else:
        print("Failed to retrieve the price")
        
save_price_to_json('name','title',19999)