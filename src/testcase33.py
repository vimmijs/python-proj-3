from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


path='C:\\Users\\vimmi\\webdrivers\\chromedriver'

driver = webdriver.Chrome(executable_path = path)
driver.get('http://www.theTestingWorld.com/')
driver.maximize_window()
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


act = ActionChains(driver)
#act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()
#act.click().perform()

#rt-click
#act.context_click().perform()

#act.double_click().perform()
#act.double_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()