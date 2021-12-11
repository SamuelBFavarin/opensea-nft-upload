from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import logging

EXTENSION_PATH='assets/metamask.crx'
EXECUTABLE_PATH='assets/chromedriver'


def create_webdrive_session():
    opt = webdriver.ChromeOptions()
    opt.add_extension(EXTENSION_PATH)

    return webdriver.Chrome(executable_path=EXECUTABLE_PATH,
                            options=opt)

def get_login_config():
    with open('config.json', 'r') as openfile:
        return json.load(openfile)

def login_meta_mask(driver, credentials):

    try:
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])
        
        driver.find_element(By.TAG_NAME, 'button').click()
        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/form/div[4]/div[1]/div/input').send_keys(credentials["secret_phrase"])
        driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(credentials["password"])
        driver.find_element(By.XPATH, '//*[@id="confirm-password"]').send_keys(credentials["password"])
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div').click()
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/form/button').click()
       
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button').click()
        return True

    except Exception as e:
        logging.error(e)
        logging.error("Error on logging in metamask")
        return False


if __name__ == '__main__':
    driver = create_webdrive_session()
    login_config = get_login_config()

    login_meta_mask(driver, login_config['meta_mask_credentials'])

