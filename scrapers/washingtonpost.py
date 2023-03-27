from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Set up the web driver
driver = webdriver.Chrome()

# Load the search results page
url = "https://www.washingtonpost.com/search/?query=chatgpt"
driver.get(url)

# Wait for the "Load More" button to appear and click it until it's no longer there.
while True:
    try:
        load_more_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='inline-flex items-center justify-center lh-md overflow-hidden border-box min-w-btn transition-colors duration-200 ease-in-out font-sans-serif font-bold antialiased bg-offblack hover-bg-gray-darker focus-bg-gray-darker white b-solid bw bc-transparent focus-bc-black mt-md mb-md brad-lg pl-md pr-md h-md pt-0 pb-0 w-100 pointer']"))
        )
        time.sleep(1)  # Wait for new articles to load
        load_more_button.click()
    except:
        break

# Extract the article URLs from the search results page
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Target the section element
section = soup.find("section", {"class": "search-results-wrapper"})

# Target the article elements
articles = section.find_all('article')

# Get all the links from the article elements
links = [article.find("a")["href"] for article in articles]

# Append the links to articles_url.txt, one link per line
with open('articles_url.txt', 'a') as f:
    for link in links:
        f.write(link + '\n')

# Trim the last 17 lines of articles_url.txt
with open('articles_url.txt', 'r') as f:
    lines = f.readlines()
with open('articles_url.txt', 'w') as f:
    for line in lines[:-17]:
        f.write(line)