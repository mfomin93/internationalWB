import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import datetime

# log write and path
output_file_name = "logs"
output_file_path = os.getcwd() + "//{}.txt".format(output_file_name)
outputFile = open(output_file_path, "a+")


# date/timestamp function
def get_timestamp():
    dt = datetime.datetime.now()
    print_timestamp = dt.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    return print_timestamp


# WEB UI LOCATORS
RESET_ALL_OUTLETS = (By.XPATH, "/html/body/div/div[2]/div[4]/button")

# counter variables
resets_counter = 0
USERNAME = input("Enter the username: ")
PASSWORD = input("Enter the password: ")
IP_ADDRESS = input("Enter the Wattbox IP address: ")
URL = "http://{}:{}@{}/main".format(USERNAME, PASSWORD, IP_ADDRESS)
start_script_choice = input("Start script? y/n: ")

print(get_timestamp(), "Script started!")
print(get_timestamp(), "Script started!", file=outputFile)

options = Options()
capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "normal"
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(10)

while start_script_choice == 'Y' or start_script_choice == 'y':
    driver.set_window_size(1200, 600)

    # Increases + 1 for every loop
    resets_counter = resets_counter + 1
    print(get_timestamp(), "Outlet Reset Count: " + str(resets_counter))
    print(get_timestamp(), "Outlet Reset Count: " + str(resets_counter), file=outputFile)

    # Navigate to web interface
    driver.get(URL)
    time.sleep(2)

    # Selecting Update button
    print(get_timestamp(), "Resetting all outlets...")
    print(get_timestamp(), "Resetting all outlets...", file=outputFile)
    driver.find_element(*RESET_ALL_OUTLETS).click()

    # Waiting couple minutes for device to boot up and recover
    print(get_timestamp(), "Waiting 5 minutes...")
    print(get_timestamp(), "Waiting 5 minutes...", file=outputFile)
    time.sleep(300)

    # Browser close
    print(get_timestamp(), "Restarting Test!")
    print(get_timestamp(), "Restarting Test!", file=outputFile)
    time.sleep(2)
    driver.close()
    time.sleep(2)
    driver.start_session(capabilities=capa)
    driver.set_window_size(1200, 600)


print(get_timestamp(), "Script Finished!")
print(get_timestamp(), "Script Finished!", file=outputFile)

driver.quit()
