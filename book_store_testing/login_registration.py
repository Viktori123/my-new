# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.find_element_by_id('menu-item-50').click()
# email = driver.find_element_by_id('reg_email')
# email.send_keys('rozavvl1@gmail.com')
# time.sleep(3)
# password = driver.find_element_by_id('reg_password')
# password.send_keys('123WSX321xsw')
# driver.find_element_by_css_selector('.woocomerce-FormRow.form-row :nth-child(3)').click()
# driver.quit()
###############################################################################

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.find_element_by_id('menu-item-50').click()
# login = driver.find_element_by_id('username')
# login.send_keys('rozavvl1@gmail.com')
# time.sleep(3)
# password = driver.find_element_by_id('password')
# password.send_keys('123WSX321xsw')
# driver.find_element_by_css_selector('.form-row [name="login"]').click()
# time.sleep(3)
# element = driver.find_element_by_css_selector('.woocommerce-MyAccount-navigation :nth-child(6)')
# element_get_text = element.text
# assert element_get_text == "Logout"
# driver.quit()
