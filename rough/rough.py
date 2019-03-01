import os
print(os.getcwd())
driver_loc = os.getcwd().replace("\\","/")+"/drivers"

from selenium import webdriver
driver=webdriver.Chrome(executable_path=driver_loc+"/chromedriver.exe")