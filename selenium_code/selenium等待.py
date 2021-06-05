# https://www.cnblogs.com/hkgov/p/13893061.html
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver')

# 全局隐式等待目标元素 最长等待事件5秒
driver.implicitly_wait(5)
driver.get('https://www.baidu.com')
try:
    driver.find_element_by_id('123')
except Exception as e:
    print(e)
finally:
    driver.quit()
