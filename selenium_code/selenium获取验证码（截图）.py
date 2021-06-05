from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
try:
    driver.get('https://www.bjcourt.gov.cn/ktgg/index.htm?c=&court=&start=2021-06-04&end=2021-07-04&type=&p=13')
    img_base64 = driver.find_element_by_id('yzmImg').screenshot_as_base64
    img_png_bytes = driver.find_element_by_id('yzmImg').screenshot_as_png
    is_success:bool = driver.find_element_by_id('yzmImg').screenshot('yzm.png')
    driver.get('https://www.bjcourt.gov.cn/yzm.jpg')
    driver.save_screenshot('yzm.jpg')
finally:
    driver.quit()
