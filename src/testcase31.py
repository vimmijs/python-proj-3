from selenium import webdriver

path='C:\\Users\\vimmi\\webdrivers\\chromedriver'

driver = webdriver.Chrome(executable_path = path)
driver.get('http://www.theTestingWorld.com/testings')
driver.maximize_window()

# enter data into textbox
driver.find_element_by_name('fld_username').send_keys('hello_Vimmi')
driver.find_element_by_xpath("//input[@name='fld_email']").send_keys('abc@yahoo.com')
driver.find_element_by_name('fld_password').send_keys('abc123')
driver.find_element_by_name('fld_cpassword').send_keys('abc123')
driver.find_element_by_name('fld_username').send_keys('abc123')
driver.find_element_by_name('fld_username').clear()
driver.find_element_by_name('fld_username').send_keys('abc123')

# new comment
driver.find_element_by_xpath("//input[@value='office']").click()

# working on check button
driver.find_element_by_xpath("//input[@name='terms']").click()

# working on button
driver.find_element_by_xpath("//input[@type='submit']").click()

# working on link
driver.find_element_by_link_text('Read Detail').click()

driver.find_element_by_name('fld_username').clear()

driver.find_element_by_name('fld_username').send_keys('xyz567')

driver.close()