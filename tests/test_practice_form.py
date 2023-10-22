from demoqa_tests.pages.RegistrationPage import RegistrationPage
from demoqa_tests.data import users_data


def test_practice_form():
    registration_page = RegistrationPage()
    irina = users_data.irina

    registration_page.open()
    registration_page.register_user(irina)
    registration_page.modal_form(irina)
