import requests
import bs4 
import smtplib
import json
import time
from database import product_history

my_email="arush3218@gmail.com"
password="fecttaurkgnlcsux"
connection=smtplib.SMTP("smtp.gmail.com")
connection.starttls()
    
base_url= "https://www.amazon.in"
url= input('Enter the amazon url:')
headerz={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    'Accept-Language': 'en-US,en;q=0.9',
   
}
base_response=requests.get(base_url,headers=headerz)
cookies=base_response.cookies

budget=float(input("Enter your budget:"))

product_request= requests.get(url,headers=headerz,cookies=cookies)
soup=bs4.BeautifulSoup(product_request.text,"html.parser")
pricess= soup.find(class_='a-price-whole')
title=soup.find(id='productTitle')
price=float(pricess.text.replace(',',''))

def send_mail():
    connection.login(user=my_email,password=password)
    ssendmail=connection.sendmail(from_addr=my_email,to_addrs=input('Enter your email:'),msg=f"Subject: PRICE DROPPED BELOW YOUR BUDGET FOR THE PRODUCT\nThe price of the product youve been wanting has dropeed below your budget!!Grab the offer now!!\n{url}")
    connection.close()

if price >= budget:
    send_mail()
    print(f"The product is in budget BUY NOW:\n{url}")

else:
    print("Price is still above the budget. Please wait for the best deal132")


print(title.text.replace('        ',''))
print(price)

    
