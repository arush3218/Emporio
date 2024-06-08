import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def product_history(product_name, product_price, company_name):
    product_data = {
        'product_title': product_name,
        'product_price': product_price,
        'search_date': datetime.now().strftime('%d-%B-%Y'),
        'search_time': datetime.now().strftime('%I:%M %p')
    }

    # Check if company document exists
    company_ref = db.collection('products').document(company_name)
    if company_ref.get().exists:
        # Update product history
        company_ref.update({
            'product_history': firestore.ArrayUnion([product_data])
        })
    else:
        # Create new company document and product history
        company_ref.set({
            'product_history': [product_data]
        })