# This app scrap product data from  amazon website


# BeautifulSoup4
# requests
# lxml


from bs4 import BeautifulSoup
import requests
import csv


url ="https://www.amazon.in/Sonos-Ace-Wireless-Headphones-Cancellation/dp/B0D37R7X6Z/ref=sr_1_17_sspa?crid=3TD7782SQ1LQW&dib=eyJ2IjoiMSJ9.WmthW5Av9KLVzjDws38S75FRrT1p9Eqc3-A4BkvqSuTGjHj071QN20LucGBJIEps.qQiMfkWIfs4TUu5Odabj2ngdaZrJs-GXV6ERbJ_Gq04&dib_tag=se&keywords=apple%2Bairpods%2Bmax%2Bwireless&nsdOptOutParam=true&qid=1764247794&sprefix=%2Caps%2C289&sr=8-17-spons&xpid=J3wl4LEBVRpU3&aref=OTTFtAF28v&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGZfbmV4dA&th=1"
headers = {"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}


response = requests.get(url, headers=headers)


if response.status_code == 200:
    # print(response.status_code)
    html_content = response.text
else:
    print("fetching error:", response.status_code)
    
    
  


soup = BeautifulSoup(html_content, 'lxml') 

# print(soup.prettify())    

product_title = soup.find ("span", id='productTitle').text.strip()
product_price = soup.find ("span", class_='a-price-whole').text.strip()
product_rating = soup.find ("span", class_='a-icon-alt').text.strip()
product_bp= soup.find ("span", class_='a-list-item').text.strip()
product_bullet_points = soup.find ("div", id='feature-bullets').text.strip()
product_reviews = soup.find ("span", id='acrCustomerReviewText').text.strip()

print(product_reviews)

# saving data to csv file
with open('amazon_product_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Title', 'Price', 'Rating', 'Best Price', 'Bullet Points', 'Reviews'])
    writer.writerow([product_title, product_price, product_rating, product_bp, product_bullet_points, product_reviews])
# printing the data
print("data saved to amazon_product_data.csv")