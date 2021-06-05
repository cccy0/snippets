from seleniumwire import webdriver  # Import from seleniumwire
# https://github.com/wkeeling/selenium-wire
# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Go to the Google home page
driver.get('https://www.bjcourt.gov.cn/ktgg/index.htm?c=&court=&start=2021-06-04&end=2021-07-04&type=&p=1')

# Access requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        print(
            request.url,
            request.response.status_code,
            request.response.headers['Content-Type']
        )
driver.quit()