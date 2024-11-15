import requests
from bs4 import BeautifulSoup
import os

URL = "https://www.amazon.in/dp/B09XM4RNQT?ref_=cm_sw_r_apan_dp_3PAJMSHT9YDHZ2A5XGGE&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
                  "/115.0.0.0 Safari/537.36 OPR/101.0.0.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=URL, headers=headers)
amzn_html = response.text

soup = BeautifulSoup(amzn_html, "html.parser")
product_price = int(soup.find(class_="a-price-whole").text.replace(".", ""))
product_name = soup.find(id="productTitle").text.replace("        ", "").replace("       ", "")
product_link = soup.find_all("link", rel="canonical")[0]['href']


if product_price < 800:
    import smtplib

    my_mail = os.environ.get("MY_EMAIL")
    password = os.environ.get("MY_PASSWORD")
    to_mail = os.environ.get("TO_EMAIL")

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=to_mail,
            msg=f"Subject:Amazon Price Alert!🚨\n\n{product_name} is now ₹{product_price}.\n{product_link}".encode())
