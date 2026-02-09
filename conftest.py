import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument(
        "--disable-blink-features=AutomationControlled")
    chrome_options.add_extension("adblock.crx")  # добавляем расширение AdBlock

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
