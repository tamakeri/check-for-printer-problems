from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#CODED FOR TWO TYPES OF DEVİCES MAY NEED MANUEL CHANGİNG

def go(adres):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(adres)
    driver.find_element(By.XPATH, '//*[@id="inputUsername"]').send_keys("YOUR  USERİNTERFACE NAME")
    driver.find_element(By.XPATH, '//*[@id="inputPassword"]').send_keys("YOUR USER İNTERFACE PASSWORD")
    driver.find_element(By.XPATH,'//*[@id="widgetProfileSubmit"]').click()
    time.sleep(10)
    tum_durum=(driver.find_element(By.XPATH,'//*[@id="MaintenanceInfomationModule"]').text)
    makine_ad=driver.find_element(By.XPATH,'//*[@id="productInformation"]/table/tbody/tr[2]/td').text
    makine_arıza=driver.find_element(By.XPATH,'//*[@id="deviceStatusModule"]').text
    driver.quit()

    return tum_durum ,makine_ad,makine_arıza


def other_type(adres):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(adres)
    driver.find_element(By.XPATH, '//*[@id="i0019"]').send_keys("admin")
    driver.execute_script("""document.querySelector("#submitButton").click()""")
    kagıt_kartus=(driver.find_element(By.XPATH,'//*[@id="MaintenanceInfomationModule"]').text)
    makine_arıza=driver.find_element(By.XPATH, '//*[@id="deviceErrorInfoModule"]').text
    makine_ad=driver.find_element(By.XPATH,'//*[@id="productInformation"]/table/tbody/tr[2]/td').text
    return kagıt_kartus ,makine_ad,makine_arıza
