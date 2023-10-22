from demoqa_tests.pages.RegistrationPage import RegistrationPage


def test_practice_form():
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_full_name("Irina", "Kirillova")
    registration_page.fill_email("IrinaQA@gmail.com")
    registration_page.gender("Female")
    registration_page.fill_number("8909898900")
    registration_page.fill_date_of_birth("28", "March", "1993")
    registration_page.fill_subject("Commerce")
    registration_page.fill_hobbies("Reading")
    registration_page.fill_image('Screenshot_1.png')
    registration_page.fill_address('Almaty, street Testovaya 1, 44')
    registration_page.fill_state_and_city('Haryana', 'Karnal')
    registration_page.click_button()

    registration_page.should_have_registrated_user_with(
        'Irina Kirillova',
        'IrinaQA@gmail.com',
        'Female',
        '8909898900',
        '28 March,1993',
        'Commerce',
        'Reading',
        'Screenshot_1.png',
        'Almaty, street Testovaya 1, 44',
        'Haryana Karnal',
    )
    registration_page.close_modal()

