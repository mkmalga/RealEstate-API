from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

# Path to your ChromeDriver
chrome_driver_path = r"D:\NEW PROJECT\chromedriver-win64\chromedriver.exe"

# Set up Selenium WebDriver
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (no GUI)
driver = webdriver.Chrome(service=service, options=options)

# URL for Hyderabad property listings
url = "https://www.magicbricks.com/property-for-sale-rent-in-Hyderabad/residential-real-estate-Hyderabad"

# Load the website
driver.get(url)
time.sleep(5)  # Wait for the page to load

# Scroll down to load more listings
for _ in range(3):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(3)

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()  # Close browser

# Extract property details
properties = []
listings = soup.find_all("div", class_="mb-srp__list")  # Adjust class as per website

for listing in listings:
    try:
        title = listing.find("h2", class_="mb-srp__card--title").text.strip()
        price = listing.find("div", class_="mb-srp__card__price").text.strip()
        location = listing.find("div", class_="mb-srp__card--address").text.strip()
        details = listing.find_all("div", class_="mb-srp__card__summary__list--item")

        bhk = details[0].text.strip() if len(details) > 0 else "N/A"
        sqft = details[1].text.strip() if len(details) > 1 else "N/A"
        
        properties.append([title, price, location, bhk, sqft])
    except AttributeError:
        continue  # Skip listings with missing data

# Convert to DataFrame
df = pd.DataFrame(properties, columns=["Title", "Price", "Location", "BHK", "Square Feet"])

# Save as CSV
df.to_csv("hyderabad_housing_data.csv", index=False)

print("Scraping complete! Data saved to hyderabad_housing_data.csv")
