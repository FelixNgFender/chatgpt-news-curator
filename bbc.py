from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Set up the web driver
driver = webdriver.Chrome()

# Load the search results page
url = "https://www.bbc.co.uk/search?q=chatgpt&d=HOMEPAGE_GNL"
driver.get(url)

links = []

# Click the div until it cannot be clicked anymore
while True:
    try:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='ssrcss-a11ok4-ArrowPageButtonContainer ep93jpm1']"))
        )
        time.sleep(1)  # Wait for new articles to load
        # Extract the article URLs from the search results page
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Target the ul element
        ul = soup.find("ul", {"class": "ssrcss-1020bd1-Stack e1y4nx260"})

        # Target the li elements
        lis = ul.find_all('article')

        # Get all the links from the article elements
        links += [li.find("a")["href"] for li in lis]
        # print(links)
        # print(len(links))
        
        load_more_button.click()
    except:
        break

# Append the links to articles_url.txt, one link per line
with open('articles_url.txt', 'a') as f:
    for link in links:
        f.write(link + '\n')