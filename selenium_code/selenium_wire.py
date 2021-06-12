import json
import time
from pprint import pprint

from seleniumwire import webdriver  # Import from seleniumwire

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from urllib.parse import unquote, quote

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.netcourt.gov.cn/#lassen/announcement')
WebDriverWait(driver, 1000).until(EC.presence_of_element_located(
    (By.XPATH, '//li[@title="2"]')
)).click()
for request in driver.requests:
    if request.url == 'https://www.netcourt.gov.cn/portal/indexRpc/queryCourtTrialVos.json' and request.headers.get(
            'token'):
        pprint(request.headers)
        pprint(json.loads(request.response.body))
