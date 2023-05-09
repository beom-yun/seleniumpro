from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

KEYWORD = "buy domain"

# Set chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)

browser.get("https://google.com")
search_bar = browser.find_element(By.CLASS_NAME, "gLFyf")
search_bar.send_keys(KEYWORD)
search_bar.send_keys(Keys.ENTER)

search_results = browser.find_elements(By.CLASS_NAME, "g")
for index, search_result in enumerate(search_results):
    try:
        search_result.screenshot(f"screenshots/{KEYWORD}x{index}.png")
    except:
        continue

browser.quit()
