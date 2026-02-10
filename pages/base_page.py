from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException,
)


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def click(self, locator) -> None:
        element = self.wait.until(ec.presence_of_element_located(locator))

        # прокрутка в центр экрана
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

        try:
            self.wait.until(ec.element_to_be_clickable(locator))
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            # fallback для CI / рекламы / iframe
            self.driver.execute_script("arguments[0].click();", element)

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

    def get_attr(self, locator, attr_name: str) -> str | None:
        element = self.find(locator)
        return element.get_attribute(attr_name)

    def is_input_valid(self, locator) -> bool:
        """
        Uses browser native validation (HTML5 constraint validation API).
        Returns True if element.checkValidity() is True, else False.
        """
        element = self.find(locator)
        return bool(self.driver.execute_script("return arguments[0].checkValidity();", element))

    def get_validation_message(self, locator) -> str:
        """
        Returns browser native validation message for invalid input.
        Empty string if valid.
        """
        element = self.find(locator)
        return str(self.driver.execute_script("return arguments[0].validationMessage;", element))
