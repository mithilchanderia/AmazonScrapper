from bs4 import BeautifulSoup
import requests
import smtplib
import time

URL='https://www.amazon.in/dp/B07XVMCLP7'
flag=True
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

def check_price():
    page=requests.get(URL,headers=headers)

    soup= BeautifulSoup(page.content,'html.parser')

    title=soup.findAll('span',id='productTitle')[0].get_text().strip()
    price=float(soup.findAll('span',id='priceblock_ourprice')[0].get_text().strip()[2:].replace(',',''))
    if(price<69900):
        send_mail(title,price)
    else:
        print("price is high")

def send_mail(title,price):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('fragout1010@gmail.com','password')
    subject='PRICE OF {} IS DOWN'.format(title)
    body='Here is the link to the product: {} Hurry up!'.format(URL)
    msg1=f"Subject:{subject}\n\n{body}"

    server.sendmail(from_addr='fragout1010@gmail.com',
                    to_addrs='mithilchanderia@gmail.com',
                    msg=msg1)
    print("Email is sent")
    global flag
    flag=False
    server.quit()

while(flag==True):
    print(flag)
    check_price()
    time.sleep(60)
