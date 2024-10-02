# automation_script.py
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load CSV data
csv_file = "path_to_your_csv_file.csv"  # Replace with your CSV file path
data = pd.read_csv(csv_file)

# Set up the WebDriver (Chrome)
chrome_driver_path = "path_to_your_chromedriver"  # Replace with your ChromeDriver path
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Log in to Django admin
admin_url = "http://your_django_admin_url/admin/login/?next=/admin/"
driver.get(admin_url)

# Login credentials
username = "your_username"
password = "your_password"

# Wait for the login form to appear, then input credentials
username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password_input = driver.find_element(By.NAME, "password")

username_input.send_keys(username)
password_input.send_keys(password)

# Submit login form
password_input.send_keys(Keys.RETURN)

# Wait for the page to load after login
time.sleep(3)

# Loop through the CSV data
for index, row in data.iterrows():
    # Navigate to the Django model's "add" page (adjust URL to your specific model)
    driver.get("http://your_django_admin_url/admin/your_app/your_model/add/")

    # Wait for the form to load
    time.sleep(2)

    # Fill in form fields (adjust the 'By.NAME' values according to your form fields in Django)
    driver.find_element(By.NAME, 'first_name').send_keys(row['first_name'])
    driver.find_element(By.NAME, 'last_name').send_keys(row['last_name'])
    driver.find_element(By.NAME, 'email').send_keys(row['email'])
    driver.find_element(By.NAME, 'phone_number').send_keys(row['phone_number'])

    # If there's a dropdown field (e.g., gender, nationality, etc.), use the appropriate keys
    driver.find_element(By.NAME, 'gender').send_keys(row['gender'])
    
    # Submit the form
    driver.find_element(By.NAME, '_save').click()

    # Wait for 3 seconds before processing the next entry
    time.sleep(3)

# Close the browser once the task is complete
driver.quit()

print("Automation complete!")
