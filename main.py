
# URL of the website to scrape

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Use the appropriate WebDriver for your browser

# URL of the webpage to scrape
url = "https://www.forbes.com/real-time-billionaires/"

# Load the page
driver.get(url)
try:
    # Wait for the table rows to load (adjust the selector as needed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "tr.base"))
    )

    # Get the page source after JavaScript execution
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Find all table rows with class "base"
    rows = soup.find_all("tr", class_="base")

    # Extract only the <h3> elements from the first 200 rows
    data = []
    for i, row in enumerate(rows[:200], start=1):
        h3_elements = [h3.get_text(strip=True) for h3 in row.find_all("h3")]
        data.append(h3_elements)
        print(f"{i}. {h3_elements[0]}")

finally:
    # Close the WebDriver
    driver.quit()