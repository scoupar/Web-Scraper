import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.co.uk/Hitman-III-Deluxe-Edition-PS4/dp/B08LZNKJ7X/ref=sr_1_4?dchild=1&keywords=hitman+3&qid=1622726139&sr=8-4'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:6])

    if(converted_price > 40.00):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('scott.coupar@googlemail.com', 'nyckcecjlpifxqex')
    subject = 'Price Fell Down'
    body = 'Check out the new price on Amazon: https://www.amazon.co.uk/Hitman-III-Deluxe-Edition-PS4/dp/B08LZNKJ7X/ref=sr_1_4?dchild=1&keywords=hitman+3&qid=1622726139&sr=8-4'

    msg =f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'scott.coupar@googlemail.com',
        'allthewaydown@gmail.com',
        msg
    )

    print('Hey, email has been sent!')

    server.quit()

while(True):
    check_price()
    time.sleep(86400)
