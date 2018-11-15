from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import  Keys


path='C:\\Users\\vimmi\\webdrivers\\chromedriver'

driver = webdriver.Chrome(executable_path = path)
driver.get('http://www.theTestingWorld.com/testings')
driver.maximize_window()

# enter data into textbox
driver.find_element_by_name('fld_username').send_keys('hello_Vimmi')

act = ActionChains(driver)
act.send_keys(Keys.CONTROL)
act.send_keys(Keys.TAB).send_keys('a').perform()