from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import logging

EXTENSION_PATH='assets/metamask.crx'
EXECUTABLE_PATH='assets/chromedriver'


def create_webdrive_session() -> webdriver:
    opt = webdriver.ChromeOptions()
    opt.add_extension(EXTENSION_PATH)

    return webdriver.Chrome(executable_path=EXECUTABLE_PATH,
                            options=opt)

def get_config() -> json:
    with open('config.json', 'r') as openfile:
        return json.load(openfile)

def login_meta_mask(driver:webdriver, credentials:json) -> bool:

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
        time.sleep(5)

        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div/button').click()
        return True

    except Exception as e:
        logging.error(e)
        logging.error("Error on logging in metamask")
        return False

def login_opensea(driver:webdriver, credentials:json) -> bool:
    
    try:
        opensea_url = f"""https://opensea.io/collection/{credentials["collection_name"]}/assets/create"""
        driver.execute_script(f"""window.open('{opensea_url}', '_blank')""")
        driver.switch_to.window(driver.window_handles[2])
        time.sleep(7)

        driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/ul/li[1]/button').click()
        time.sleep(2)

        driver.switch_to.window(driver.window_handles[3])
        time.sleep(3)

        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]').click()
        time.sleep(3)

        driver.switch_to.window(driver.window_handles[3])
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
        time.sleep(3)

        driver.switch_to.window(driver.window_handles[3])
        driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[2]/div/div[3]/button[2]').click()
        time.sleep(5)
    except Exception as e:
        logging.error(e)
        logging.error("Error on logging in opensea")
        return False

if __name__ == '__main__':
    driver = create_webdrive_session()
    config = get_config()

    if login_meta_mask(driver, config['meta_mask_credentials']):
        if login_opensea(driver, config['opensea_credentials']):
            pass

