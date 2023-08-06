#Отображение страницы товара

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
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_css_selector('.woocommerce-LoopProduct-link [alt="Mastering HTML5 Forms"]').click()
# name = driver.find_element_by_css_selector('.product_title.entry-title')
# name_get_text = name.text
# assert name_get_text =='HTML5 Forms'
# print('Заголовок книги называется HTML5 Forms')
# driver.quit()
############################################################################
#количество товаров  в категории

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
# driver.find_element_by_id('menu-item-40').click()
# time.sleep(3)
# driver.find_element_by_css_selector(' .product-categories>li:nth-child(2)>a').click()
# items_count = driver.find_elements_by_css_selector('.products.masonry-done li')
# assert len(items_count) == 3
# driver.quit()

###################################################################
#Сортировка товара

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
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
# driver.find_element_by_id('menu-item-40').click()
# element = driver.find_element_by_class_name('orderby')
# element_check = element.get_attribute("value")
# assert element_check == "menu_order"
# driver.find_element_by_class_name('orderby').click()
# price = driver.find_element_by_css_selector('[name="orderby"].orderby')
# select = Select(price)
# select.select_by_index(5)
# element = driver.find_element_by_css_selector('.orderby [value="price-desc"]')
# element_check = element.get_attribute("value")
# assert element_check == "price-desc"
# driver.quit()

#############################################################
#Отображение. скидка товара

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
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
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_css_selector('[title="Android Quick Start Guide"]').click()
# old = driver.find_element_by_css_selector('.price > del > span')
# old_get_text = old.text
# assert old_get_text == '₹600.00'
# new = driver.find_element_by_css_selector('.price > ins >span')
# new_get_text = new.text
# assert new_get_text == '₹450.00'
# element = WebDriverWait(driver, 10).until(
#      EC.element_to_be_clickable((By.CSS_SELECTOR, ".woocommerce-main-image.zoom")))
# element.click()
# btn = WebDriverWait(driver, 10).until(
#      EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# btn.click()
# driver.quit()
#####################################################################
#Проверка цены в корзине

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.find_element_by_id('menu-item-40').click()
# driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()
# item = driver.find_element_by_css_selector('[title="View your shopping cart"] > .cartcontents ')
# item_get_text = item.text
# price = driver.find_element_by_class_name('amount')
# price_get_text = price.text
# assert item_get_text == "1 Item"
# assert price_get_text == "₹180.00"
# cart = driver.find_element_by_class_name('wpmenucart-contents')
# cart.click()
# time.sleep(3)
# some_element = WebDriverWait(driver, 10).until(
#      EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal"), "₹180.00"))
# element = WebDriverWait(driver, 10).until(
#      EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.order-total>[data-title="Total"]'), "₹183.60"))
# driver.quit()

##########################################################
#Работа в корзине

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.find_element_by_id('menu-item-40').click()
# driver.execute_script('window.scrollBy(0,300);')
# time.sleep(3)
# #driver.find_element_by_css_selector('[data-product_id="182"]').click() # Книга не добавлялась тест выполнен с одной книгой
# driver.find_element_by_css_selector('[href="/shop/?add-to-cart=180"]').click()
# time.sleep(3)
# cart = driver.find_element_by_id('wpmenucartli')
# cart.click()
# time.sleep(3)
# driver.find_element_by_css_selector('[title="Remove this item"]').click()
# time.sleep(3)
# driver.find_element_by_css_selector('.woocommerce-message>a').click()
# driver.find_element_by_css_selector('.cart_item:nth-child(1) .quantity [step="1"]').clear()
# driver.find_element_by_css_selector('.cart_item:nth-child(1) .quantity [step="1"]').click()
# quant = driver.find_element_by_css_selector('.cart_item:nth-child(1) .quantity [step="1"]')
# quant.send_keys(3)
# driver.find_element_by_css_selector('[name="update_cart"]').click()
# time.sleep(3)
# quantity = driver.find_element_by_css_selector('.quantity>input')
# quantity_check = quantity.get_attribute('value')
# assert quantity_check == "3"
# time.sleep(3)
# apply = driver.find_element_by_css_selector('[name="apply_coupon"]').click()
# element1 = driver.find_element_by_css_selector('.woocommerce-error > li')
# element1_get_text = element1.text
# assert element1_get_text == 'Please enter a coupon code.'
# driver.quit()

#########################################################

#Покуака товара

# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get("https://practice.automationtesting.in/")
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.find_element_by_id('menu-item-40').click()
# driver.execute_script('window.scrollBy(0,300);')
# time.sleep(3)
# driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]').click()
# cart = driver.find_element_by_css_selector('[title="View your shopping cart"]')
# cart.click()
# driver.execute_script('window.scrollBy(0,600);')
# time.sleep(5)
# element = WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '.wc-proceed-to-checkout>a')))
# element.click()
# time.sleep(3)
# first_name = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, 'billing_first_name')))
# first_name.click()
# first_name = driver.find_element_by_id('billing_first_name')
# first_name.send_keys('Viktori')
# last_name = driver.find_element_by_id('billing_last_name')
# last_name.send_keys('Totori')
# email = driver.find_element_by_id('billing_email')
# email.send_keys('rozavvl1@gmail.com')
# phone = driver.find_element_by_id('billing_phone')
# phone.send_keys('1234567890')
# driver.find_element_by_id('s2id_billing_country').click()
# search = driver.find_element_by_id('s2id_autogen1_search')
# search.send_keys('Russia')
# driver.find_element_by_css_selector('ul li div span.select2-match').click()
# address = driver.find_element_by_id('billing_address_1')
# address.send_keys('1234')
# city = driver.find_element_by_id('billing_city')
# city.send_keys('Moscow')
# state = driver.find_element_by_id('billing_state')
# state.send_keys('Russia')
# zip = driver.find_element_by_id('billing_postcode')
# zip.send_keys('123')
# driver.execute_script('window.scrollBy(0,600);')
# time.sleep(5)
# pay = driver.find_element_by_id('payment_method_cheque').click()
# driver.find_element_by_id('place_order').click()
# some_element= WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received "), "Thank you. Your order has been received."))
# some_element = WebDriverWait(driver, 10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot :nth-child(3)>td "), "Check Payments"))
# driver.quit()