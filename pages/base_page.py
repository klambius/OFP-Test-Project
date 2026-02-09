from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def click(self, locator) -> None:
        element = self.wait.until(ec.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text: str) -> None:
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def is_visible(self, locator) -> bool:
        try:
            self.wait.until(ec.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def get_text(self, locator) -> str:
        return self.find(locator).text
