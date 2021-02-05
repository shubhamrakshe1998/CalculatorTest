from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:\driver\chromedriver.exe")

driver.get("https://www.calculator.net/")
print(driver.title)
print(driver.current_url)
# Multiplication code
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[1]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[2]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[3]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[4]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[2]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[2]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[2]").click()

element = driver.find_element_by_xpath("//*[@id='sciOutPut']").text
result1 = int(element)

if result1 == 222075:
    print("Test 1 passed")
else:
    print("Test 1 failed")

time.sleep(5)
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[5]/span[3]").click()
time.sleep(2)


#Division code

driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[1]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[4]/span[1]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[4]/span[1]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[4]/span[1]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[4]/span[4]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[2]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[4]/span[1]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[4]/span[1]").click()

element1 = driver.find_element_by_xpath("//*[@id='sciOutPut']").text
result2 = int(element1)

if result2 == 20:
    print("Test 2 passed")
else:
    print("Test 2 failed")

time.sleep(5)
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[5]/span[3]").click()
time.sleep(2)





#Addition Code


driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[4]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[2]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[3]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[1]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[2]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[3]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[1]").click()

driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[1]/span[4]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[3]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[1]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[2]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[3]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[1]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[2]").click()
element2 = driver.find_element_by_xpath("//*[@id='sciOutPut']").text
result3 = int(element2)

if result3 == 111111:
    print("Test 3 passed")
else:
    print("Test 3 failed")

time.sleep(5)
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[5]/span[3]").click()
time.sleep(2)








#subtrction code

driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[2]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[3]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[1]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[1]/span[2]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[2]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[3]").click()

driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[4]").click()

driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[4]").click()

driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[2]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[3]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[4]/span[1]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[1]/span[3]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[2]/span[1]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[1]/span[2]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[2]").click()
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[3]/span[3]").click()

element3 = driver.find_element_by_xpath("//*[@id='sciOutPut']").text
result4 = int(element3)

if result4 == 23329646:
    print("Test 4 passed")
else:
    print("Test 4 failed")

time.sleep(5)
driver.find_element_by_xpath("//*[@id='sciout']/tbody/tr[2]/td[2]/div/div[5]/span[3]").click()
time.sleep(2)



driver.close()