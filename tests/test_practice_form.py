from demoqa_tests.pages.RegistrationPage import RegistrationPage
from demoqa_tests.data import users_data


def test_practice_form():
    registration_page = RegistrationPage()

    registration_page.open()

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

    registration_page.should_have_registrated_user_with(users_data.irina)
    registration_page.close_modal()
