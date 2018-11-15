from selenium import webdriver

path='C:\\Users\\vimmi\\webdrivers\\chromedriver'

driver = webdriver.Chrome(executable_path = path)
driver.get('http://www.theTestingWorld.com/testings')
driver.maximize_window()

# enter data into textbox
driver.find_element_by_name('fld_username').send_keys('hello_Vimmi')
