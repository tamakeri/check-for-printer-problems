from selenium import webdriver
from selenium.webdriver.common.by import By
def go(adres):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    #adres="http://192.168.0.252:8000/rps/"
    driver.get(adres)

    driver.find_element(By.XPATH, '//*[@id="inputUsername"]').send_keys("admin")
    driver.find_element(By.XPATH, '//*[@id="inputPassword"]').send_keys("12345")
    driver.find_element(By.XPATH,'//*[@id="widgetProfileSubmit"]').click()



    tum_durum=(driver.find_element(By.XPATH,'//*[@id="MaintenanceInfomationModule"]').text)
    #toner=driver.find_element(By.XPATH,'//*[@id="tonerInfomationModule"]').text
    makine_ad=driver.find_element(By.XPATH,'//*[@id="productInformation"]/table/tbody/tr[2]/td').text
    makine_arıza=driver.find_element(By.XPATH,'//*[@id="deviceStatusModule"]').text
    return tum_durum ,makine_ad,makine_arıza
