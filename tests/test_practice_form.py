import allure

from demoqa_tests.pages.registration_page import RegistrationPage
from demoqa_tests.data import users_data


@allure.title("Successful fill form")
def test_practice_form():
    registration_page = RegistrationPage()

    with allure.step("Open registrations form"):
        registration_page.open()

    with allure.step("Fill form"):
        registration_page.fill_full_name(users_data.irina)
        registration_page.fill_email(users_data.irina)
        registration_page.gender(users_data.irina)
        registration_page.fill_number(users_data.irina)
        registration_page.fill_date_of_birth(users_data.irina)
        registration_page.fill_subject(users_data.irina)
        registration_page.fill_hobbies(users_data.irina)
        registration_page.fill_image(users_data.irina)
        registration_page.fill_address(users_data.irina)
        registration_page.fill_state_and_city(users_data.irina)
        registration_page.click_button()

    with allure.step("Check form results"):
        registration_page.should_have_registrated_user_with(users_data.irina)
        registration_page.close_modal()
