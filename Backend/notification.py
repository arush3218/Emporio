import smtplib
email = 'arush3218@gmail.com'
password = 'fecttaurkgnlcsux'


def email_notification():
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(user=email, password=password)
    
    message = (
        f'Subject: PRICE DROPPED BELOW YOUR BUDGET FOR THE PRODUCT\n\n'
        f'The price of the product you\'ve been wanting has dropped below your budget! '
        f'Grab the offer now!!\n'
    )
    recipient_email = input('Enter your email:')
    connection.sendmail(from_addr=email, to_addrs=recipient_email, msg=message)
    connection.close()
    
    return 'Email sent successfully.'
