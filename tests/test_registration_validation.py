from pages.register_page import RegisterPage


class TestRegistrationValidation:

    def test_username_starts_with_digit(self, driver):
        register_page = RegisterPage(driver)
        register_page.open_page()

        register_page.fill_registration_form(
            first_name="John",
            last_name="Doe",
            username="1username",
            password="Password123!"
        )
        register_page.submit()

        assert register_page.is_error_displayed(
        ), "Expected validation error, but none was shown"

        error_text = register_page.get_error_message_text()
        # На demoqa текст может отличаться, поэтому проверяем по смыслу (userName/username)
        assert "user" in error_text.lower(
        ), f"Unexpected error message: {error_text}"

    def test_password_less_than_8_characters(self, driver):
        register_page = RegisterPage(driver)
        register_page.open_page()

        register_page.fill_registration_form(
            first_name="John",
            last_name="Doe",
            username="john_doe_test123",
            password="1234567"
        )
        register_page.submit()

        assert register_page.is_error_displayed(
        ), "Expected password length error, but none was shown"

        error_text = register_page.get_error_message_text()
        # Обычно сообщение содержит "Password" и/или "8"
        assert "password" in error_text.lower() or "8" in error_text, (
            f"Unexpected error message: {error_text}"
        )
