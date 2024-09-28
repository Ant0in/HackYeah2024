from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to a webpage
    driver.get("https://example.com")

    # Perform actions, for example, find an element
    element = driver.find_element(By.TAG_NAME, 'h1')
    print("Page title is:", element.text)

    driver.get("https://hackyeah.pl/tasks-prizes/")

    # Perform actions, for example, find an element
    element = driver.find_element(By.TAG_NAME, 'h2')
    print("Page title is:", element.text)
finally:
    # Clean up and close the driver
    driver.quit()
