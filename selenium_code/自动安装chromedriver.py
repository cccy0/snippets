# pip install webdriver-manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# https://mp.weixin.qq.com/s/8PWFZvegoMsl4T2m3H_9UA
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.quit()