from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
    URL = "https://demoqa.com/register"

    # Locators
    FIRST_NAME_INPUT = (By.ID, "firstname")
    LAST_NAME_INPUT = (By.ID, "lastname")
    USERNAME_INPUT = (By.ID, "userName")
    PASSWORD_INPUT = (By.ID, "password")
    REGISTER_BUTTON = (By.ID, "register")
    BACK_TO_LOGIN_BUTTON = (By.ID, "gotologin")

    ERROR_MESSAGE = (By.ID, "name")  # общий контейнер ошибок

    def open_page(self) -> None:
        self.open(self.URL)

    def fill_first_name(self, first_name: str) -> None:
        self.type(self.FIRST_NAME_INPUT, first_name)

    def fill_last_name(self, last_name: str) -> None:
        self.type(self.LAST_NAME_INPUT, last_name)

    def fill_username(self, username: str) -> None:
        self.type(self.USERNAME_INPUT, username)

    def fill_password(self, password: str) -> None:
        self.type(self.PASSWORD_INPUT, password)

    def submit(self) -> None:
        self.click(self.REGISTER_BUTTON)

    def click_back_to_login(self) -> None:
        self.click(self.BACK_TO_LOGIN_BUTTON)

    def fill_registration_form(
        self,
        first_name: str,
        last_name: str,
        username: str,
        password: str
    ) -> None:
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_username(username)
        self.fill_password(password)

    def is_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_MESSAGE)

    def get_error_message_text(self) -> str:
        return self.get_text(self.ERROR_MESSAGE).strip()
