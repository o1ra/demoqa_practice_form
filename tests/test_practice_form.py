from demoqa_tests.pages.RegistrationPage import RegistrationPage
from demoqa_tests.users import user


def test_practice_form():
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_full_name(user.irina)
    registration_page.fill_email(user.irina)
    registration_page.gender(user.irina)
    registration_page.fill_number(user.irina)
    registration_page.fill_date_of_birth(user.irina)
    registration_page.fill_subject(user.irina)
    registration_page.fill_hobbies(user.irina)
    registration_page.fill_image(user.irina)
    registration_page.fill_address(user.irina)
    registration_page.fill_state_and_city(user.irina)
    registration_page.click_button()

    registration_page.should_have_registrated_user_with(user.irina)
    registration_page.close_modal()
