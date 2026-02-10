import pytest
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path

# project root: .../ (where pages/ is located)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# tests dir: .../tests (so "steps.*" imports work)
TESTS_DIR = Path(__file__).resolve().parent
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

pytest_plugins = (
    "steps.registration_steps"
)


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

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
