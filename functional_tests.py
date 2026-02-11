from selenium import webdriver
from selenium.webdriver.chrome.service import Service

google_driver_path = "/driver/chromedriver"

service = Service(executable_path=google_driver_path)
options = webdriver.ChromeOptions()
options.add_argument("--headless")

browser = webdriver.Chrome(
    options=options,
    service=service,
)
browser.get('http://localhost:8000')

print(1)
print(f"{browser.title=}")
assert 'Django' in browser.title

print(2)

browser.quit()
