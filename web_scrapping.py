import chromedriver_autoinstaller
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()

web = "https://www.thesun.co.uk/sport/football/"

# Headless mode
options = Options()
options.add_argument("--headless=new")

driver = webdriver.Chrome()
driver.get(web)

# Wait for the containers to be present
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='teaser__copy-container']")))
containers = driver.find_elements(By.XPATH, "//div[@class='teaser__copy-container']")

titles = []
subtitles = []
links = []

for container in containers:
    try:
        link = container.find_element(By.XPATH, "./a").get_attribute("href")
        
        try:
            title = container.find_element(By.XPATH, "./a/span[contains(@class, 'teaser__kicker')]").text
        except:
            title = None
        
        try:
            subtitle = container.find_element(By.XPATH, "./a/h3").text
        except:
            subtitle = None
    
    except:
        link = None
           
        try:
            title = container.find_element(By.XPATH, "./span[contains(@class, 'teaser__kicker')]").text
        except:
            title = None
        
        try:
            subtitle= container.find_element(By.XPATH, "./h3").text
        except:
            subtitle = None

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

# Create DataFrame
df = pd.DataFrame({"Title": titles, "Subtitle": subtitles, "Link": links})

# Exporting data to the same folder where the executable will be located
my_dict = {"title": titles, "subtitle": subtitles, "link": links}
df_headlines = pd.DataFrame(my_dict)
df_headlines.to_csv("./output/auto_headline.csv")

driver.quit()