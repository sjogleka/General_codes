import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

r = requests.get('https://sjogleka.github.io/')
print(r.headers)
print(r.status_code)
if r.status_code==200:
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
    driver.get("https://sjogleka.github.io/")
    driver.maximize_window()

    WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,"//a[@href='portfolio-single.html']")))
    mlPage = driver.find_element_by_xpath("//a[@href='portfolio-single.html']")
    action = ActionChains(driver).move_to_element(mlPage)
    mlPage.click()
    #gitML = driver.find_element_by_xpath("//a[@href='https://github.com/sjogleka/Machine-Learning']")
    #driver.implicitly_wait(30)
    #gitML.click()
    driver.__exit__()