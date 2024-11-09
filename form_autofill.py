import chromedriver_autoinstaller
import pandas as pd
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chromedriver_autoinstaller.install()

website = "https://forms.gle/YuQczM1pVUxnkuWL9"  # Google Form link

# Headless mode
options = Options()
options.add_argument("--headless=new")

driver = webdriver.Chrome()

df = pd.read_csv("./output/fake_data.csv")

for i in range(0, len(df)):
    driver.get(website)
    time.sleep(10)
    
    for column in df.columns:
        text_input = driver.find_element(by="xpath", value=f"//div[contains(@data-params, '{column}')]//input | "
                                                           f"//div[contains(@data-params, '{column}')]//textarea")
        text_input.send_keys(df.loc[i, column])
    
    submit_button = driver.find_element(by="xpath", value="//div[@role='button']//span[text()='Submit'] |"
                                                          "//div[@role='button']//span[text()='Kirim']")
    submit_button.click()

driver.quit