from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

#--Chrome
service_obj = Service()

driver = webdriver.Chrome(service=service_obj)


driver.get("https://rahulshettyacademy.com/angularpractice/")

#ID, XPATH, CSS_SELECTOR, CLASSNAME, NAME, LINK_TEXT

driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# XPATH - //tagname[@attribute = 'value'] -> //input[@type='submit']
# CSS - tagname[@attribute = 'value'] -> input[@type='submit']

driver.find_element(By. CSS_SELECTOR,"input[name='name']").send_keys("Khushboo")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

#Static Dropdown
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(1)
#dropdown.select_by_value()

driver.find_element(By.XPATH,"//input[@type='submit']").click()
message= driver.find_element(By.CLASS_NAME,"alert-success").text
print(message)

assert "Success" in message

driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("helloagain")
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()


input("Press enter to close the browser")
