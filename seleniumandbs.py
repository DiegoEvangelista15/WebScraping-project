from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.55538073901367%2C%22east%22%3A-122.31127826098633%2C%22south%22%3A37.65674456506729%2C%22north%22%3A37.89364955836753%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

address = soup.find_all(name='address', class_='list-card-addr') 
addresses = [n.getText() for n in address]
       
prices = [n.getText().split("+")[0] for n in soup.select('.list-card-heading div') if "$" in n.getText()]

links = [n.get('href') for n in soup.select('.list-card-top a') if "http" not in n]

links = []
link = soup.select('.list-card-top a')
for n in link:
    href = n['href']
    if 'https' not in href:
        links.append(f'https://www.zillow.com/{href}')
    else:
        links.append(href)
        
chrome_driver_path = Service(YOUR GOOGLE CHROME DRIVER LOCATION)
driver = webdriver.Chrome(service=chrome_driver_path)

for index in range(len(links)):
    driver.get(YOUR GOOGLE FORM)
    time.sleep(2)
    
    add = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add.send_keys(addresses[index])
    
    link = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(links[index])
    
    pric = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pric.send_keys(prices[index])
    
    confirm = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    confirm.click()
    
    time.sleep(3)
    
    confirm_again = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    confirm_again.click()
    
    
    
    
    
    # FOR TEST
    # print(addresses[index])
    # print(links[index])
    # print(prices[index])
    
    





    

