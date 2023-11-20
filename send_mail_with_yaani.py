from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


def ilk_çalışma():
    driver.get("https://mail.istesuit.com/home/login")
    time.sleep(5)
    driver.execute_script("location.reload();")
    driver.find_element(
        By.XPATH, '//*[@id="input-email"]').send_keys("YOUR EMAİL ")
    time.sleep(5)
    driver.execute_script(
        "document.querySelector(\"body > div > main > section > div > div > form > div.form__action.flex.justify-end > button\").click()")
    time.sleep(5)
    driver.find_element(
        By.XPATH, '//*[@id="input-password"]').send_keys(" YOUR PASSWORD HERE")
    time.sleep(5)
    driver.execute_script(
        "document.querySelector(\"body > div > main > section > div > div > form > div.form__action.flex.justify-space-between > button\").click()")
    time.sleep(5)
    driver.execute_script(
        "document.querySelector(\"body > modal-container > div.modal-dialog.modal-dialog-centered.modal-large > div > app-common-modal > div.modal-header > div:nth-child(2) > button > i\").click()")
    print("ilk çalışma tamam")


# now it is  about to be Qsending
def gonder(kime, içerik):
    driver.get(
        "https://mail.istesuit.com/m/"+              "YOUR MAİL HERE" +"PRIMARY/inbox/compose")
    time.sleep(5)
    driver.find_element(
        By.XPATH, "/html/body/app-root/app-layout/app-mailbox-layout/div/section/app-mailbox/div/div/div[2]/app-compose/app-sender/div/div/form/div[2]/div[1]/div[2]/app-recipient-suggestion/ngym-tag-container/div/div/ngym-tag-input/form/input").send_keys(kime)
    driver.find_element(
        By.XPATH, "/html/body/app-root/app-layout/app-mailbox-layout/div/section/app-mailbox/div/div/div[2]/app-compose/app-sender/div/div/form/div[2]/div[4]/div[2]/div[1]").send_keys(içerik)
    time.sleep(2)

    driver.execute_script("""document.querySelector("body > app-root > app-layout > app-mailbox-layout > div > section > app-mailbox > div > div > div.mb-view.resizeable.print-container > app-compose > app-sender > div > div > form > div:nth-child(2) > div.d-flex.justify-content-end.py-2.bt > button.btn.btn-small.btn-primary.robot_sender_sendButton").click();""")
    driver.execute_script("""document.querySelector("body > app-root > app-layout > app-mailbox-layout > div > section > app-mailbox > div > div > div.mb-view.resizeable.print-container > app-compose > app-sender > div > div > form > div:nth-child(2) > div.d-flex.justify-content-end.py-2.bt > button.btn.btn-small.btn-primary.robot_sender_sendButton").click();""")
    driver.execute_script("""document.querySelector("body > app-root > app-layout > app-mailbox-layout > div > section > app-mailbox > div > div > div.mb-view.resizeable.print-container > app-compose > app-sender > div > div > form > div:nth-child(2) > div.d-flex.justify-content-end.py-2.bt > button.btn.btn-small.btn-primary.robot_sender_sendButton").click();""")
    time.sleep(5)
