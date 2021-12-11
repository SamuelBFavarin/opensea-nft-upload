from selenium import webdriver

EXTENSION_PATH='assets/metamask.crx'
EXECUTABLE_PATH='assets/chromedriver'

opt = webdriver.ChromeOptions()
opt.add_extension(EXTENSION_PATH)

drive = webdriver.Chrome(executable_path=EXECUTABLE_PATH,
                         options=opt)



