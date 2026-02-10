from pages.register_page import RegisterPage


class TestRegistrationValidation:

    def test_username_starts_with_digit_client_validation(self, driver):
        register_page = RegisterPage(driver)
        register_page.open_page()

        register_page.fill_registration_form(
            first_name="John",
            last_name="Doe",
            username="1username",
            password="Password123!"
        )

        # Проверяем клиентскую валидность username без сабмита
        assert not register_page.is_input_valid(register_page.USERNAME_INPUT), (
            "Username starting with a digit should be invalid by client-side validation"
        )

        validation_msg = register_page.get_validation_message(
            register_page.USERNAME_INPUT)
        assert validation_msg != "", "Expected browser validation message for invalid username"

    def test_password_less_than_8_characters_client_validation(self, driver):
        register_page = RegisterPage(driver)
        register_page.open_page()

        register_page.fill_registration_form(
            first_name="John",
            last_name="Doe",
            username="john_doe_test123",
            password="1234567"
        )

        # Проверяем minlength/валидность password без сабмита
        assert not register_page.is_input_valid(register_page.PASSWORD_INPUT), (
            "Password shorter than 8 characters should be invalid by client-side validation"
        )

        validation_msg = register_page.get_validation_message(
            register_page.PASSWORD_INPUT)
        assert validation_msg != "", "Expected browser validation message for invalid password"
