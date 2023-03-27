from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Set up the web driver
driver = webdriver.Chrome()

# Load the search results page
url = "https://www.nytimes.com/search?query=chatgpt"
driver.get(url)

# Wait for the "Load More" button to appear and click it until it's no longer there
while True:
    try:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-testid='search-show-more-button']"))
        )
        time.sleep(1)  # Wait for new articles to load
        load_more_button.click()
    except:
        break

# Extract the article URLs from the search results page
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Target the ol element
ol = soup.find("ol", {"data-testid": "search-results"})

# Target the li elements
lis = ol.find_all('li')

# Get all the links from the li elements
links = [li.find("a")["href"] for li in lis]

# Append the links to articles_url.txt, one link per line
with open('articles_url.txt', 'a') as f:
    for link in links:
        if link.startswith('/'):
            f.write('https://www.nytimes.com' + link + '\n')