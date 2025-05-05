import pandas as pd
import time
import os
import csv
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# ============ CONFIG ============
MAX_PAGES = 40
BASE_PAGE_URL = "https://www.cityu.edu.hk/hktech300/start-ups/all-start-ups?page="
BASE_DOMAIN = "https://www.cityu.edu.hk"
OUTPUT_CSV = "cityu_tech300_startups.csv"

# Check if the output file already exists, if so, exit the script to avoid overwriting
file_exists = os.path.isfile(OUTPUT_CSV)
if file_exists:
    print(f"File {OUTPUT_CSV} already exists. Please delete it before running the script.")
    exit(1)
else:
    with open(OUTPUT_CSV, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Company Name", "CityU URL", "Company Website", "Email"])


# ============ Setup Selenium ============
options = Options()
options.add_argument("--headless") # This will run Chrome without opening a window
driver = webdriver.Chrome(options=options)

# ============ Helper Functions ============
def extract_profile_details(profile_soup):
    """
    Extracts the company website and email address from a startup's profile page.

    Args:
        profile_soup (BeautifulSoup): The BeautifulSoup-parsed HTML content of a startup's profile page.

    Returns:
        tuple: A tuple containing two strings:
            - website (str): The company's external website URL (if available).
            - email (str): The team member's email address (if available).
    """

    website, email = None, None

    # Dynamically look for any plugin-id ending with :field_client or :field_company_website (Company Website)
    website_div = profile_soup.find(
        'div',
        attrs={"data-block-plugin-id": lambda value: value and (
            value.endswith(":field_client") or value.endswith(":field_company_website")
        )}
    )
    if website_div:
        a_tag = website_div.find('a', href=True)
        if a_tag:
            website = a_tag['href'].strip()

    # Dynamically look for any plugin-id ending with :field_team_members_email (Company Email)
    email_div = profile_soup.find(
        'div',
        attrs={"data-block-plugin-id": lambda value: value and value.endswith(":field_team_members_email")}
    )
    if email_div:
        a_tag = email_div.find('a', href=True)
        if a_tag:
            email = a_tag.text.strip()

    # If no email or website found, return "No Info Found" else return the found values
    email = email or "No Info Found"
    website = website or "No Info Found"

    return website, email

# ============ Main Scraping Logic ============

print("Starting the scraping process...")

# Loop through all pages and scape the startup information
for page in tqdm(range(MAX_PAGES), desc="Scraping Startup Information from CityU"):
    page_url = f"{BASE_PAGE_URL}{page}"
    driver.get(page_url)
    time.sleep(2)  # Wait for the page to load

    # Get the main page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Get all <li> elements under the specified (contains all the startup information)
    li_elements = soup.select("ul.list-unstyled.row > li")

    # Loop through each <li> element and extract the required information
    for li in tqdm(li_elements, desc=f"Page {page + 1}"):
        card = li.select_one("div.card.fund.team")
        if not card:
            continue

        # Extract company name + profile URL
        a_tags = card.find_all("a")
        name, profile_url = None, None
        for a in a_tags:
            if a.text.strip():
                name = a.text.strip()
                profile_url = BASE_DOMAIN + a.get("href")
                break
        
        # If company name or city profile URL is not found, skip this entry
        if not name or not profile_url:
            continue

        # Load the company profile page
        driver.get(profile_url)
        time.sleep(2) # Wait for the page to load

        # Get the startup profile page source and parse it with BeautifulSoup
        profile_soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extract website and email from profile
        website, email = extract_profile_details(profile_soup)

        # Append the data to the CSV file
        with open(OUTPUT_CSV, mode='a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([name, profile_url, website, email])

# Close the WebDriver
driver.quit()
print("Scraping Completed. Data successfully saved to cityu_tech300_startups.csv")