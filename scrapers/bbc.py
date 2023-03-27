from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Set up the web driver
driver = webdriver.Chrome()

# Load the search results page
url = "https://www.bbc.co.uk/search?q=chatgpt"
driver.get(url)

links = []

# Click the div until it cannot be clicked anymore
for i in range(2, 7):
    load_more_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='/search?q=chatgpt&d=SEARCH_PS&page=" + str(i) + "']"))
    )
    time.sleep(1)  # Wait for new articles to load
    # Extract the article URLs from the search results page
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Target the a elements
    anchors = soup.find_all("a", {"class": "ssrcss-rl2iw9-PromoLink e1f5wbog1"})
    # Append list of links to the end of links
    links.extend([anchor["href"] for anchor in anchors])
    load_more_button.click()

    # Account for the last page
    if i == 6:
        time.sleep(1)  # Wait for new articles to load
        # Extract the article URLs from the search results page
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Target the a elements
        anchors = soup.find_all("a", {"class": "ssrcss-rl2iw9-PromoLink e1f5wbog1"})
        # Append list of links to the end of links
        links.extend([anchor["href"] for anchor in anchors])

# Append the links to articles_url.txt, one link per line
with open('articles_url.txt', 'a') as f:
    for link in links:
        f.write(link + '\n')