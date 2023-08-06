# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(7)
# driver.execute_script('window.scrollBy(0,600);')
# driver.find_element_by_id('text-22-sub_row_1-0-2-0-0').click()
# driver.find_element_by_class_name('reviews_tab').click()
# driver.find_element_by_css_selector('.stars :nth-child(5)').click()
# review = driver.find_element_by_id('comment')
# review.send_keys('Nice book!')
# name = driver.find_element_by_id('author')
# name.send_keys('Viktori')
# time.sleep(3)
# email = driver.find_element_by_id('email')
# email.send_keys('rozavvl1@gmail.com')
# time.sleep(3)
# driver.find_element_by_class_name('submit').click()
# driver.quit()