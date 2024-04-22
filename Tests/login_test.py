import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Initialize the WebDriver
driver = webdriver.Chrome()  # You can use any other WebDriver like Firefox or Edge

pause = 1  # Pause duration to allow you to see what's happening

# Open the login page
driver.get("http://172.20.156.190:8081/")

# Wait for the username field to be present
username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "username"))
)
time.sleep(pause)  # Pause to allow observation of the field being located

# Enter the username slowly, character by character
for character in "test":
    username_field.send_keys(character)
    time.sleep(0.5)  # Pause after typing each character

# Wait for and find the password field
password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "password"))
)
time.sleep(pause)  # Pause to allow observation of the field being located

# Enter the password slowly, character by character
for character in "test":
    password_field.send_keys(character)
    time.sleep(0.5)  # Pause after typing each character

# Submit the login form by simulating the RETURN key
password_field.send_keys(Keys.RETURN)
time.sleep(pause)  # Pause to observe the submission action

# Wait for the page to load (you might need to add explicit waits for elements you expect on the next page)
# For example, you might wait for a specific element that only appears after login:
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "some_element_id"))
    )
except TimeoutException:
    print("Login failed or the expected element did not appear.")

time.sleep(10)  # Sleep for 10 seconds to allow you to inspect the page

# Close the WebDriver
driver.quit()
