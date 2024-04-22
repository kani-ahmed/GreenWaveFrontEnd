import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Initialize the WebDriver
driver = webdriver.Chrome()  # You can use any other WebDriver like Firefox or Edge

pause = 0.5  # Increase pause duration to better observe the actions

# Open the login page
driver.get("http://172.20.156.190:8081/")
time.sleep(pause)  # Pause after opening the page

# Wait for the username field to be present
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
time.sleep(pause)  # Pause to allow observation of the field being located

# Enter the username slowly, character by character
for character in "test":
    username_field.send_keys(character)
    time.sleep(0.3)  # Increase pause after typing each character for better visibility

# Wait for and find the password field
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password"))
)
time.sleep(pause)  # Pause to allow observation of the field being located

# Enter the password slowly, character by character
for character in "test":
    password_field.send_keys(character)
    time.sleep(0.3)  # Increase pause after typing each character

# Submit the login form by simulating the RETURN key
password_field.send_keys(Keys.RETURN)
time.sleep(pause)  # Pause to observe the submission action

# Wait for the page to load
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "some_element_id"))
    )
    time.sleep(pause)  # Pause once the page has loaded
except TimeoutException:
    print("Login failed or the expected element did not appear.")
    time.sleep(pause)

# Wait for and interact with the dropdown
dropdown = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "bottlepicker"))
)
Select(dropdown).select_by_value('rp25')  # Select "Reusable Plastic 25 oz" from dropdown
time.sleep(pause)  # Pause to observe the dropdown selection

# Find and click the button (represented here by an image)
button = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//img[contains(@src, "waterbottle")]'))
)
button.click()
time.sleep(pause)  # Pause after button click to observe the action

time.sleep(5)  # Sleep for 10 seconds to allow you to inspect the page

# Close the WebDriver
driver.quit()
