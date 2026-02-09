import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized --disable-extensions")

    # Получаем папку драйвера
    driver_folder = os.path.dirname(ChromeDriverManager().install())
    # Полный путь к chromedriver.exe
    driver_path = os.path.join(driver_folder, "chromedriver.exe")

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()