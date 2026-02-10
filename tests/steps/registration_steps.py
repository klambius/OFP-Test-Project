import allure
import pytest
from pytest_bdd import given, when, then, parsers

from pages.register_page import RegisterPage


@pytest.fixture
def register_page(driver):
    return RegisterPage(driver)


@given("открыта страница регистрации")
@allure.step("Открыть страницу регистрации")
def step_open_registration_page(register_page):
    register_page.open_page()


@when("пользователь заполняет форму регистрации валидными данными")
@allure.step("Заполнить форму регистрации валидными данными")
def step_fill_valid_form(register_page):
    register_page.fill_registration_form(
        first_name="Иван",
        last_name="Иванов",
        username="ivan_test_123",
        password="Password123!"
    )


@when("пользователь отправляет форму регистрации")
@allure.step("Отправить форму регистрации")
def step_submit_form(register_page):
    register_page.submit()


@then("отображается ошибка необходимости captcha")
@allure.step("Проверить, что отображается ошибка captcha")
def step_verify_captcha_error(register_page):
    assert register_page.is_error_displayed(), (
        "Ожидалось сообщение об ошибке captcha, но оно не появилось"
    )
    error_text = register_page.get_error_message_text()
    assert "captcha" in error_text.lower(
    ), f"Неожиданный текст ошибки: {error_text}"


@when(parsers.parse('пользователь вводит логин "{username}"'))
@allure.step("Ввести логин: {username}")
def step_enter_username(register_page, username):
    register_page.fill_username(username)


@then("поле логина должно быть невалидным")
@allure.step("Проверить, что поле логина невалидно (client-side)")
def step_username_invalid(register_page):
    assert not register_page.is_input_valid(register_page.USERNAME_INPUT), (
        "Поле логина должно быть невалидным"
    )
    msg = register_page.get_validation_message(register_page.USERNAME_INPUT)
    assert msg != "", "Ожидалось браузерное сообщение валидации для логина"


@when(parsers.parse('пользователь вводит пароль "{password}"'))
@allure.step("Ввести пароль: {password}")
def step_enter_password(register_page, password):
    register_page.fill_password(password)


@then("поле пароля должно быть невалидным")
@allure.step("Проверить, что поле пароля невалидно (client-side)")
def step_password_invalid(register_page):
    assert not register_page.is_input_valid(register_page.PASSWORD_INPUT), (
        "Поле пароля должно быть невалидным"
    )
    msg = register_page.get_validation_message(register_page.PASSWORD_INPUT)
    assert msg != "", "Ожидалось браузерное сообщение валидации для пароля"
