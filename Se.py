from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Edge()

driver.get("https://hello.iitk.ac.in/user/login")

search_box = driver.find_element_by_id("edit-name")
search_box.send_keys("akshatm21@iitk.ac.in")

password = driver.find_element_by_id("edit-pass")
password.send_keys("")

driver.find_element_by_id("edit-submit").click()

driver.get("https://hello.iitk.ac.in/mth101a2122/#/lecture/18")

