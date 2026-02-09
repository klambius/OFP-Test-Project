from pages.register_page import RegisterPage


class TestRegistrationPositive:

    def test_registration_with_valid_data(self, driver):
        register_page = RegisterPage(driver)

        register_page.open_page()
        register_page.fill_registration_form(
            first_name="John",
            last_name="Doe",
            username="john_doe_test123",
            password="Password123!"
        )
        register_page.click_captcha
        register_page.submit()
        
        assert register_page.is_error_displayed(), (
            "Expected error message due to missing CAPTCHA, "
            "but no error was displayed"
        )
